#!/usr/bin/python
# -*- coding: utf-8 -*-
#dir=C:/workspaces/ws_ubuntu_1/G20110617_095214_nbp_new/nbp.py
#file=v2u2
"""
2011/06/17-10:42:39
'nbp_new' command

Variables
  usage t t1  t2  i kw  opts  strings
  x y admin ans VERSION directory time_label
  command1  command2  args dir_src:os.path.dirname(__file__)
  f_src f_dst _dir  command1_path command2_path

"""

import sys
import os
import datetime
import re
import shutil
import getopt
import inspect
import traceback

VERSION = ["4.19", "2011/07/27-07:12:59"]
"""
edit: create_cpp_files(directory, dir_src, time_label)
"""

"""
main.js: create a file by 'read()' style; introduce version
  and 'created_at' lines
"""

usage = """Usage: options
  -A<options>  administer
    p: file path
    v: file version
    <EXAMPLE>: python nbp.py -Avp
  -D<directory>  Create a project dir at the directory
  -h  help
  -P<type> project type
	=> cpp: c, C, cpp
	=> Python: P, p, python, Python
  -S<string>  Add a string to the tail of the time label

<<configure.py>>

"""

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


def handle_args(args):
  # set time label
  kw = "S:A:hD:P:p:y"
  opts, strings = getopt.getopt(args[1:], kw)

  time_label = ""; directory = ""; proj = ""; yes_flag = False
  
  for x, y in opts:
	if x == '-h': print usage; sys.exit()
	elif x == '-A':
		admin = y
		if 'p' in admin: print "\t", "path=%s" % \
			os.path.dirname(os.path.realpath(__file__))
		if 'v' in admin: print "\t", "version=%s" % VERSION
		ans = raw_input("Continue creating a project directory?[y/n]")
		if not ans.lower() == 'y': sys.exit(0)
	elif x == '-S': time_label = get_time_label2() + "_" + y
	elif x == '-D': directory = y
	elif x == '-P' or x == '-p':
		if y in ["P", "p",  "Py", "python", "Python"]:
			proj = "python"
		elif y in ["cpp", "c", "C"]:
			proj = "cpp"
		elif y in ["java", "j", "J"]:
			proj = "java"
		else:
			print "Project type not specified: Set to default => Python"
			proj = "python"
	elif x == '-y': yes_flag = True
    
  if time_label == "": time_label = get_time_label2()

  if directory == "" or directory == "$":
      directory = os.path.join("C:", os.sep,"workspaces", "ws_ubuntu_1")
  elif directory[0] == "." and not len(directory) == 1:
      directory = re.sub(".", os.getcwd(), directory, 1)
  elif directory == ".": directory = os.getcwd()

  if proj == "": proj = "python"

  print "directory=%s" % directory #debug
  print "time_label=%s" % "_".join(time_label.split("_")[:2]) #debug
  print "Project type: %s" % proj

  return directory, time_label, proj, yes_flag

def _create_main_js(dir_src, directory, time_label, group_dir):
	      # main.js
      f_src = "%s%s%s%smain.js" % (dir_src, os.sep, group_dir, os.sep)
      f_dst = "%s" % \
              os.path.join(directory, "G" + time_label, os.path.basename(f_src))
      try:
        f = file(f_src, "r")
        content = f.read()
        for item in ['//version', '//created_at', '//project']:
            if item == '//version': content = content.replace(item, "//v=1.0")
            elif item == '//created_at':
                content = content.replace(item, "//created at: %s" % \
                                          "_".join(time_label.split("_")[:2]))
            elif item == '//project': content = content.replace(item, "//project: %s" % os.path.dirname(f_dst))
      except Exception, e: print e

      try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
      except Exception, e: print e

def _create_main_py(dir_src, directory, time_label, group_dir):
	      # open the main.py
	_dir = os.path.join(directory, "G" + time_label, "main.py")
	#      _dir = "%s/G%s/main.py" % (directory, "G" + time_label, "main.py")
#	f_src = file("%s/main.py" % dir_src, "r").read() % \

	#bug-fix
#	f_src = file("%s/%s/main.py" % (dir_src, group_dir), "r").read()
#	print ('utf-8', _dir, "_".join(time_label.split("_")[:2]), \
#                      get_time_label3())

	f_src = file("%s/%s/main.py" % (dir_src, group_dir), "r").read() % \
            ('utf-8', _dir, "_".join(time_label.split("_")[:2]), \
                      get_time_label3())
#                      get_time_label3(),\
#				  123)
#            ('utf-8', _dir, time_label, get_time_label3())
	print "[DEBUG:%d]" % inspect.currentframe().f_lineno; sys.exit()

	try:
          f_dst = file(_dir, "w")
          f_dst.write(f_src)
          f_dst.close()
          print "File written: %s" % _dir
	except Exception, e: print e

