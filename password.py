#!/usr/bin/python
import os,crypt
password= "Mathematiques1"
encrypt= crypt.crypt(password, "vv")
user= os.system("useradd -m -p " + encrypt + "samy")
print("done")
