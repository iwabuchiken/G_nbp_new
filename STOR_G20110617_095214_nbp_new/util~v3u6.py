#!/usr/bin/python
# -*- coding: %s -*-
#dir=%s
#file=v1u0
#created_at=%s

"""
2011/06/17-13:08:20

add: d:versioning

"""

import sys
import os
import re
import shutil
import datetime
import inspect
import getopt
import traceback

# variables ========================
VERSION = ["3.0", "2011/07/31-13:43:16"]

USAGE = """<<Usage>>
	<Options>
	recal
		recalibrate version signiture
	-h
		show usage
	-J
		make jar file
	-L<file name>
		name of the file for logging
	-T<sentences>
		Sentences to be written into the log file
		Use quotation if space char involved
	-v<file_name(trunk)>
		versioning
	<Example>
	util.py -Lmain.py -T"Edit: func: do_job()"
"""

# methods ========================
def get_time_label3():
  t = datetime.datetime.today()
  t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
  t2 = [str(item) for item in t1]

  for i in range(len(t2)):
    if len(t2[i]) < 2: t2[i] = "0" + t2[i]

  return "/".join(t2[:3]) + " " + ":".join(t2[3:])

def get_time_label2():
  t = datetime.datetime.today()
  t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
  t2 = [str(item) for item in t1]

  for i in range(len(t2)):
    if len(t2[i]) < 2: t2[i] = "0" + t2[i]
      
  return "".join(t2[:3]) + "_" + "".join(t2[3:])

def handle_STOR_dir(dir_name):
	print "./STOR_%s" % dir_name
	if os.path.isdir("./STOR_%s" % dir_name) == False:
#		print "STOR directory does not exist"
#		while(True):
#			ans = raw_input("Create a STOR directory?[y/n]")
#			if ans.lower() == 'n': print "You chose 'n'."; sys.exit(0)
##			if ans.lower() == 'n': print "You chose not to create. Ok."; sys.exit(0)
#			else:
#				print "You chose to create a STOR directory"
#				try:
		os.mkdir("STOR_%s" % dir_name)
		print "STOR dir created"
#			except Exception, e: print e
	else: print "STOR directory exists."

def handle_version_file(dir_name, target_file, list):
	reg = re.compile("^version~%s" % target_file)

	flag = 0
	for item in list:
		if reg.search(item):  # if version file exists
			print "Version file exists: %s" % item
			flag = 1          # turn the flag to 1
			version_file = item
			break

	if flag == 0: # if the version file doesn't exist
		f = file("./STOR_%s/version~%s=1.0" % (dir_name, target_file), "w")
		version_file = "version~%s=1.0" % target_file
		print "New file created: ./STOR_%s/%s" % \
				(dir_name, version_file)
		f.close()
#	else:
#		print "version file for '%s' exists" % target_file

	return version_file

def get_version_number(version_file):
	version_num = version_file.split("=")[1]
	ver = version_num.split(".")[0]
	update = version_num.split(".")[1]

	return version_num, ver, update

def copy_files(target_file, dir_name, ver, update):
#	items = target_file.split(".")
	trunk, ext = os.path.splitext(target_file)
#	if len(items) > 1:
	if len(ext) > 0:
#		copy_name = "%s~v%su%s.%s" % (trunk, ver, update, ext)
		copy_name = "%s~v%su%s%s" % (trunk, ver, update, ext)
#			(target_file.split(".")[0], ver, update, target_file.split(".")[1])
	else:
		copy_name = "%s~v%su%s" % (target_file, ver, update)

	try:
		print "File copying..."
		
		shutil.copyfile(target_file, os.path.join("STOR_%s" % dir_name, copy_name))
		print "File copied"
		print "\t", "From: ", target_file
		print "\t", "To: ", os.path.join("STOR_%s" % dir_name, copy_name)

	except Exception, e:
		print e
		print e.args
		sys.exit(-1)

	return os.path.join("STOR_%s" % dir_name, copy_name)
#	return copy_name

