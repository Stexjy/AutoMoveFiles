from watchdog.events import FileSystemEventHandler

import os

class AutoMoveHandler(FileSystemEventHandler):

    def __init__(self, folderToTrack, folderDestination, extensions):
        self.folderToTrack = folderToTrack
        self.folderDestination = folderDestination
        self.extensions = extensions

    def on_modified(self, event):
        
        for filename in os.listdir(self.folderToTrack):
            
            for extension in self.extensions:

                if extension in filename:
                    
                    src = self.folderToTrack + "/" + filename
                    newDestination = self.folderDestination + "/" + filename

                    if os.listdir(self.folderDestination).count(filename) > 0:
                        i = 1

                        for copy in os.listdir(self.folderDestination):
                            if copy.startswith(filename + " - Copy "):
                                i = int(copy.replace(filename + " - Copy ", "")) + 1

                        newDestination = newDestination + " - Copy " + str(i)

                    os.rename(src, newDestination)