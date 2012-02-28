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
VERSION = ["5.2", "2011/07/25-09:09:30"]

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
def allocate_list2(list_all, cur_dir_src):
	list_all = [os.path.join(cur_dir_src, item) for item in list_all]

	#debug
	for i in list_all:
		print i
#	pass
#	list_all = [os.path.join(cur_dir_src, item) for item in list_all]
#
#	print list_all #debug
#	print inspect.currentframe().f_lineno

def allocate_list(list_all):
	list_files = list()
	list_dirs = list()

	for item in list_all:
		if os.path.isfile(item):
			list_files.append(item)
#		elif item.rsplit(".", 1)[1] in ["c", "h", "cpp"]
#			list_files.append(item)
		elif os.path.isdir(item):
			list_dirs.append(item)
		else: pass

	return list_files, list_dirs
def dir_exists(ssh, dir_path, yes_flag):
	res = is_dir(ssh, dir_path)

	# if dir exists ---------------
	if res == 1: print "Dir exists: %s" % dir_path
	# if not exist ---------------
	elif res == -1:
		print "Dir does not exist: %s" % dir_path
		# create a new dir?
		while (yes_flag == False):
#		while (True):
			ans = raw_input("Create a dir?[y/n]")
			if ans.lower() == 'n':
				print "You chose not to create a dir"
				print "Program ends. Thank you for trying"
				sys.exit(0)
#			if ans.lower() == 'n': break
			# create a dir
#			if ans.lower() == 'y':
		res_makedir = makedir(ssh, dir_path)
		if res_makedir == 1: print "Dir created: %s" % dir_path
		else: print res_makedir
	else:
		print "DEBUG:%d:" % inspect.currentframe().f_lineno,
		print "res=%s" % str(res)



	list_files = list()
	list_dirs = list()
	list_all = [os.path.join(cur_dir_src, item) for item in list_all]

	print list_all
#	print inspect.currentframe().f_lineno; sys.exit() #debug


	list_files = list()
	list_dirs = list()

	for item in list_all:
		if os.path.isfile(item): list_files.append(item)
		elif os.path.isdir(item): list_dirs.append(item)

	return list_files, list_dirs

def exec_chmod(ssh, modnum, file_path_dst, yes_flag):
	if modnum == 0 and yes_flag == False:
		ans = raw_input("Exec 'chmod'(755)?[y/n]")
		if ans.lower() == 'y':
			for item in file_path_dst:
				try:
					ssh.exec_command("chmod 755 %s" % item)
					print "'chmod'(755) done to: %s" % item
				except Exception, e: print e
		else: pass
	elif modnum == 0 and yes_flag == True:
		for item in file_path_dst:
			try:
				ssh.exec_command("chmod 755 %s" % item)
				print "'chmod'(755) done to: %s" % item
			except Exception, e: print e
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

def get_files_path_src(list_files, cur_dir):

	return [os.path.join(cur_dir,item) for item in list_files]

def get_files_path_dst(list_files, cur_dir_dst):

	return ["/".join((cur_dir_dst,item)) for item in list_files]

def get_ubuntu_path(cur_dir_src, root_dir_dst):
	elems = cur_dir_src.split("\\")
	reg = re.compile('G[0-9_]+')
	for el in elems:
		if reg.search(el):  #print el, "\t", elems.index(el)
			n = elems.index(el)
			new_path = "/".join((root_dir_dst, "/".join(elems[n:])))

	return new_path

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
		elif x == "-U": username = y
		elif x == "-F":
			if y == '*': file_path_src = get_file_list()
			else:
				files = y.split(",")
				for item in files:
					file_path_src.append(os.path.join(os.getcwd(), item))
		elif x == "-D":
			if y == '.': dir_path_dst = "/var/www/cgi-bin/%s" % \
				os.path.basename(os.getcwd())
			else: dir_path_dst = y
		elif x == "-M": modnum = int(y)
		elif x == "-P": passwd = y
		elif x == "-y": yes_flag = True
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

	return username, file_path_src, file_path_dst, modnum, passwd, yes_flag
#def handle_args(args):/

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
def upload_files(ssh, file_path_src, file_path_dst):
	try:
		sftp = ssh.open_sftp()
		print "sftp opened"
	except Exception, e:
		print e; sys.exit()

	for i in range(len(file_path_src)):
		try:
			sftp.put(file_path_src[i], file_path_dst[i])
			print "File uploaded"
			print "\t", "From: %s" % file_path_src[i]
			print "\t", "To: %s" % file_path_dst[i]
		except Exception, e: print e

#		res = is_file(ssh, file_path_dst[i])

#		if res == 1 and yes_flag == False:
#			print "File exists: %s" % file_path_dst[i]
#			while(True):
#				ans = raw_input("Overwrite a file?[y/n]")
#				if ans.lower() == 'n':
#					break_flag = True
#					break
#				else: break
#			 # Overwrite
##			if ans.lower() == 'y':
#			if break_flag == True: continue
#
#			print "Overwrite"
#			try:
#				sftp.put(file_path_src[i], file_path_dst[i])
#				print "File uploaded"
#				print "\t", "From: %s" % file_path_src[i]
#				print "\t", "To: %s" % file_path_dst[i]
#			except Exception, e: print e
#
##			if ans.lower() == 'n': print "Not overwrite"
#		# file does not exist
#		elif res == 1 and yes_flag == True:
#			print "Overwrite"
#			try:
#				sftp.put(file_path_src[i], file_path_dst[i])
#				print "File uploaded"
#				print "\t", "From: %s" % file_path_src[i]
#				print "\t", "To: %s" % file_path_dst[i]
#			except Exception, e: print e
#
#		elif res == -1:
#			try:
#				sftp.put(file_path_src[i], file_path_dst[i])
#				print "File uploaded:"
#				print "\t", "From: %s" % file_path_src[i]
#				print "\t", "To: %s" % file_path_dst[i]
#			except Exception, e: print e