def update_version_file(dir_name, version_file, ver, update):
	try:
		cur_name = "./STOR_%s/%s" % (dir_name, version_file)
		new_name = "./STOR_%s/%s" % (dir_name, version_file.split("=")[0] + "="  \
				+ ver + "." + str(int(update)+1))

		os.rename(cur_name, new_name)
		print "Version file renamed"
		print "\t", "From: %s" % cur_name
		print "\t", "To: %s" % new_name
#		print "Version file renamed to: %s" % os.path.basename(new_name)
#		print "File renamed to: %s" % version_file
#		print "Version file renamed to: %s" % os.path.basename(new_name)
	except Exception, e: print e

	return new_name

def do_job(target_file='main.py'):
	#01 setup ==========================	
	dir_name = os.path.basename(os.getcwd())

	handle_STOR_dir(dir_name)

	#02 version file exists? ==========================
	list = os.listdir("./STOR_%s" % dir_name)
	version_file = handle_version_file(dir_name, target_file, list)

	#03 get version number ==========================
	version_num, ver, update = get_version_number(version_file)
#	print version_num, ver, update

	#04 copy 'main.py' to STOR ==========================
	new_file_path = copy_files(target_file, dir_name, ver, update)

	#05 update the number of the version file ==================
	new_version_file = update_version_file(dir_name, version_file, ver, update)

	#06 log ========================================
	f = file(r"log\%s_%s.log" % (target_file.split(".")[0], target_file.split(".")[1]), "a")
	f.write("[log %s] ------------------------\n" % get_time_label3())
	f.write("<job>: Versioning\n")
	f.write("File: %s\n" % target_file)
	f.write("\tVersion file: %s\n" % version_file)
	f.write("\tNew version file: %s\n" % os.path.basename(new_version_file))
#			f.write("\t%s\n" % options['-T'])
	f.write("[/log %s] ------------------------\n\n" % get_time_label3())

	return new_file_path

def _do_recalibrate(f, fname, dir_STOR):
  res = f.readlines()
  reg1 = re.compile('^#file=v(\d+)(u|p)(\d+)')
  reg2 = re.compile('v(\d+)(u|p)(\d+).py')
  res2 = reg2.search(fname)
  counter = 0

  new_lines = list()
  for line in res:
    res1 = reg1.search(line)
    if res1:  #if "#file" detected
      ver_line = (res1.group(1), res1.group(3))
      ver_name = (res2.group(1), res2.group(3))

      if ver_line == ver_name:
        new_lines.append(line)
      else:
#        ver_info = "#file=v%su%s\n" % ver_name
        ver_info = "#file=v%su%s\n" % ver_name
        new_lines.append(ver_info)
        counter += 1
    else:
      new_lines.append(line)
    #/if
  #/for
  try:
#    f2 = file(dir_STOR + "/" + fname.split(".")[0] + "_new" + ".py", "w")
    f2 = file(dir_STOR + "/" + fname, "w")
  except Exception, e:
    print e
  try:
    f2.write("".join(new_lines))
    print "File written: %s" % fname
#    counter += 1
  except Exception, e:
    print e

  print "%d item(s) of '%s' files recalibrated" %       (counter, fname.split(".")[0].split("~")[0])


def recalibrate():
  #01 find the STOR directory
  dir_main = os.path.realpath(os.getcwd())

  items = os.listdir(dir_main)
  dir_STOR = ""
  reg1 = re.compile('^STOR')
  for item in items:
    if reg1.search(item):
      dir_STOR = item
  if dir_STOR == "":
    print "STOR directory not found"
    exit(0)

  #02 get items in STOR dir
  items2 = os.listdir(dir_STOR)

  #03 open if Python file
  reg2 = re.compile('v(\d+)(u|p)(\d+).py')
  for item in items2: # files in STOR dir
    res2 = reg2.search(item)
    if res2:  # if item is a python file
      f = file(dir_STOR + "/" + item, "r")  # open the python file
      _do_recalibrate(f, item, dir_STOR)
#      _do_versioning(f, item, dir_STOR)
    #/if
    #debug
#    break

def handle_args():
	# preliminaries ==========================
	args = sys.argv
	if len(args) < 2: print "Please input at least one argument"; sys.exit(0)

	if args[1] == 'v': 
		print "Option 'v' was deprecated. Please use '-v' option."
		sys.exit(0)