def _create_lib_py(dir_src, directory, time_label, group_dir):
	      # open the main.py
	fname = "lib.py"
	_dir = os.path.join(directory, "G" + time_label, fname)
	#      _dir = "%s/G%s/main.py" % (directory, "G" + time_label, "main.py")
#	f_src = file("%s/main.py" % dir_src, "r").read() % \
	f_src = file("%s%s%s%s%s" % (dir_src, os.sep, group_dir, os.sep, fname), "r").read()

	# replace ====================
	content = """#!/usr/bin/python
# -*- coding: %s -*-
#dir=%s
#created_at=%s""" % ("utf-8", _dir, time_label)
	content2 = """
VERSION = ["1.0", "%s"]""" % "_".join(time_label.split("_")[:2])

	f_src = f_src.replace("#file_info", content)
	f_src = f_src.replace("VERSION = []", content2)

	try:
          f_dst = file(_dir, "w")
          f_dst.write(f_src)
          f_dst.close()
          print "File written: %s" % _dir
	except Exception, e: print e

def _create_main_html(directory, dir_src, time_label, group_dir):
	f_src = "%s%s%s%smain.html" % (dir_src, os.sep, group_dir, os.sep)
	f_dst = "%s" % \
              os.path.join(directory, "G" + time_label, os.path.basename(f_src))

	try:
		f = file(f_src, "r")
		content = f.read()

		content = content.replace("<!--file info-->", \
                            "<!-- v=1.0 create_at=%s project=%s -->" % \
                              ("_".join(time_label.split("_")[:2]), \
                                  os.path.dirname(f_dst)))
	except Exception, e: print e

	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e



def _create_do_cgi(directory, dir_src, time_label, group_dir, fname):
#	fname = "%s" % f_name
#	fname = "main.cpp"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	f_dst = "%s" % os.path.join(
			directory, \
			"G" + time_label, \
			os.path.basename(f_src))

	try:
		f = file(f_src, "r")
		content = f.read()

		content = content.replace("//path", \
					"/".join(("/var/www/cgi",
							os.path.basename(os.path.dirname(f_dst)))))#,
#							os.path.splitext(os.path.basename(f_dst))[0] + ".exe"))))
#					"/".join(
#					"/var/www/cgi",
#					os.path.dirname(f_dst),
#					os.path.splitext(os.path.basename(f_dst))[0] + ".exe"))
#                              (time_label, os.path.dirname(f_dst)))
		content = content.replace("{{time}}", get_time_label3(), 2)
	except Exception, e: print e

	# write a file
	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e

def _create_lib_c(directory, dir_src, time_label, group_dir):
#	fname = "%s" % f_name
	fname = "lib.c"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	f_dst = "%s" % os.path.join(
			directory, \
			"G" + time_label, \
			os.path.basename(f_src))

	try:
		f = file(f_src, "r")
		content = f.read()

		content = content.replace("//file_info", \
                            "//v=1.0\n//created_at=%s\n//project=%s" % \
                              ("_".join(time_label.split("_")[:2]), \
                                  os.path.dirname(f_dst) + os.sep + os.path.basename(f_dst)))
#                              (time_label, os.path.dirname(f_dst)))
#		content = content.replace("//define", \
#					"#define CREATED_AT \"%s\"\n#define MODIFIED_AT \"%s\"\n#define FILE_VERSION \"1.0\""\
#					% ("_".join(time_label.split("_")[:2]), "_".join(time_label.split("_")[:2])))
#define FILE_VERSION "1.1"")
	except Exception, e: print e

	# write a file
	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e

def _create_commands_txt(directory, dir_src, time_label, group_dir):
#	fname = "%s" % f_name
	fname = "commands.txt"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	f_dst = "%s" % os.path.join(
			directory, \
			"G" + time_label, \
			os.path.basename(f_src))

	try:
		f = file(f_src, "r")
		content = f.read()

		content = content.replace(
							"@path@", \
							os.path.dirname(f_dst),\
							2)

#		content = content.replace(
#							"@path1@", \
#							os.path.dirname(f_dst),\
#							2)
#
#		content = content.replace(
#							"@path2@", \
#							os.path.basename(os.path.dirname(f_dst)),\
#							2)
	except Exception, e: print e

	# write a file
	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e

def _create_main_c(directory, dir_src, time_label, group_dir):
#	fname = "%s" % f_name
	fname = "main.c"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	f_dst = "%s" % os.path.join(
			directory, \
			"G" + time_label, \
			os.path.basename(f_src))

	try:
		f = file(f_src, "r")
		content = f.read()

		content = content.replace("//file_info", \
                            "//v=1.0\n//created_at=%s\n//project=%s" % \
                              ("_".join(time_label.split("_")[:2]), \
                                  os.path.dirname(f_dst) + os.sep + os.path.basename(f_dst)))
