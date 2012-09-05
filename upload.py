import os.path
#!/usr/bin/python
# -*- coding: utf-8 -*-
#dir=C:\workspaces\ws_ubuntu_1/G20110622_113004/main.py
#file=7.1
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

# vars and constants ========================
VERSION = ["6.3", "2011/07/26-16:13:03"]

USAGE = """<<Usage>>
  <Options>
    -D<path> destination path: default="/var/www/cgi-bin/Gxxxxxx_xxxxxx_ssssss"
	"." => /var/www/cgi-bin/Gxxxxxx_xxxxxx_ssssss
	"h+xxx" => /var/www/html/Gxxxxxx_xxxxxx_ssssss/xxx
	"*" => /var/www/(cgi-bin|html)/<All files>
    -F<path> file path to upload
    -U<name> user name: default="root"
    -M<number> chmod to number: default=~
    -P<password> password: default=~
    html/cgi-bin which line of directory to upload
  <Example>
    1. upload.py -D. -FUTIL.py
      => upload "UTIL.py" in the current dir to
          "/var/www/cgi-bin/Gxxxxxx_xxxxxx_xxxxxx/UTIL.py"
    2. upload.py -D. -FUTIL.py,main.html
      => upload "UTIL.py" and main.html in the current dir to
          "/var/www/cgi-bin/Gxxxxxx_xxxxxx_xxxxxx/UTIL.py"
          "/var/www/cgi-bin/Gxxxxxx_xxxxxx_xxxxxx/main.html"
"""

if len(sys.argv) and "html" in sys.argv:
	root_dir_d = "/var/www/html"
else:
	root_dir_d = "/var/www/cgi-bin"
#root_dir_d = "/var/www/html"
root_dir_s = r"C:\workspaces\ws_ubuntu_1"

# methods ========================
def get_time_label2():
	t = datetime.datetime.today()
	t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
	t2 = [str(item) for item in t1]

	for i in range(len(t2)):
		if len(t2[i]) < 2: t2[i] = "0" + t2[i]

	return "".join(t2[:3]) + "_" + "".join(t2[3:])

def makedir(ssh, dir_path):
    #debug
#    print "[DEBUG:%d]" % inspect.currentframe().f_lineno
#    print "dir_path=%s" % dir_path
#    sys.exit(0)
    """
    return
    1 => dir created
    str => error  """
    stdin, stdout, stderr = ssh.exec_command("mkdir -p %s" % dir_path)
    err = stderr.read()
    if  err == '': return 1
    else: return "Error: " + err.strip().split(":")[-1]

def upload_files(list_files_s, list_files_d):

	#debug
	print "<list_files_s>"
	for i in list_files_s: print "\t", i
	print inspect.currentframe().f_lineno
#	sys.exit()

	# get ssh ================
	username = "root"; passwd = "5n6WW09Y"
	ssh = get_ssh(username, passwd)

	# create dirs in the remote ================
	if len(list_files_d) > 0:
		create_dirs(ssh, os.path.dirname(list_files_d[0]))
	else: return -1

	# upload files ==============================
	try:
		sftp = ssh.open_sftp()
		print "sftp opened"
	except Exception, e: print e; sys.exit()

	for i in range(len(list_files_s)):
		try:
			#debug
			print "\t", "list_files_s[i]=", list_files_s[i]
			print "\t", "list_files_d[i]=", list_files_d[i]

			sftp.put(list_files_s[i], list_files_d[i])
			print "File uploaded"
			print "\t", "From: %s" % list_files_s[i]
			print "\t", "To: %s" % list_files_d[i]
		except Exception, e:
			#debug
			print inspect.currentframe().f_lineno
			print e

	# fromdos =====================
#	print "fromdos %s/*" % os.path.dirname(list_files_d[0])
	stdin, stdout, stderr = ssh.exec_command(
				"fromdos %s/*" % os.path.dirname(list_files_d[0]))
	err = stderr.read()
	if  err == '': print "'fromdos' done"

	# chmod 755 =====================
	stdin, stdout, stderr = ssh.exec_command(
				"chmod 755 %s/*" % os.path.dirname(list_files_d[0]))
	err = stderr.read()
	if  err == '': print "chmod done: 755"

	#debug
