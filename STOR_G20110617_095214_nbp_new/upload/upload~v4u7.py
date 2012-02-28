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

"""
Variables
  VERSION usage
  get_time_label2(): t, t1, t2, i
  get_ssh(): ssh, username, passwd, e
  get_file_list(): items, file_list, item
  handle_args(): username, file_path_src, dir_path_dst,
              file_path_dst, item, args, item
  is_dir(): ssh, dir_path, stdin, stdout, stderr, err,
          res, item, columns
  is_file(): ssh, file_path, stdin, stdout, stderr, err,
          out, out_list
  makedir(): ssh, dir_path, stdin, stdout, stderr, err
"""

# vars and constants ========================
VERSION = [4.7, "2011/07/14-06:40:38"]

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
	if len(args) < 2: print usage; sys.exit(0)
	# initiate the variables
	username = ""
	file_path_src = list()
	file_path_dst = list()
	dir_path_dst = ""
	modnum = 0
	passwd = ''
	yes_flag = False

	kw = "hU:F:D:M:P:y"
	opts, strings = getopt.getopt(args[1:], kw)

	if "-h" in [list(i)[0] for i in opts]:
		print usage
		print VERSION
		sys.exit(0)

  #debug
#  print opts

	for x, y in opts:
		if x == "-h": print VERSION#; sys.exit(0)
		if x == "-U": username = y
		if x == "-F":
			if y == '*': file_path_src = get_file_list()
			else:
				files = y.split(",")
				for item in files:
					file_path_src.append(os.path.join(os.getcwd(), item))
		if x == "-D":
			if y == '.': dir_path_dst = "/var/www/cgi-bin/%s" % \
				os.path.basename(os.getcwd())
			else: dir_path_dst = y
		if x == "-M": modnum = int(y)
		if x == "-P": passwd = y
		else: pass
	  #for/

	# set defaults
	if username =="": username = "root"
	if len(file_path_src) == 0: file_path_src.append(\
                                        os.path.join(os.getcwd(), "main.py"))
	if dir_path_dst == "":
		dir_path_dst = "/var/www/cgi-bin/%s" % \
                                    os.path.basename(os.getcwd())

	# single file
	if len(file_path_src) == 1:
		if not ":" in file_path_src[0][:4]: file_path_src[0] = os.path.join(os.getcwd(), file_path_src[0])
	# multiple files
	if len(file_path_src) > 1:
		for i in range(len(file_path_src)): # on each file path
			# such as "main.js"
			if len(file_path_src[i]) > 2 and not ":" in file_path_src[i][:2]:
				file_path_src[i] = os.path.join(os.getcwd(), file_path_src[i])
			else: file_path_src[i] = os.path.join(os.getcwd(), file_path_src[i])

	for item in file_path_src:
		file_path_dst.append(dir_path_dst + "/" + os.path.basename(item))

	return username, file_path_src, file_path_dst, modnum, passwd
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

def dir_exists(ssh, dir_path):
	res = is_dir(ssh, dir_path)

	# if dir exists ---------------
	if res == 1: print "Dir exists: %s" % dir_path
	# if not exist ---------------
	elif res == -1:
		print "Dir does not exist: %s" % dir_path
		# create a new dir?
		while (True):
			ans = raw_input("Create a dir?[y/n]")
			if ans.lower() == 'n': break
			# create a dir
			if ans.lower() == 'y':
				res_makedir = makedir(ssh, dir_path)
				if res_makedir == 1: print "Dir created: %s" % dir_path
				else: print res_makedir
				break
	else: print res

def upload_file(ssh, file_path_src, file_path_dst):
	for i in range(len(file_path_dst)):
		try:
			sftp = ssh.open_sftp()
			print "sftp opened"
		except Exception, e: print e

		res = is_file(ssh, file_path_dst[i])

		if res == 1:
			print "File exists: %s" % file_path_dst[i]
			ans = raw_input("Overwrite a file?[y/n]")
			 # Overwrite
			if ans.lower() == 'y':
				print "Overwrite"
				try:
					sftp.put(file_path_src[i], file_path_dst[i])
					print "File uploaded"
					print "\t", "From: %s" % file_path_src[i]
					print "\t", "To: %s" % file_path_dst[i]
				except Exception, e: print e

			if ans.lower() == 'n': print "Not overwrite"
		# file does not exist
		if res == -1:
			try:
				sftp.put(file_path_src[i], file_path_dst[i])
				print "File uploaded:"
				print "\t", "From: %s" % file_path_src[i]
				print "\t", "To: %s" % file_path_dst[i]
			except Exception, e: print e

def exec_chmod(ssh, modnum, file_path_dst):
	if modnum == 0:
		ans = raw_input("Exec 'chmod'(755)?[y/n]")
		if ans.lower() == 'y':
			for item in file_path_dst:
				try:
					ssh.exec_command("chmod 755 %s" % item)
					print "'chmod'(755) done to: %s" % item
				except Exception, e: print e
		else: pass
	else: # modnum != 0
		for item in file_path_dst:
			try:
				ssh.exec_command("chmod %d %s" % (modnum, item))
				print "'chmod'(%d) done to: %s" % (modnum, item)
			except Exception, e: print e

def exec_fromdos(ssh, file_path_dst):
	for item in file_path_dst:
		try:
			ssh.exec_command("fromdos %s" % item)
			print "'fromdos' done to: %s" % item
		except Exception, e: print e

def do_job(): 
	# setup variables
	username, file_path_src, file_path_dst, modnum, passwd = handle_args()

#	debug
#	print username, file_path_src,
#	print "file_path_dst=", file_path_dst, modnum, passwd
#	print inspect.currentframe().f_lineno
#	sys.exit()

	#debug
	print "username=%s" % username
  
	# create an ssh instance ----------------------------
	ssh = get_ssh(username, passwd)

	# Dir exists? --------------------------------------
	#debug
#	print "file_path_dst[0]=", file_path_dst[0]
#	print "os.path.dirname(file_path_dst[0])=", os.path.dirname(file_path_dst[0])
#	print inspect.currentframe().f_lineno
#	sys.exit()

	dir_exists(ssh, os.path.dirname(file_path_dst[0]))

	# upload files -----------------------------------
	upload_file(ssh, file_path_src, file_path_dst)

	# exec fromdos --------------------------------
	exec_fromdos(ssh, file_path_dst)

	# exec chmod --------------------------------
	exec_chmod(ssh, modnum, file_path_dst)

	# closing message --------------------------------
	print "All the work done. Thank you for working with me. See you again"
	sys.exit(0)
    
# execute ========================
if __name__ == '__main__':
  print "Content-Type: text/html"
  print ""

  do_job()
