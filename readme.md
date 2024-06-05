# Datei-Manager Skript

Dieses Skript ermöglicht das Verschieben oder Löschen von Dateien, basierend auf einem config.file (`config.json`). Das Skript durchsucht ein Quellverzeichnis und führt Aktionen aus, die durch Kommandozeilenparameter gesteuert werden.

## Beispiel Config (`config.json`)

Erstelle eine `config.json` Datei im gleichen Verzeichnis wie das Skript. Diese Datei definiert die Regeln für das Verschieben und Löschen von Dateien. Beispiel:

```json
{
  "images": {
    "destination": "Bilder",
    "extension": [
      "png",
      "jpg",
      "jpeg",
      "gif",
      "bmp",
      "tiff",
      "svg",
      "webp",
      "ico"
    ]
  },
  "documents": {
    "destination": "Dokumente",
    "extension": [
      "pdf",
      "doc",
      "docx",
      "txt",
      "xls",
      "xlsx",
      "ppt",
      "pptx"
    ]
  },
  "music": {
    "destination": "Musik",
    "extension": [
      "mp3",
      "wav",
      "aac",
      "flac",
      "m4a",
      "wma"
    ]
  },
  "videos": {
    "destination": "Videos",
    "extension": [
      "mp4",
      "mkv",
      "avi",
      "mov",
      "wmv",
      "flv"
    ]
  },
  "archives": {
    "destination": "Archive",
    "extension": [
      "zip",
      "rar",
      "tar",
      "gz",
      "7z"
    ]
  },
  "scripts": {
    "destination": "Skripte",
    "extension": [
      "py",
      "js",
      "sh",
      "bat",
      "rb",
      "pl"
    ]
  },
  "delete": {
    "extension": [
      "tmp",
      "log",
      "bak"
    ]
  }
}
```


## Nutzung

### Download

Das Verzeichnis herunterladen und in das Homedirectory ablegen.

```bash
cd ~
git clone https://github.com/sleeps21/afilr.git afilr
```
### Skript ausführen

    Dateien verschieben: Um Dateien zu verschieben, nutze den -m Parameter:

```bash
python afilr/script.py -m [source_directory]
```


Dateien löschen: Um Dateien zu löschen, nutze den -d Parameter:

```bash
python afilr/script.py -d [source_directory]
```

Falls kein Quellverzeichnis angegeben wird, wird standardmäßig das ~/Downloads Verzeichnis genutzt.
#### Log-Datei

Das Skript erstellt eine log.txt Datei, die alle ausgeführten Aktionen protokolliert. Jede Transaktion wird mit einem Zeitstempel und einer Trennlinie festgehalten.
