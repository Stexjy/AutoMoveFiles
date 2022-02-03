import requests
import os

version = open(__file__.replace("AutoMoveFiles" + os.path.sep + "checkupdates.py", "") + os.path.sep + "version.txt").read()

url = "https://raw.githubusercontent.com/Stexjy/AutoMoveFiles/main/version.txt"
newVersion = requests.get(url).text

def update():
    dir = __file__.replace(os.path.sep + "checkupdates.py", "")
    url2 = "https://github.com/Stexjy/AutoMoveFiles/tree/main/AutoMoveFiles"
    print(requests.get(url2).text)

if version != newVersion:
    update()