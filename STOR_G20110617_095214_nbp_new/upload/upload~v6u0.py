#!/usr/bin/python
# -*- coding: utf-8 -*-
#dir=C:\workspaces\ws_ubuntu_1/G20110622_113004/main.py
#file=v2u2
#created_at=20110622_113004

import os
import sys
import datetime
import paramiko
import getpass
import re
import getopt
import inspect

# vars and constants ========================
VERSION = ["6.0", "2011/07/25-12:28:19"]

usage = """<<Usage>>
  <Options>
    -D<path> destination path: default="/var/www/cgi-bin/Gxxxxxx_xxxxxx_ssssss"
      "." => /var/www/cgi-bin/Gxxxxxx_xxxxxx_ssssss
    -F<path> file path to upload
    -U<name> user name: default="root"
    -M<number> chmod to number: default=~
    -P<password> password: default=~
  <Example>
    1. upload.py -D. -FUTIL.py
      => upload "UTIL.py" in the current dir to
          "/var/www/cgi-bin/Gxxxxxx_xxxxxx_xxxxxx/UTIL.py"
    2. upload.py -D. -FUTIL.py,main.html
      => upload "UTIL.py" and main.html in the current dir to
          "/var/www/cgi-bin/Gxxxxxx_xxxxxx_xxxxxx/UTIL.py"
          "/var/www/cgi-bin/Gxxxxxx_xxxxxx_xxxxxx/main.html"
"""

root_dir_d = "/var/www/cgi-bin"
root_dir_s = r"C:\workspaces\ws_ubuntu_1"

# methods ========================
def upload_files(list_files_s, list_files_d):
	# get ssh ================
	username = "root"; passwd = "5n6WW09Y"
	ssh = get_ssh(username, passwd)

	# create dirs in the remote ================
	create_dirs(ssh, os.path.dirname(list_files_d[0]))

	# upload files ==============================
	try:
		sftp = ssh.open_sftp()
		print "sftp opened"
	except Exception, e:
		print e; sys.exit()

	for i in range(len(list_files_s)):
		try:
			sftp.put(list_files_s[i], list_files_d[i])
			print "File uploaded"
			print "\t", "From: %s" % list_files_s[i]
			print "\t", "To: %s" % list_files_d[i]
		except Exception, e: print e


def allocate_items(cur_dir_s, list_all):	

	path_list = [os.path.join(cur_dir_s, item) for item in list_all]

	list_files_s = list()
	list_files_slist_dirs_s = list()

	for item in path_list:
		if os.path.isfile(item): list_files_s.append(item)
		elif os.path.isdir(item): list_files_slist_dirs_s.append(item)

	return list_files_s, list_files_slist_dirs_s

def get_ubuntu_path(list_files_s):
	list_files_d = list()

	for item in list_files_s:
		elems = item.split("\\")
		reg = re.compile('G[0-9_]+')
		for el in elems:
			if reg.search(el):  #print el, "\t", elems.index(el)
				n = elems.index(el)
				list_files_d.append("/".join((root_dir_d, "/".join(elems[n:]))))

	return list_files_d

def get_ssh(username='', passwd=''):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  if username == '': username = raw_input("Username: ")
#  msg = "Password for %s: " % username
  if passwd == '':
    passwd = getpass.getpass("Password for %s: " % username)

  try:
    ssh.connect('183.181.0.54', 3843, username=username, password=passwd)
    print "ssh connected"; return ssh
  except Exception, e:
    print e; return -1

def create_dirs(ssh, file_path_d):
  stdin, stdout, stderr = ssh.exec_command("mkdir -p %s" % file_path_d)

  err = stderr.read()
  if  err == '': print "Dir created: %s" % file_path_d; return 1
  else: return "Error: " + err.strip().split(":")[-1]

def do_upload(cur_dir_s):

#	cur_dir_s = os.path.join(root_dir_s, os.path.basename(os.getcwd()))
	cur_dir_d = get_ubuntu_path([cur_dir_s])
#	cur_dir_d = "/".join((root_dir_d, os.path.basename(os.getcwd())))

	# get files list =====================
	list_all_s = os.listdir(cur_dir_s)

	# allocate items ======================
	list_files_s, list_dirs_s = allocate_items(cur_dir_s, list_all_s)

	# convert into ubuntu path ==============
	list_files_d = get_ubuntu_path(list_files_s)

	# upload files ==============
	upload_files(list_files_s, list_files_d)

	#debug
#	sys.exit()
	
#	print "<files>"
#	for i in list_files_s: print i
#	print "<dirs>"
#	for i in list_dirs_s: print i
#	print inspect.currentframe().f_lineno; sys.exit()
#	sys.exit()
#
#	upload_files(cur_dir_s, files_list_s, cur_dir_d)

# execute ========================
if __name__ == '__main__':

	cur_dir_s = os.path.join(root_dir_s, os.path.basename(os.getcwd()))
	
	do_upload(cur_dir_s)
"""
	#debug
	print inspect.currentframe().f_lineno; sys.exit()
	sys.exit()
"""