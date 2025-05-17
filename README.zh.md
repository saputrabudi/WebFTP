# WebFTP

一个基于Web的FTP文件管理应用程序，类似于WinSCP，但具有更简单的Web界面。

## 功能

- **FTP文件浏览器**：浏览FTP服务器上的目录和文件
- **代码编辑器**：使用语法高亮编辑源代码文件
- **网站预览**：查看HTML文件和图像预览
- **文件管理**：上传、下载和删除文件
- **目录管理**：创建和删除目录

## 要求

- Python 3.6+
- Flask
- pyftpdlib
- 以及其他依赖项（请参阅requirements.txt）

## 安装

1. 克隆此仓库：
   ```
   git clone https://github.com/username/WebFTP.git
   cd WebFTP
   ```

2. 创建并激活虚拟环境（可选）：
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. 安装依赖项：
   ```
   pip install -r requirements.txt
   ```

4. 运行应用程序：
   ```
   python app.py
   ```

5. 打开浏览器并访问 `http://localhost:9000` 来使用应用程序

## 使用方法

1. **FTP登录**：输入您的FTP主机、端口、用户名和密码
2. **浏览文件**：登录后，您可以浏览文件和目录
3. **编辑文件**：点击要编辑的文件上的"编辑"按钮
4. **预览**：点击HTML文件上的"查看"按钮以查看预览
5. **上传文件**：点击"上传文件"并从您的计算机中选择文件
6. **创建目录**：点击"创建目录"并输入新目录的名称

## 安全性

此应用程序使用未加密的标准FTP连接。请勿在敏感文件或不安全的网络上使用。为了更好的安全性，请考虑使用SFTP或FTPS。

## 许可证

MIT许可证。有关更多详细信息，请参阅LICENSE文件。

by Saputra Budi 