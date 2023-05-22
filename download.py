#I made this to not clutter up main.py, I probably could've done it better but DEAL WITH IT
import requests
import os

user = os.getlogin()
insdir = f'/home/{user}/Morpheus/'
downloadgui = 'https://raw.githubusercontent.com/s1csty9/Morpheus/main/gui.py'
saveguipath = f'{insdir}gui.py'
response = requests.get(downloadgui)
 if response.status_code == 200:
    with open(saveguipath, 'wb') as file:
        file.write(response.content)
