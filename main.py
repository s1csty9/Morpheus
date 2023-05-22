import subprocess
import os
import requests
import time

user = os.getlogin()
insdir = f'/home/{user}/Morpheus/'
downloadurl = 'https://github.com/s1csty9/Morpheus/raw/main/download.py'
savescrpath = f'{insdir}download.py'

if os.path.exists(insdir)and os.path.isdir(insdir):
 response = requests.get(downloadurl)
 if response.status_code == 200:
    with open(savescrpath, 'wb') as file:
        file.write(response.content)
        while not os.path.exists(f'{insdir}download.py'):
            time.sleep(0.1)
        subprocess.run(['python3', 'download.py'], cwd=insdir)
else:
  subprocess.run(['mkdir', '-p', insdir])
