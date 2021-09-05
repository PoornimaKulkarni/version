import re
import subprocess
import psutil

com = "ipconfig"
a = subprocess.Popen(com, shell=True)
b = a.wait()

mem = psutil.virtual_memory()
print(mem)

with open('text.txt','r') as file:
    file_data = file.read()

ver = re.sub("VERSION:1.1", "VERSION:1.2", file_data)

with open('text.txt','w') as file:
    file.write(ver)
