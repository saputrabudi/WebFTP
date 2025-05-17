# WebFTP

Eine webbasierte Anwendung zur Verwaltung von Dateien über FTP, ähnlich wie WinSCP, aber mit einer einfacheren Weboberfläche.

## Funktionen

- **FTP-Datei-Browser**: Verzeichnisse und Dateien auf dem FTP-Server durchsuchen
- **Code-Editor**: Quellcode-Dateien mit Syntax-Hervorhebung bearbeiten
- **Website-Vorschau**: HTML-Dateien und Bilder in der Vorschau anzeigen
- **Dateiverwaltung**: Dateien hochladen, herunterladen und löschen
- **Verzeichnisverwaltung**: Verzeichnisse erstellen und löschen

## Anforderungen

- Python 3.6+
- Flask
- pyftpdlib
- und andere Abhängigkeiten (siehe requirements.txt)

## Installation

1. Klonen Sie dieses Repository:
   ```
   git clone https://github.com/username/WebFTP.git
   cd WebFTP
   ```

2. Erstellen und aktivieren Sie eine virtuelle Umgebung (optional):
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Installieren Sie die Abhängigkeiten:
   ```
   pip install -r requirements.txt
   ```

4. Starten Sie die Anwendung:
   ```
   python app.py
   ```

5. Öffnen Sie Ihren Browser und greifen Sie auf die Anwendung unter `http://localhost:9000` zu

## Verwendung

1. **FTP-Login**: Geben Sie Ihren FTP-Host, Port, Benutzernamen und Passwort ein
2. **Dateien durchsuchen**: Nach dem Einloggen können Sie Dateien und Verzeichnisse durchsuchen
3. **Dateien bearbeiten**: Klicken Sie auf die Schaltfläche "Bearbeiten" bei der Datei, die Sie bearbeiten möchten
4. **Vorschau**: Klicken Sie auf die Schaltfläche "Ansehen" bei HTML-Dateien, um eine Vorschau zu sehen
5. **Dateien hochladen**: Klicken Sie auf "Datei hochladen" und wählen Sie eine Datei von Ihrem Computer aus
6. **Verzeichnis erstellen**: Klicken Sie auf "Verzeichnis erstellen" und geben Sie einen Namen für das neue Verzeichnis ein

## Sicherheit

Diese Anwendung verwendet Standard-FTP-Verbindungen, die nicht verschlüsselt sind. Verwenden Sie sie nicht für sensible Dateien oder in unsicheren Netzwerken. Für bessere Sicherheit sollten Sie SFTP oder FTPS in Betracht ziehen.

## Lizenz

MIT-Lizenz. Weitere Details finden Sie in der LICENSE-Datei.

by Saputra Budi 