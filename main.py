import subprocess
import os

user = os.getlogin()
insdir = f'/home/{user}/Morpheus/'
if os.path.exists(insdir)and os.path.isdir(insdir):
 print('ok')
else:
  subprocess.run(['mkdir', '-p', insdir])
#insname will be set to different file names depending on user input in the future, for now ins_tor.sh is a placeholder for testing
insname='ins_tor.sh'
script_path=f'{insdir}{insname}'


subprocess.run(['bash', script_path])
