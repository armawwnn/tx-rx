import subprocess
import re


subprocess.run(["sudo","apt","update","-y"],check=True)
subprocess.run(["sudo","apt","upgrade","-y"],check=True)


res = subprocess.run(["sudo","apt","install","vnstat","-y"],check=True)

if res.returncode == 0:
    outputcmd = subprocess.run(["vnstat"], capture_output=True)

outputcmd = str(outputcmd)
txres = re.findall('tx:\s*(\d*\.*\d*)',outputcmd)
txiB = re.findall('tx:\s*\d*\.*\d*\s(\w\w\w)',outputcmd)
rxiB = re.findall('rx:\s*\d*\.*\d*\s(\w\w\w)',outputcmd)
rxres = re.findall('rx:\s*(\d*\.*\d*)',outputcmd)
if txiB[0] == 'TiB':
    tx = float(txres[0]) * 1000
else:
    tx = float(txres[0])
if rxiB[0] == 'TiB':
    rx = float(rxres[0]) * 1000
else:
    rx = float(rxres[0])

resault = tx/rx
if resault < 10 :
    print('start Upload')
else:
    print('vaz khobe')
