import subprocess
output = subprocess.run(["ls", "-la"], capture_output=True)
print (output)
