import os
import shutil


def move_files(path, music, videos, pictures, documents, applications, archives):

    music_ext = [
        ".mp3",
        ".m4a",
        ".wav",
        ".wma",
        ".aac",
        ".flac",
        ".alac"
    ]

    videos_ext = [
        ".mp4",
        ".3gp",
        ".webm",
        ".mov",
        ".mpeg",
        ".avi",
        ".mkv",
        ".wmv",
        ".flv",
        ".ogg"
    ]

    pictures_ext = [
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".tiff",
        ".raw",
        ".svg",
        ".webp",
        ".ai",
        ".tif",
        ".bmp",
        ".eps",
        ".cr2",
        ".nef",
        ".orf",
        ".avif"
    ]

    documents_ext = [
        ".pdf",
        ".epub",
        ".doc",
        ".docx",
        ".html",
        ".htm",
        ".xls",
        ".xlsx",
        ".txt",
        ".csv",
        ".mobi"
    ]

    applications_ext = [
        ".exe",
        ".apk",
        ".deb",
        ".app"
    ]

    archives_ext = [
        ".zip"
    ]

    files = os.listdir(path)

    for file in files:
        filepath = f"{path}/{file}"
        ext = os.path.splitext(filepath)[1]
        if ext in music_ext:
            shutil.move(filepath, music)
        elif ext in videos_ext:
            shutil.move(filepath, videos)
        elif ext in pictures_ext:
            shutil.move(filepath, pictures)
        elif ext in documents_ext:
            shutil.move(filepath, documents)
        elif ext in applications_ext:
            shutil.move(filepath, applications)
        elif ext in archives_ext:
            shutil.move(filepath, archives)
    return 0