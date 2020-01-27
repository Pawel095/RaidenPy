import subprocess
import os
import shutil

path = os.getcwd()+'\\assets'
files = []
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

args = ["pyinstaller", "-F"]
args.append("main.py")
print(args)
subprocess.call(args)
try:
    os.mkdir("dist\\assets\\")
except FileExistsError as e:
    pass
    
for f in files:
    shutil.copy(f, "dist\\assets\\")
