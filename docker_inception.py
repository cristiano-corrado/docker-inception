#!/usr/bin/python
# Script to exececute from within docker containare to save docker-container

import subprocess
from subprocess import call
import re

repotag="kalilinux/kali-linux-docker:latest"
containerName="kali"
checkname=subprocess.Popen(["docker","ps","-f"," name="+containerName], stdout=subprocess.PIPE)
blackList=["hours","minutes","seconds","moment","ago","STATUS","CREATED","COMMAND","PORTS"]
elemdictUpper={"Image":'',"Container ID":'','Name':''}
f=checkname.stdout.read()

for b in f.split():
    if b.islower():
        if not b in blackList:
            if re.findall(r"\d+",b):
                elemdictUpper['Container ID']=b
            elif re.findall(repotag,b):
                elemdictUpper['Image']=b
            elif re.findall(containerName,b):
                elemdictUpper['Name']=b

commitChanges=subprocess.Popen(["docker","commit",elemdictUpper['Container ID'],elemdictUpper['Image']], stdout=subprocess.PIPE)

if "sha" in commitChanges.stdout.read():
    print "Commit successfull of the Image: ", elemdictUpper['Image']
else:
    print "Error"
