import os
import shutil


def move_files(path, music, videos, pictures, documents, applications, archives, miscellaneous):

    music_ext = [
        ".aa",
        ".aac",
        ".aax",
        ".act",
        ".aiff",
        ".amr",
        ".ape",
        ".au",
        ".dvf",
        ".flac",
        ".m4a",
        ".m4b",
        ".mp3",
        ".mogg",
        ".ra",
        ".rm",
        ".vox",
        ".wav",
        ".tta",
        ".wma",
        ".wv"
    ]

    videos_ext = [
        ".webm",
        ".mkv",
        ".flv",
        ".vob",
        ".drc",
        ".gifv",
        ".mng",
        ".avi",
        ".mov",
        ".qt",
        ".wmv",
        ".yuv",
        ".rm",
        ".rmvb",
        ".asf",
        ".mp4",
        ".m4p",
        ".m4v",
        ".mpg",
        ".mp2",
        ".mpeg",
        ".mpe",
        ".mpv",
        ".3gp",
        ".3g2",
        ".flv",
        ".f4v",
        ".f4p"
    ]

    pictures_ext = [
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".ico",
        ".bmp",
        ".cpt",
        ".psd",
        ".psp",
        ".xcf",
        ".ppm",
        ".pgm",
        ".pbm",
        ".pnm"
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
        ".mobi",
        "ppt",
        "pptx",
        "xml",
        "css",
        "js",
        "php"
    ]

    applications_ext = [
        ".exe",
        ".apk",
        ".deb",
        ".app",
        ".msi",
        ".cmd",
        ".bin"
    ]

    archives_ext = [
        ".zip",
        "rar",
        "7z",
        "cab"
    ]


    files = os.listdir(path)
    created_folders = ["Pictures", "Music", "Videos", "Documents", "Applications", "Archives"]

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
        else:
            if file in created_folders:
                continue
            shutil.move(filepath, miscellaneous)
    return 0