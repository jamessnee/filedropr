#!/usr/bin/env python

import os
import sys

def create_config(config_loc):
	f = open(config_loc,'w')
	dropb_loc = raw_input('Dropbox location: ')
	f.write(dropb_loc)

def open_config():
	home = os.getenv("HOME")
	config_loc = home + '/.filedropr.conf'
	if os.path.isfile(config_loc)==0:
		create_config(config_loc)
	f = open(config_loc,'r')
	dropb_loc = f.read()
	return dropb_loc	

def link_file(dropb_loc,ftodrop,cwd):
	fpath = cwd + ftodrop

	os.system('cd '+dropb_loc+'\n ln -s '+fpath+' '+ftodrop)

if __name__=='__main__':
	"""Check for a command line arg"""
	ftodrop = None
	if len(sys.argv)>1:
		ftodrop = sys.argv[1]
		print ftodrop
	else:
		print "Usage: <file_to_drop>"
		sys.exit()
	
	"""Open the config file to get the location of the dropbox folder"""
	dropb_loc = open_config()

	cwd = os.getcwd()

	"""Create a symlink"""
	link_file(dropb_loc,ftodrop,cwd)

	