#	stdin, stdout, stderr = ssh.exec_command(
#				"ls -lF %s" % os.path.dirname(list_files_d[0]))
#	err = stderr.read()
#	sout= stdout.read()
#	souts= stdout.readlines()
#	for line in souts:
#		line = line[:-1]
#		rows = line.split(" ")
##		rows[-1]
#		print rows[-1]
##	sin= stdin.read()
#	print "err=", err
#	print sout
#	print type(stdin)
#	print dir(stdin)
#	print sin


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

	#debug
#	for i in list_dirs_s: print i
#	print inspect.currentframe().f_lineno; sys.exit()
#	sys.exit()

	# convert into ubuntu path ==============
	list_files_d = get_ubuntu_path(list_files_s)

	# upload files ==============
	upload_files(list_files_s, list_files_d)

	# try other dirs ==================
	for item in list_dirs_s:
#	if len(list_dirs_s) > 0:
		do_upload(item)
#		do_upload(list_dirs_s[0])

def do_job():
	if len(sys.argv) > 1: do_upload2()
	else:
		cur_dir_s = os.path.join(root_dir_s, os.path.basename(os.getcwd()))
		do_upload(cur_dir_s)

def handle_args():
	args = sys.argv
	if len(args) < 2: print USAGE; sys.exit(0)
	# initialize the variables -----------------
	username = ""
	file_path_src = list(); file_path_dst = list()
	dir_path_dst = ""
	modnum = 0
	passwd = ''
	yes_flag = False; flag_hyb = False

	# process getopt -----------------
	kw = "hU:F:D:M:P:y"
	opts, strings = getopt.getopt(args[1:], kw)

#	if "-h" in [list(i)[0] for i in opts]:
	if "-h" in [x for x, y in opts]:
		print USAGE; print VERSION
		sys.exit(0)

	for x, y in opts:
		if x == "-U": username = y	# user name
		elif x == "-F":					# file path: source
			if y == '*':
#				file_path_src = get_file_list()
				items = [i for i in os.listdir(os.getcwd()) \
							if os.path.isfile(i)]
				file_path_src = [os.path.join(os.getcwd(), i)\
											for i in items]
				#debug
#				print "[DEBUG:%d]" % inspect.currentframe().f_lineno
#				print file_path_src
#				sys.exit(0)
			
			else:
				files = y.split(",")
				file_path_src = [os.path.join(os.getcwd(), i)\
											for i in files if os.path.isfile(i)]
				#debug
#				print "[DEBUG:%d]" % inspect.currentframe().f_lineno
#				print file_path_src
#				sys.exit(0)

#				for item in files:
#					file_path_src.append(os.path.join(os.getcwd(), item))
		elif x == "-D":
			if y == '.': dir_path_dst = "/var/www/cgi-bin/%s" % \
				os.path.basename(os.getcwd())
			elif y == 'html': dir_path_dst = "/var/www/html/%s" % \
				os.path.basename(os.getcwd())
#			elif y[:1] == 'h+':
			elif y[:2] == 'h+':
				dir_path_dst = "/var/www/html/%s/%s" % \
					(os.path.basename(os.getcwd()), y[2:])
