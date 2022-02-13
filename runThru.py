#!/usr/bin/python
#Written by mcg29_ (c) 2019 

import os

def runThru(dir, list=[]):
	dirList = os.listdir(dir)
	for item in dirList:
		item = os.path.join(dir, item)
		list.append(item)
		if (os.path.isdir(item)):	
			runThru(item, list)	
	return list #Return list of all files