def upload_file(ssh, file_path_src, file_path_dst, yes_flag):
	for i in range(len(file_path_dst)):
		break_flag = False
		try:
			sftp = ssh.open_sftp()
			print "sftp opened"
		except Exception, e: print e

		res = is_file(ssh, file_path_dst[i])

		if res == 1 and yes_flag == False:
			print "File exists: %s" % file_path_dst[i]
			while(True):
				ans = raw_input("Overwrite a file?[y/n]")
				if ans.lower() == 'n':
					break_flag = True
					break
				else: break
			 # Overwrite
#			if ans.lower() == 'y':
			if break_flag == True: continue

			print "Overwrite"
			try:
				sftp.put(file_path_src[i], file_path_dst[i])
				print "File uploaded"
				print "\t", "From: %s" % file_path_src[i]
				print "\t", "To: %s" % file_path_dst[i]
			except Exception, e: print e

#			if ans.lower() == 'n': print "Not overwrite"
		# file does not exist
		elif res == 1 and yes_flag == True:
			print "Overwrite"
			try:
				sftp.put(file_path_src[i], file_path_dst[i])
				print "File uploaded"
				print "\t", "From: %s" % file_path_src[i]
				print "\t", "To: %s" % file_path_dst[i]
			except Exception, e: print e

		elif res == -1:
			try:
				sftp.put(file_path_src[i], file_path_dst[i])
				print "File uploaded:"
				print "\t", "From: %s" % file_path_src[i]
				print "\t", "To: %s" % file_path_dst[i]
			except Exception, e: print e

def upload_files1():
		# setup variables ====================
	cur_dir_src = os.getcwd()
	root_dir_dst = "/var/www/cgi-bin/%s"
	root_dir_src = r"C:\workspaces\ws_ubuntu_1"
	cur_dir_dst = root_dir_dst % os.path.basename(cur_dir_src)

	list_all = os.listdir(cur_dir_src)

	# get ssh ================
	username = "root"; passwd = "5n6WW09Y"
	ssh = get_ssh(username, passwd)

	# allocate list ====================
	list_files, list_dirs = allocate_list(list_all)

	# create dirs in the remote ================
	res = makedir(ssh, cur_dir_dst)
	if res == 1: print "Dir created: %s" % cur_dir_dst
	else: print res

	# prepare source files path ================
	files_path_src = get_files_path_src(list_files, cur_dir_src)

	# prepare dst files path ================
	files_path_dst = get_files_path_dst(list_files, cur_dir_dst)

	# upload files ================
	upload_files(ssh, files_path_src, files_path_dst)

	# create dirs =========================
	for item in list_dirs:
		new_dir = "/".join((cur_dir_dst, item))
		try:
			res = makedir(ssh, "%s" % new_dir)
			if res == 1: print "Dir created: %s" % new_dir
			else: print res
		except Exception, e: print e

    # create dirs from list_dirs =========================
	dirs_src = [os.path.join(cur_dir_src, item) for item in list_dirs]
#	debug
	print dirs_src
	print inspect.currentframe().f_lineno
	sys.exit()

def upload_files2(cur_dir_src, root_dir_dst):

	dir_path_dst = get_ubuntu_path(cur_dir_src, root_dir_dst)

	# 01 get files and dirs lists ====================
	list_all = os.listdir(cur_dir_src)
	#debug
#	print list_all
#	print "cur_dir_src", cur_dir_src
#	print inspect.currentframe().f_lineno; sys.exit()

	allocate_list2(list_all, cur_dir_src)
#	list_files, list_dirs = allocate_list2(list_all, cur_dir_src)

	print "OK." #debug
	print inspect.currentframe().f_lineno; sys.exit()
	
	# 02 get ssh ================
	username = "root"; passwd = "5n6WW09Y"
	ssh = get_ssh(username, passwd)

	# get ubuntu path ================
#	root_dir_dst = "/var/www/cgi-bin"
	new_path = get_ubuntu_path(cur_dir_src, root_dir_dst)

	# 03 create dirs in the remote ================
	res = makedir(ssh, cur_dir_dst)
	if res == 1: print "Dir created: %s" % cur_dir_dst
	else: print res

	#debug
#	print list_all
#	print list_files, list_dirs
#	print inspect.currentframe().f_lineno; sys.exit()

def do_job():
	
	# upload_files1 =========================
#	upload_files1()
	# upload_files2 =========================
	root_dir_dst = "/var/www/cgi-bin"
	dirs_src = r"C:\workspaces\ws_ubuntu_1\G20110723_074103_upload_new_version_directory\include"
	upload_files2(dirs_src, root_dir_dst)

# execute ========================
if __name__ == '__main__':
#  print "Content-Type: text/html"
#  print ""

#	print __file__
	do_job()
#	print inspect.currentframe().f_lineno; sys.exit()