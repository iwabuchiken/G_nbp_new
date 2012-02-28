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
import traceback

"""
Variables

"""

# vars and constants ========================
VERSION = ["1.2", "2011/07/15-05:58:11"]

usage = """<<Usage>>
  <Options>
    -D<path> directory path to which download the file
	   default=os.getcwd()
	   "." => os.getcwd()
    -F<path> file path from which to download
        :default => /var/www/cgi-bin/Gxxx/main.py
    -U<name> user name: default => "root"
    -P<password> password: default => ~
  <Example>
    1. download.py -D. -FUTIL.py
      => download "UTIL.py" to the current dir from
          "/var/www/cgi-bin/Gxxxxxx_xxxxxx_xxxxxx/UTIL.py"    
"""
# methods ========================
def get_time_label2():
  t = datetime.datetime.today()
  t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
  t2 = [str(item) for item in t1]

  for i in range(len(t2)):
    if len(t2[i]) < 2: t2[i] = "0" + t2[i]

  return "".join(t2[:3]) + "_" + "".join(t2[3:])

def get_ssh(username='', passwd=''):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  if username == '': username = raw_input("Username: ")
#  msg = "Password for %s: " % username
  if passwd == '':
    passwd = getpass.getpass("Password for %s: " % username)

  try:
    ssh.connect('183.181.0.54', 3843, username=username, password=passwd)
    print "ssh connected"
    return ssh
  except Exception, e:
    print e
    return -1

def makedir(ssh, dir_path):
  """
  return
  1 => dir created
  str => error  """
  stdin, stdout, stderr = ssh.exec_command("mkdir -p %s" % dir_path)

  err = stderr.read()
  if  err == '': return 1
  else: return "Error: " + err.strip().split(":")[-1]

#def is_dir(ssh, dir_path, name):
def is_dir(ssh, dir_path):
  """
  1 => dir exists
  -1 => dir does not exist
  str => error
  """
  stdin, stdout, stderr = ssh.exec_command("ls -l %s" % os.path.dirname(dir_path))
  err = stderr.read()
  if not err == '': return err.strip().split(":")[-1]

  res = stdout.readlines()
  for item in res:
#    print item
    columns = item.strip().split(" ")
#    print columns
    if os.path.basename(dir_path) in columns and columns[0][0] == 'd': return 1

  return -1

def get_file_list(dir=os.getcwd()):
  items = os.listdir(dir)
  file_list = list()
  for item in items:
    if os.path.isfile(item): file_list.append(item)

  return file_list

def handle_args():
	args = sys.argv
	if len(args) < 2: print usage; sys.exit()
	# initiate the variables
	username = ""
	passwd = ''
	f_path_src = ""
	f_path_dst = ""
	dir_path_dst = ""

	kw = "hU:F:D:P:"
	opts, strings = getopt.getopt(args[1:], kw)
  
	for x, y in opts:
		if x == "-h":
			print os.path.realpath(__file__)
			print VERSION
			print usage
			sys.exit(0)
		elif x == "-U": username = y
#		elif x == "-F": f_path_src.append(y)
		elif x == "-F": f_path_src = y
		elif x == "-D": #f_path_dst = y
			if y == '.':
				f_path_dst = os.getcwd()
			else: f_path_dst = y
		elif x == "-P": passwd = y
		else: pass
  #for/

	# set defaults
	if username =="": username = "root"
	if f_path_src =="":
		print "File to download not designated"
		sys.exit()
	f_path_dst = os.path.join(f_path_dst, os.path.basename(f_path_src))

	return username, f_path_src, f_path_dst, passwd
#def handle_args(args):/

def is_file(ssh, file_path):
  """
  return
  1 => file exists
  2 => dir exists
  -1 => no such file
  -2 => error
  """
  stdin, stdout, stderr = ssh.exec_command("ls -l %s" % file_path)
  err = stderr.read()
#  if not err == '': return err.strip().split(":")[-1]
  if "No such file or directory" in err: return -1

  out = stdout.read()
  out_list = out.split(" ")
  if out_list[0][0] == '-': return 1
  if out_list[0][0] == 'd': return 2

  return -2

def get_sftp(ssh):
	try:
		 sftp = ssh.open_sftp()
		 print "sftp opened"
		 return sftp
	except Exception, e: print e; sys.exit()

def download_file(sftp, f_path_src, f_path_dst):
	print "File downloading:"
	print "\t", "From: %s" % f_path_src
	print "\t", "To: %s" % f_path_dst

	try:
		sftp.get(f_path_src, f_path_dst)
	except Exception,e:
		traceback.print_exc(); sys.exit()

	print "File downloaded:"
	print "\t", "From: %s" % f_path_src
	print "\t", "To: %s" % f_path_dst

def do_job(): 
  # setup variables
  username, f_path_src, f_path_dst, passwd = handle_args()

  #debug
  print "username=%s" % username
  
  # create an ssh instance ----------------------------
  ssh = get_ssh(username, passwd)

  # Dir exists? --------------------------------------

  # get sftp -----------------------------------
  sftp = get_sftp(ssh)
  # download file -----------------------------------
  download_file(sftp, f_path_src, f_path_dst)

  # closing message -----------------------------------
  print "All the work complete. Thank you for your participation"
  print "See you again."

# execute ========================
if __name__ == '__main__':
#  print "Content-Type: text/html"
#  print ""

  do_job()