#                              (time_label, os.path.dirname(f_dst)))
#		content = content.replace("//define", \
#					"#define CREATED_AT \"%s\"\n#define MODIFIED_AT \"%s\"\n#define FILE_VERSION \"1.0\""\
#					% ("_".join(time_label.split("_")[:2]), "_".join(time_label.split("_")[:2])))
#define FILE_VERSION "1.1"")
	except Exception, e: print e

	# write a file
	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e

def _create_main_cpp(directory, dir_src, time_label, group_dir):
	fname = "main.cpp"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	f_dst = "%s" % os.path.join(
			directory, \
			"G" + time_label, \
			os.path.basename(f_src))

	try:
		f = file(f_src, "r")
		content = f.read()

		content = content.replace("//file_info", \
                            "//v=1.0\n//created_at=%s\n//project=%s" % \
                              ("_".join(time_label.split("_")[:2]), \
                                  os.path.dirname(f_dst) + os.sep + os.path.basename(f_dst)))
#                              (time_label, os.path.dirname(f_dst)))
		content = content.replace("{{time}}", get_time_label3(), 2)
	except Exception, e: print e
	
	# write a file
	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e

def _create_makefile(directory, dir_src, time_label, group_dir):
	fname = "Makefile"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	f_dst = "%s" % os.path.join(
			directory, \
			"G" + time_label, \
			os.path.basename(f_src))
	file_info = "#v=1.0\n#created_at=%s\n#modified_at=%s\n#project=%s" %\
			("_".join(time_label.split("_")[:2]), \
			 "_".join(time_label.split("_")[:2]), \
			    os.path.dirname(f_dst) + os.sep + os.path.basename(f_dst))

	try:
		f = file(f_src, "r")
		content = f.read()

		content = content.replace("#file_info", file_info)
	except Exception, e: print e

	# write a file
	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e

def _create_main_h(directory, dir_src, time_label, group_dir):
	fname = "main.h"
	fname2 = "main_c.h"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)
	f_src2 = "%s" % os.path.join(dir_src, group_dir, fname2)

	inc_dir = os.path.join(directory, "G" + time_label, "include")
	os.mkdir(inc_dir)

	f_dst = "%s" % os.path.join(
			inc_dir,
			os.path.basename(f_src))
	f_dst2 = "%s" % os.path.join(
			inc_dir,
			os.path.basename(f_src2))
	file_info = "//v=1.0\n//created_at=%s\n//modified_at=%s\n//project=%s" %\
			("_".join(time_label.split("_")[:2]), \
			 "_".join(time_label.split("_")[:2]), \
			    os.path.dirname(f_dst) + os.sep + os.path.basename(f_dst))

	try:
		f = file(f_src, "r")
		content = f.read()

		content = content.replace("//file_info", file_info)
	except Exception, e: print e

	# write a file
	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e

	try:
		f = file(f_src2, "r")
		content = f.read()

		content = content.replace("//file_info", file_info)
	except Exception, e: print e

	# write a file
	try:
          f = file(f_dst2, "w")
          f.write(content)
          print "New file created: %s" % f_dst2
	except Exception, e: print e

#def

def _create_lib_cpp(directory, dir_src, time_label, group_dir):
	fname = "lib.cpp"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	f_dst = "%s" % os.path.join(
			directory, \
			"G" + time_label, \
			os.path.basename(f_src))
	file_info = "//v=1.0\n//created_at=%s\n//modified_at=%s\n//project=%s" %\
			("_".join(time_label.split("_")[:2]), \
			 "_".join(time_label.split("_")[:2]), \
			    os.path.dirname(f_dst) + os.sep + os.path.basename(f_dst))

	try:
		f = file(f_src, "r")
		content = f.read()

		content = content.replace("//file_info", file_info)
	except Exception, e: print e

	# write a file
	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e


def _create_main_java(directory, dir_src, time_label, group_dir):
	fname = "Main.java"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	f_dst = "%s" % os.path.join(
			directory, \
			"G" + time_label, \
			os.path.basename(f_src))

	try:
		f = file(f_src, "r")
		content = f.read()

		content = content.replace("//file_info", \
                            "//v=1.0\n//created_at=%s\n//project=%s" % \
                              ("_".join(time_label.split("_")[:2]), \
                                  os.path.dirname(f_dst) + os.sep + os.path.basename(f_dst)))
#                              (time_label, os.path.dirname(f_dst)))
#		content = content.replace("{{time}}", get_time_label3(), 2)
	except Exception, e: print e

	# write a file
	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e

# PUBLIC ============================================


