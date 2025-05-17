from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
import os
import ftplib
import tempfile
import mimetypes
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'temp_uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max 16MB

# Pastikan direktori temporary ada
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    if 'ftp_host' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            host = request.form['host']
            port = int(request.form['port'])
            username = request.form['username']
            password = request.form['password']
            
            # Coba koneksi ke server FTP
            ftp = ftplib.FTP()
            ftp.connect(host, port)
            ftp.login(username, password)
            ftp.quit()
            
            # Simpan detail koneksi di session
            session['ftp_host'] = host
            session['ftp_port'] = port
            session['ftp_username'] = username
            session['ftp_password'] = password
            
            flash('Login berhasil!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Login gagal: {str(e)}', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Anda telah keluar dari sesi', 'info')
    return redirect(url_for('login'))

@app.route('/browse', methods=['GET'])
def browse():
    if 'ftp_host' not in session:
        return redirect(url_for('login'))
    
    current_path = request.args.get('path', '/')
    
    try:
        ftp = ftplib.FTP()
        ftp.connect(session['ftp_host'], session['ftp_port'])
        ftp.login(session['ftp_username'], session['ftp_password'])
        
        # Navigasi ke direktori yang ditentukan
        if current_path != '/':
            ftp.cwd(current_path)
        
        # Dapatkan konten direktori
        files = []
        directories = []
        
        # Tampung hasil LIST lengkap
        dir_listing = []
        ftp.retrlines('LIST', dir_listing.append)
        
        # Proses setiap baris listing
        for line in dir_listing:
            # Format listing biasanya: "perms links owner group size month day time/year name"
            parts = line.split(None, 8)
            if len(parts) < 9:
                continue
                
            name = parts[8]
            # Jika diawali dengan 'd', itu adalah direktori
            if parts[0].startswith('d'):
                directories.append(name)
            else:
                files.append(name)
        
        # Membersihkan
        ftp.quit()
        
        return render_template('browse.html', 
                              current_path=current_path,
                              files=files, 
                              directories=directories,
                              parent_path=os.path.dirname(current_path) if current_path != '/' else '/')
    
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('index'))

@app.route('/edit', methods=['GET', 'POST'])
def edit_file():
    if 'ftp_host' not in session:
        return redirect(url_for('login'))
    
    file_path = request.args.get('path')
    
    if request.method == 'POST':
        try:
            content = request.form['content']
            
            # Simpan konten yang diedit ke file sementara
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file.write(content.encode('utf-8'))
            temp_file.close()
            
            # Upload file ke server FTP
            ftp = ftplib.FTP()
            ftp.connect(session['ftp_host'], session['ftp_port'])
            ftp.login(session['ftp_username'], session['ftp_password'])
            
            with open(temp_file.name, 'rb') as f:
                ftp.storbinary(f'STOR {file_path}', f)
            
            # Membersihkan
            ftp.quit()
            os.unlink(temp_file.name)
            
            flash('File berhasil disimpan!', 'success')
            return redirect(url_for('browse', path=os.path.dirname(file_path)))
        
        except Exception as e:
            flash(f'Error menyimpan file: {str(e)}', 'danger')
    
    try:
        # Ambil konten file dari server FTP
        ftp = ftplib.FTP()
        ftp.connect(session['ftp_host'], session['ftp_port'])
        ftp.login(session['ftp_username'], session['ftp_password'])
        
        # Simpan ke file sementara
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        ftp.retrbinary(f'RETR {file_path}', temp_file.write)
        temp_file.close()
        
        # Baca konten file
        with open(temp_file.name, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        # Membersihkan
        ftp.quit()
        os.unlink(temp_file.name)
        
        file_name = os.path.basename(file_path)
        return render_template('edit.html', file_path=file_path, file_name=file_name, content=content)
    
    except Exception as e:
        flash(f'Error membuka file: {str(e)}', 'danger')
        return redirect(url_for('browse', path=os.path.dirname(file_path) if file_path else '/'))

@app.route('/preview', methods=['GET'])
def preview_file():
    if 'ftp_host' not in session:
        return redirect(url_for('login'))
    
    file_path = request.args.get('path')
    
    try:
        # Ambil file dari server FTP
        ftp = ftplib.FTP()
        ftp.connect(session['ftp_host'], session['ftp_port'])
        ftp.login(session['ftp_username'], session['ftp_password'])
        
        # Simpan ke file sementara
        file_name = os.path.basename(file_path)
        local_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file_name))
        
        with open(local_path, 'wb') as f:
            ftp.retrbinary(f'RETR {file_path}', f.write)
        
        # Membersihkan
        ftp.quit()
        
        # Deteksi mime type
        mime_type, _ = mimetypes.guess_type(file_path)
        
        if mime_type and mime_type.startswith('text/html'):
            return render_template('preview.html', file_path=file_path, local_path=local_path)
        elif mime_type and (mime_type.startswith('image/') or mime_type.startswith('text/')):
            return send_from_directory(app.config['UPLOAD_FOLDER'], secure_filename(file_name))
        else:
            flash('Tipe file tidak dapat di-preview', 'warning')
            return redirect(url_for('browse', path=os.path.dirname(file_path)))
    
    except Exception as e:
        flash(f'Error preview file: {str(e)}', 'danger')
        return redirect(url_for('browse', path=os.path.dirname(file_path) if file_path else '/'))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'ftp_host' not in session:
        return redirect(url_for('login'))
    
    current_path = request.args.get('path', '/')
    
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Tidak ada file yang diunggah', 'danger')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('Tidak ada file yang dipilih', 'danger')
            return redirect(request.url)
        
        if file:
            try:
                # Simpan file sementara
                filename = secure_filename(file.filename)
                local_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(local_path)
                
                # Unggah ke server FTP
                ftp = ftplib.FTP()
                ftp.connect(session['ftp_host'], session['ftp_port'])
                ftp.login(session['ftp_username'], session['ftp_password'])
                
                # Navigasi ke direktori yang ditentukan
                if current_path != '/':
                    ftp.cwd(current_path)
                
                # Unggah file
                with open(local_path, 'rb') as f:
                    ftp.storbinary(f'STOR {filename}', f)
                
                # Membersihkan
                ftp.quit()
                os.remove(local_path)
                
                flash('File berhasil diunggah!', 'success')
                return redirect(url_for('browse', path=current_path))
            
            except Exception as e:
                flash(f'Error mengunggah file: {str(e)}', 'danger')
                return redirect(url_for('browse', path=current_path))
    
    return render_template('upload.html', current_path=current_path)

