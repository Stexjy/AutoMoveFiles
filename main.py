from time import time
from watchdog.observers import Observer
from folders.downloads import Downloads

import time

observer = Observer()

# Loading event Handlers
Downloads.loadHandlers(observer)

observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()