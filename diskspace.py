#!/usr/bin/env python

import subprocess

def uname():
	    uname = "uname"
	    uname_arg = "-av"
	    subprocess.call([uname, uname_arg])

def diskspace():
	    diskspace = "df"
	    disk_spacearg = "-h"
	    subprocess.call([diskspace, disk_spacearg])
#main function

def main():
	uname()
	diskspace()
        
      main()