#	if args[1] == 'v':
#		if len(args) == 3: do_job(args[2])
#		else: do_job()
#	elif args[1] == "recal": recalibrate()
	if args[1] == "recal":
		recalibrate()
		sys.exit()

	#debug
#	print "[DEBUG:%d]" % inspect.currentframe().f_lineno
#	sys.exit()

	# 01 ==========================
	kw = "v:hJL:T:"
	try:
		opts, strings = getopt.getopt(args[1:], kw)
	except Exception, e:
		print "[DEBUG:%d]" % inspect.currentframe().f_lineno
		print e
		traceback.print_exc()
		sys.exit()

	# option: -v ====================
#	jar_files = list()
	do_files = list() # list of files for 'do_job()'

	#debug
#	print opts
#	print dict(opts)
#	print dict(opts).keys()
#
#	print "[DEBUG:%d]" % inspect.currentframe().f_lineno; sys.exit()

	options = dict(opts)

	for x,y in opts:
		if x == "-h": print USAGE; sys.exit()
		if x == "-v":
			if y == "" or y == ".": do_files.append("main.py")
#			if y == "" or y == ".": jar_files.append(do_job())
			elif "," in y :
				files = y.split(",")
				for i in files: do_files.append(i)
#				for i in files: jar_files.append(do_job(i))
#				for i in files: do_job(i)
			else: do_files.append(y)
#			else: jar_files.append(do_job(y))
#			else: do_job(y)
		if x == "-L" and "-T" in options.keys():
			f = file(r"log\%s_%s.log" % (options['-L'].split(".")[0], options['-L'].split(".")[1]), "a")
			f.write("[log %s] ------------------------\n" % get_time_label3())
			f.write("<job>: Logging\n")
			f.write("File: %s\n" % options['-L'])
			f.write("\t%s\n" % options['-T'])
			f.write("[/log %s] ------------------------\n\n" % get_time_label3())

	return do_files, opts

#	print jar_files

#	if "-J" in sys.argv: print "You wrote '-J' option; A jar file will be created"
#	if "-J" in [x for x,y in opts]: print "You wrote '-J' option; A jar file will be created"
#	print [x for x,y in opts]
#	print "opts=", opts

def do_jar(jar_files):
	files = " ".join(jar_files)
	name_trunk = os.path.basename(os.getcwd())
	dir_STOR = "STOR_%s" % name_trunk
	jar_file_path = "%s\\%s%s%s.jar" % (dir_STOR, name_trunk, "_", get_time_label2())
#	jar_file_path = os.path.join(
#				dir_STOR,
#				".".join(
#						"".join((name_trunk, "_", get_time_label2())),
#						"jar"))
	#debug
#	print jar_file_path
#	sys.exit()

	command = "jar cvf %s %s" % (jar_file_path, files)
#	command = "jar cvf %s %s" % (name_trunk, get_time_label2(), files)
#	command = "jar cvf %s_%s.jar %s" % (name_trunk, get_time_label2(), files)
#	print command #debug
#	sys.exit()
	try:
		os.system(command)
		print "Jar file created: %s" % jar_file_path
#		print "Jar file created: %s" % ".".join(name_trunk, "jar")
	except Exception,e :
		print e
		traceback.print_exc()
		sys.exit()

#	print "files=", files #debug
		

# execute ========================

if __name__ == '__main__':
	# 00 =============================
	if len(sys.argv) < 2: print USAGE; sys.exit(0)

	# 01 handle args ================
	do_files, opts = handle_args()
	print do_files #debug

	#debug
#	print "[DEBUG:%d]" % inspect.currentframe().f_lineno; sys.exit()
#	sys.exit()

	# 02 do job ================
	jar_files = list()
	for i in do_files:
		jar_files.append(do_job(i))

	print jar_files #debug

	# 03 jar file ================
	if "-J" in sys.argv: do_jar(jar_files)

"""
	#debug
	print "[DEBUG:%d]" % inspect.currentframe().f_lineno; sys.exit()
	sys.exit()
"""