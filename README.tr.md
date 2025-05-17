# WebFTP

WinSCP'ye benzer ancak daha basit bir web arayüzüne sahip, FTP üzerinden dosya yönetimi için web tabanlı bir uygulama.

## Özellikler

- **FTP Dosya Tarayıcısı**: FTP sunucusundaki dizinleri ve dosyaları görüntüleme
- **Kod Düzenleyici**: Sözdizimi vurgulamalı kaynak kod dosyalarını düzenleme
- **Web Sitesi Önizlemesi**: HTML dosyalarını ve resimleri önizleme
- **Dosya Yönetimi**: Dosya yükleme, indirme ve silme
- **Dizin Yönetimi**: Dizin oluşturma ve silme

## Gereksinimler

- Python 3.6+
- Flask
- pyftpdlib
- ve diğer bağımlılıklar (requirements.txt dosyasına bakın)

## Kurulum

1. Bu depoyu klonlayın:
   ```
   git clone https://github.com/username/WebFTP.git
   cd WebFTP
   ```

2. Sanal ortam oluşturun ve etkinleştirin (isteğe bağlı):
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Bağımlılıkları yükleyin:
   ```
   pip install -r requirements.txt
   ```

4. Uygulamayı çalıştırın:
   ```
   python app.py
   ```

5. Tarayıcınızı açın ve uygulamaya `http://localhost:9000` adresinden erişin

## Kullanım

1. **FTP Girişi**: FTP sunucu adresi, port, kullanıcı adı ve şifrenizi girin
2. **Dosyaları Görüntüleme**: Giriş yaptıktan sonra, dosyaları ve dizinleri görüntüleyebilirsiniz
3. **Dosya Düzenleme**: Düzenlemek istediğiniz dosyanın "Düzenle" düğmesine tıklayın
4. **Önizleme**: HTML dosyalarını önizlemek için "Görüntüle" düğmesine tıklayın
5. **Dosya Yükleme**: "Dosya Yükle" düğmesine tıklayın ve bilgisayarınızdan bir dosya seçin
6. **Dizin Oluşturma**: "Dizin Oluştur" düğmesine tıklayın ve yeni dizin için bir isim girin

## Güvenlik

Bu uygulama, şifrelenmemiş standart FTP bağlantılarını kullanır. Hassas dosyalar veya güvenli olmayan ağlarda kullanmayın. Daha iyi güvenlik için SFTP veya FTPS kullanmayı düşünün.

## Lisans

MIT Lisansı. Daha fazla ayrıntı için LICENSE dosyasına bakın.

by Saputra Budi 