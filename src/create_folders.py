import os


def create_folders(path):
    music = f"{path}/Music"
    if not os.path.exists(music):
        os.mkdir(music)
    videos = f"{path}/Videos"
    if not os.path.exists(videos):
        os.mkdir(videos)
    pictures = f"{path}/Pictures"
    if not os.path.exists(pictures):
        os.mkdir(pictures)
    documents = f"{path}/Documents"
    if not os.path.exists(documents):
        os.mkdir(documents)
    applications = f"{path}/Applications"
    if not os.path.exists(applications):
        os.mkdir(applications)
    archives = f"{path}/Archives"
    if not os.path.exists(archives):
        os.mkdir(archives)
    miscellaneous = f"{path}/Miscellaneous"
    if not os.path.exists(miscellaneous):
        os.mkdir(miscellaneous)  

    return (music, videos, pictures, documents, applications, archives, miscellaneous)