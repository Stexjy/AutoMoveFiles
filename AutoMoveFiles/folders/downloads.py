from folders.autoMoveHandler import AutoMoveHandler

class Downloads:
    def loadHandlers(observer):
        downloadImageHandler = AutoMoveHandler("/home/stefano/Scaricati", "/home/stefano/Immagini", (".jpg", ".png", ".gif", ".bpm"))
        downloadVideoHandler = AutoMoveHandler("/home/stefano/Scaricati", "/home/stefano/Video", (".mp4", ".mkv"))
        downloadAudioHandler = AutoMoveHandler("/home/stefano/Scaricati", "/home/stefano/Musica", (".mp3"))
        downloadDocumentsHandler = AutoMoveHandler("/home/stefano/Scaricati", "/home/stefano/Documenti", (".docx", ".pttx", ".xlsx"))

        observer.schedule(downloadImageHandler, downloadImageHandler.folderToTrack, recursive=True)