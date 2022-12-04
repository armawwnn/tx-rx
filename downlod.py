#import wget
import os
from pathlib import Path

cwd = os.getcwd()
home = Path.home()
downloadDir = str(home) + '/downloadtest'
os.mkdir(downloadDir)
cmd = "wget -P {} --limit-rate=400k https://speed.hetzner.de/10GB.bin".format(downloadDir)
rep = input("rep for hae many times? ")
rep = int(rep)
count = 0;
def colored(r, g, b, text):
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
while(count<rep):
    os.system(cmd)
    count = count +1
    listdir = os.listdir(downloadDir)
    if len(listdir) != 0 :
        for file in listdir:
            path = os.path.join(downloadDir,file)
            os.remove(path)
            coltext = colored(255,0,0,"removed")
            print(coltext + ' %s ' % file)
