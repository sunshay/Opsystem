#!/usr/bin/env python
import os
import subprocess
import sys 
import getpass

def add_user():
	     username = input("enter your username")
	     password = getpass.getpass()  

	try:
	    subprocess.run(['username', '-p', password, username ])
	except:
	    print(f"failed to add user")
add_user()