def _create_file(directory, dir_src, time_label, group_dir, fname):
#	fname = "%s" % f_name
#	fname = "main.cpp"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	f_dst = "%s" % os.path.join(
			directory, \
			"G" + time_label, \
			os.path.basename(f_src))

	try:
		f = file(f_src, "r")
		content = f.read()

#		content = content.replace("//file_info", \
#                            "//v=1.0\n//created_at=%s\n//project=%s" % \
#                              ("_".join(time_label.split("_")[:2]), \
#                                  os.path.dirname(f_dst) + os.sep + os.path.basename(f_dst)))

	except Exception, e: print e

	# write a file
	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e

def create_dirs(directory, time_label, yes_flag):
	print "directory=", directory
	command1 = "md %s" % os.path.join(directory, "G" + time_label)
	command2 = "md %s" % os.path.join(directory, "G" + time_label, "STOR_G" + time_label)

	print "Command line will be: "
	print "\t", "%s" % command1
	print "\t", "%s" % command2

	while (yes_flag == False):
#	while (True):
		ans = raw_input("Execute the command? [y/n]")
		# if yes, execute
		if ans.lower() == 'n':
			print "You choose not to execute. Ok."
			exit(0)
		else: break
	try:
		os.system(command1)
		print "Directory created: %s" % os.path.join(directory, "G" + time_label)
	except Exception, e: print e

	try:
		os.system(command2)
		print "Directory created: %s" % \
			    os.path.join(directory, "G" + time_label, "STOR_G" + time_label)
	except Exception, e: print e

def create_python_files(dir_src, directory, time_label):
	group_dir = "python"
	# main.py
	_create_main_py(dir_src, directory, time_label, group_dir)

	# main.html
	_create_main_html(directory, dir_src, time_label, group_dir)
	# main.js
	_create_main_js(dir_src, directory, time_label, group_dir)
	# lib.py
	_create_lib_py(dir_src, directory, time_label, group_dir)

	# create commands.txt
	_create_commands_txt(directory, dir_src, time_label, group_dir)

def check_isdir(target_dir):
	if not os.path.isdir(target_dir):
		try:
			os.mkdir(target_dir)
			print "Directory created: %s" % target_dir
		except Exception, e: print e

def check_isdir(target_dir):
	if not os.path.isdir(target_dir):
		try:
			os.mkdir(target_dir)
			print "Directory created: %s" % target_dir
		except Exception, e: print e


def create_java_files(directory, dir_src, time_label):
	# setup
	group_dir = "java"

	# Main.java
	_create_main_java(directory, dir_src, time_label, group_dir)

def create_cpp_files(directory, dir_src, time_label):
	# setup
	group_dir = "cpp"

	# main.cpp
	_create_main_cpp(directory, dir_src, time_label, group_dir)

	# main.c
	_create_main_c(directory, dir_src, time_label, group_dir)

	# lib.c
	_create_lib_c(directory, dir_src, time_label, group_dir)

	# Makefile
#	_create_makefile(directory, dir_src, time_label, group_dir)

	# main.h
	_create_main_h(directory, dir_src, time_label, group_dir)

	# lib.cpp
	_create_lib_cpp(directory, dir_src, time_label, group_dir)

	# do_cgi.cgi
	_create_do_cgi(directory, dir_src, time_label, group_dir, "do_cgi.cgi")

	# create Makefile.in
	_create_file(directory, dir_src, time_label, group_dir, "Makefile.in")

	# create configure.py
	_create_file(directory, dir_src, time_label, group_dir, "configure.py")

	# create configure_in.py
	_create_file(directory, dir_src, time_label, group_dir, "configure_in.py")

	# create commands.txt
	_create_commands_txt(directory, dir_src, time_label, group_dir)
#	_create_file(directory, dir_src, time_label, group_dir, "commands.txt")

def start_project():
  # handle args
  args = sys.argv

  directory = ""; time_label = ""
  directory, time_label, proj, yes_flag  = handle_args(args)

  while(yes_flag == False):
#  while(True):
      ans = raw_input('Create a project. Ok?[y/n]')

      #02 create path
      if ans.lower() == 'n':
          print "You chose 'n'"
          sys.exit(0)
      elif ans.lower() == 'y': break
      else: pass
  #while/

  #03 make directory ------------------------
  create_dirs(directory, time_label, yes_flag)

  # create files ------------------------
  dir_src = os.path.dirname(__file__)

  if proj == "python": create_python_files(dir_src, directory, time_label)
  elif proj == 'cpp': create_cpp_files(directory, dir_src, time_label)
  elif proj == 'java': create_java_files(directory, dir_src, time_label)

if __name__ == '__main__':

  print "Content-Type: text/html"
  print ""

  start_project()



  """
  "/".join(("/var/www/cgi", os.path.basename(os.path.dirname("a/b/main.c")), os.path.splitext(os.path.basename("a/b/main.c"))[0] + ".exe"))
  """