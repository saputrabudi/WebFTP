# WebFTP

Web-based application for managing files via FTP, similar to WinSCP but with a simpler web interface.

## Features

- **FTP File Browser**: Browse directories and files on FTP server
- **Code Editor**: Edit source code files with syntax highlighting
- **Website Preview**: View HTML files and images preview
- **File Management**: Upload, download, and delete files
- **Directory Management**: Create and delete directories

## Requirements

- Python 3.6+
- Flask
- pyftpdlib
- and other dependencies (see requirements.txt)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/username/WebFTP.git
   cd WebFTP
   ```

2. Create and activate virtual environment (optional):
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and access the application at `http://localhost:9000`

## Usage

1. **FTP Login**: Enter your FTP host, port, username, and password
2. **Browse Files**: After logging in, you can browse files and directories
3. **Edit Files**: Click the "Edit" button on the file you want to edit
4. **Preview**: Click the "View" button on HTML files to see a preview
5. **Upload Files**: Click "Upload File" and select a file from your computer
6. **Create Directory**: Click "Create Directory" and enter a name for the new directory

## Security

This application uses standard FTP connections which are not encrypted. Do not use for sensitive files or on unsecured networks. For better security, consider using SFTP or FTPS.

## License

MIT License. See LICENSE file for more details.

by Saputra Budi 