#			elif y[:1] == 'c+':
			elif y[:2] == 'c+':
				dir_path_dst = "/var/www/cgi-bin/%s/%s" % \
					(os.path.basename(os.getcwd()), y[2:])
			elif y == 'hyb': flag_hyb = True
			else: dir_path_dst = y
		elif x == "-M": modnum = int(y)
		elif x == "-P": passwd = y
		elif x == "-y": yes_flag = True
		else: pass
	  #for/

	# set defaults -------------------------------
	if username =="": username = "root"
	# source file is 'main.py' if getopt doesn't have '-F' option
	if len(file_path_src) == 0: file_path_src.append(\
                                        os.path.join(os.getcwd(), "main.py"))
	if dir_path_dst == "":
		dir_path_dst = "/var/www/cgi-bin/%s" % \
                                    os.path.basename(os.getcwd())

	# convert: relative src file path to absolute src file path
	if len(file_path_src) == 1:			# single file, relative path
		if not ":" in file_path_src[0][:4]:
					file_path_src[0] =\
								os.path.join(os.getcwd(), file_path_src[0])

	if len(file_path_src) > 1:			# multiple files
		for i in range(len(file_path_src)): # on each file path
			# such as "main.js"
			if len(file_path_src[i]) > 2 and not ":" in file_path_src[i][:2]:
				file_path_src[i] = os.path.join(os.getcwd(), file_path_src[i])
			else: file_path_src[i] = os.path.join(os.getcwd(), file_path_src[i])

	# convert: relative dst file path to absolute dst file path
	for item in file_path_src:
		file_path_dst.append(dir_path_dst + "/" + os.path.basename(item))

	return username, file_path_src, file_path_dst, modnum, passwd, yes_flag, flag_hyb
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

  #debug
  print r"ls -l \" % file_path : ", "ls -l %s" % file_path
  print "out=", out
  print "err=", err
  print "[DEBUG:%d]" % inspect.currentframe().f_lineno#; sys.exit()

  out_list = out.split(" ")
  if out_list[0][0] == '-': return 1
  if out_list[0][0] == 'd': return 2

  return -2

def upload_file(ssh, file_path_src, file_path_dst, yes_flag):
	for i in range(len(file_path_dst)):
		break_flag = False
		try:
			sftp = ssh.open_sftp()
			print "sftp opened"
		except Exception, e: print e

		res = is_file(ssh, file_path_dst[i])

		#debug
		print "[DEBUG:%d]" % inspect.currentframe().f_lineno
		print "res=", res

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
				print "New file: %s" % file_path_src[i]
				sftp.put(file_path_src[i], file_path_dst[i])
				print "File uploaded:"
				print "\t", "From: %s" % file_path_src[i]
				print "\t", "To: %s" % file_path_dst[i]
			except Exception, e: print e
def exec_fromdos(ssh, file_path_dst):
	for item in file_path_dst:
		try:
			ssh.exec_command("fromdos %s" % item)
			print "'fromdos' done to: %s" % item
		except Exception, e: print e

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

def _get_file_path_src_html(dir_path_src):
	file_path_src_html = list()
	file_path_src_html.append(os.path.join(dir_path_src, "main.html"))
	file_path_src_html.append(os.path.join(dir_path_src, "main.js"))

	return file_path_src_html
#	pass

def _get_file_path_dst_html(file_path_src_html):
	file_path_dst_html = list()
	for item in file_path_src_html:
		_list = item.split(os.sep)
		file_path_dst_html.append("/".join(("/var/www/html", _list[-2], _list[-1])))
#		file_path_dst_html.append("/".join(("/var/www/cgi-bin", _list[-2], _list[-1])))

	return file_path_dst_html

def _get_file_path_dst_cgi(file_path_src_cgi):
	file_path_dst_cgi = list()
	for item in file_path_src_cgi:
		_list = item.split(os.sep)
		file_path_dst_cgi.append("/".join(("/var/www/cgi-bin", _list[-2], _list[-1])))
#		file_path_dst_html.append("/".join(("/var/www/cgi-bin", _list[-2], _list[-1])))

	return file_path_dst_cgi

def get_file_list(dir=os.getcwd()):
	items = os.listdir(dir)
	file_list = list()
	for item in items:
		if os.path.isfile(item): file_list.append(item)

	return file_list

def _get_file_path_src_cgi(dir_path_src):
	file_path_src_cgi = list()
	file_path_src_cgi.append(os.path.join(dir_path_src, "main.py"))
	
	return file_path_src_cgi
#	pass

