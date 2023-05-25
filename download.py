#woo! optimisation! I'm a fucking genius!
import requests
import os

user = os.getlogin()
insdir = f'/home/{user}/Morpheus/'
downloadgui = 'https://raw.githubusercontent.com/s1csty9/Morpheus/main/gui.py'
saveguipath = f'{insdir}gui.py'
downloadid = 0
downloadidfile = f'{downloadid}.sh'
downloadidurl = f'https://raw.githubusercontent.com/s1csty9/Morpheus/main/install_scripts/install_{downloadid}.sh'
response = requests.get(downloadgui)
response2_idfk = requests.get(downloadidurl)
if response.status_code == 200:
    with open(saveguipath, 'wb') as file:
        file.write(response.content)

while downloadid < 4:
    if response2_idfk.status_code == 200:
      with open(downloadidfile, 'wb') as file:
         file.write(response2_idfk.content)
    downloadid = downloadid+1