@app.route('/mkdir', methods=['GET', 'POST'])
def make_directory():
    if 'ftp_host' not in session:
        return redirect(url_for('login'))
    
    current_path = request.args.get('path', '/')
    
    if request.method == 'POST':
        try:
            dirname = request.form['dirname']
            
            # Buat direktori di server FTP
            ftp = ftplib.FTP()
            ftp.connect(session['ftp_host'], session['ftp_port'])
            ftp.login(session['ftp_username'], session['ftp_password'])
            
            # Navigasi ke direktori yang ditentukan
            if current_path != '/':
                ftp.cwd(current_path)
            
            # Buat direktori baru
            ftp.mkd(dirname)
            
            # Membersihkan
            ftp.quit()
            
            flash('Direktori berhasil dibuat!', 'success')
            return redirect(url_for('browse', path=current_path))
        
        except Exception as e:
            flash(f'Error membuat direktori: {str(e)}', 'danger')
            return redirect(url_for('browse', path=current_path))
    
    return render_template('mkdir.html', current_path=current_path)

@app.route('/delete', methods=['GET', 'POST'])
def delete_item():
    if 'ftp_host' not in session:
        return redirect(url_for('login'))
    
    item_path = request.args.get('path')
    is_dir = request.args.get('is_dir', 'false') == 'true'
    
    try:
        ftp = ftplib.FTP()
        ftp.connect(session['ftp_host'], session['ftp_port'])
        ftp.login(session['ftp_username'], session['ftp_password'])
        
        if is_dir:
            # Implementasi sederhana, tidak menghapus direktori yang berisi file
            ftp.rmd(item_path)
            flash('Direktori berhasil dihapus!', 'success')
        else:
            ftp.delete(item_path)
            flash('File berhasil dihapus!', 'success')
        
        # Membersihkan
        ftp.quit()
        
        return redirect(url_for('browse', path=os.path.dirname(item_path) if item_path != '/' else '/'))
    
    except Exception as e:
        flash(f'Error menghapus item: {str(e)}', 'danger')
        return redirect(url_for('browse', path=os.path.dirname(item_path) if item_path != '/' else '/'))

if __name__ == '__main__':
    app.run(debug=True, port=9000, host='0.0.0.0') 