def do_upload_hyb():
	# handle args --------------------------------
	username, file_path_src, file_path_dst, \
	modnum, passwd, yes_flag, flag_hyb\
			= handle_args()
	# create an ssh instance ----------------------------
	ssh = get_ssh(username, passwd)

	# create dirs -----------------------------------
	_list = file_path_dst[0].split("/")
	_list[3] = "html"
	_list_new = "/".join(_list)

	res = makedir(ssh, os.path.dirname(_list_new))

	if res == 1: print "Dir created: %s" % os.path.dirname(_list_new)

	_list[3] = "cgi-bin"
	_list = "/".join(_list)

	res = makedir(ssh, os.path.dirname(_list))
	if res == 1: print "Dir created: %s" % os.path.dirname(_list)

		# html files
	file_path_src_html = _get_file_path_src_html(os.path.dirname(file_path_src[0]))
	file_path_dst_html = _get_file_path_dst_html(file_path_src_html)

		# cgi files

	file_path_src_cgi = _get_file_path_src_cgi(os.path.dirname(file_path_src[0]))
	file_path_dst_cgi = _get_file_path_dst_cgi(file_path_src_cgi)

		#debug
#	print file_path_src_cgi
#	print file_path_dst_cgi
#	print "[DEBUG:%d]" % inspect.currentframe().f_lineno; sys.exit()
#	sys.exit()

	# upload files -----------------------------------
	upload_file(ssh, file_path_src_html, file_path_dst_html, yes_flag)
	upload_file(ssh, file_path_src_cgi, file_path_dst_cgi, yes_flag)
#	upload_file(ssh, file_path_src, file_path_dst, yes_flag)

	# exec fromdos --------------------------------
	exec_fromdos(ssh, file_path_dst_html)
	exec_fromdos(ssh, file_path_dst_cgi)

	# exec chmod --------------------------------
	exec_chmod(ssh, modnum, file_path_dst_html, yes_flag)
	exec_chmod(ssh, modnum, file_path_dst_cgi, yes_flag)
	#

#	print "HYB"

def do_upload2():
	url_trunk = "http://183.181.0.54"
	username, file_path_src, file_path_dst, \
	modnum, passwd, yes_flag, flag_hyb\
			= handle_args()

	#debug
#	print "[DEBUG:%d]" % inspect.currentframe().f_lineno
#	print "os.path.dirname(file_path_dst[0])=",\
#					os.path.dirname(file_path_dst[0])
#	sys.exit(0)

	# create an ssh instance ----------------------------
	ssh = get_ssh(username, passwd)

	# create dirs -----------------------------------
	res = makedir(ssh, os.path.dirname(file_path_dst[0]))
	if res == 1: print "Dir created: %s" % os.path.dirname(file_path_dst[0])

	# upload files -----------------------------------
	upload_file(ssh, file_path_src, file_path_dst, yes_flag)

	# exec fromdos --------------------------------
	exec_fromdos(ssh, file_path_dst)

	# exec chmod --------------------------------
	exec_chmod(ssh, modnum, file_path_dst, yes_flag)

	# closing message --------------------------------
	print "[DEBUG:%d]" % inspect.currentframe().f_lineno
	print "All the work done. \
		Thank you for working with me. See you again"

	#debug
#	print "file_path_dst[0].split("/")=", file_path_dst[0].split("/")
#	print "Access: %/%s" % \
	print "Access: %s/%s" % \
				(url_trunk, "/".join(file_path_dst[0].split("/")[4:-1]))
#					(url_trunk, file_path_dst[0].split("/")[-2])
#					(url_trunk, file_path_dst[0].split('\/')[-2])
#					(url_trunk, file_path_dst[0].split('/')[-2])
	print get_time_label2()
	sys.exit(0)

# execute ========================
if __name__ == '__main__':
	
	if "-Dhyb" in sys.argv: do_upload_hyb()
	elif len(sys.argv) > 1: do_upload2()
	else:
		cur_dir_s = os.path.join(root_dir_s, os.path.basename(os.getcwd()))
		do_upload(cur_dir_s)

"""
#debug
print "[DEBUG:%d]" % inspect.currentframe().f_lineno
sys.exit()
"""