#!/usr/bin/python
# -*- coding: utf-8 -*-
#dir=C:/workspaces/ws_ubuntu_1/G20110617_095214_nbp_new/nbp.py
#file=v4.31
"""
2011/06/17-10:42:39
'nbp_new' command

Variables
  usage t t1  t2  i kw  opts  strings
  x y admin ans VERSION directory time_label
  command1  command2  args dir_src:os.path.dirname(__file__)
  f_src f_dst _dir  command1_path command2_path

"""
import os.path

import sys
import os
import datetime
import re
import shutil
import getopt
import inspect
import traceback

VERSION = ["4.24", ""]
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
	=> Java: ["java", "j", "J"]
	=> Ruby: ["r", "R", "ruby", "Ruby"]
	=> PIC: ["ee", "e", "E", "EE"] ===> See the option 'S'
	=> PHP: ["php", "PHP", "h", "H"]
  -S<string>  Add a string to the tail of the time label
	=> '-Spic10**' or '-Sp10**' ==> directory name will be 'PIC10**'
	=> '-Spic12**' or '-Sp12**' ==> directory name will be 'PIC12**'
	=> '-S**' ==> directory name will be 'PIC00***'

<<configure.py>>

"""
log_dir_path = os.path.join(os.path.dirname(__file__), "log")
if not os.path.isdir(log_dir_path):
    os.mkdir(log_dir_path)
    print "log dir created: %s" % log_dir_path

#logfile_path = r"C:\workspaces\ws_ubuntu_1\G20110617_095214_nbp_new\log\log_nbp.txt"
logfile_path = os.path.join(log_dir_path, "nbp.log")
logfile = file(logfile_path, "a")

# functions =============================
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
		elif y in ["r", "R", "ruby", "Ruby"]:
			proj = "ruby"
		elif y in ["php", "PHP", "h", "H"]:
			proj = "php"
		elif y in ["ee", "e", "E", "EE"]:
			proj = "ee"
			directory = os.path.join("C:", os.sep,"workspaces", "ws_ee_1", "mplab", "projects")
		else:
			print "Project type not specified: Set to default => Python"
			proj = "python"
	elif x == '-y': yes_flag = True
    
  if time_label == "": time_label = get_time_label2()

  if directory == "" or directory == "$":
#      directory = os.path.join("C:", os.sep,"workspaces", "ws_ubuntu_1")
      directory = os.path.dirname(os.path.dirname(__file__))
  elif directory[0] == "." and not len(directory) == 1:
      directory = re.sub(".", os.getcwd(), directory, 1)
  elif directory == ".": directory = os.getcwd()

  if proj == "": proj = "python"

  print "directory=%s" % directory #debug
  print "time_label=%s" % "_".join(time_label.split("_")[:2]) #debug
  print "Project type: %s" % proj

  # log
  logfile.write("directory=%s\n" % directory)
  logfile.write("time_label=%s\n" % "_".join(time_label.split("_")[:2]))
  logfile.write("Project type: %s\n" % proj)

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

	f_src = file("%s/%s/main.py" % (dir_src, group_dir), "r").read()

	word_list = {
			"{{coding}}": 'utf-8',
			"{{dir}}": _dir,
			"{{created_at}}": "_".join(time_label.split("_")[:2]),
			"{{version}}": get_time_label3(),
			"{{debug}}": 'print "[DEBUG:%d]" % inspect.currentframe().f_lineno\nsys.exit()'
	}

	for key in word_list.keys():
		f_src = f_src.replace(key, word_list[key], 1)

	#debug
#	print f_src
#	print "[DEBUG:%d]" % inspect.currentframe().f_lineno; sys.exit()

#                      get_time_label3(),\
#				  123)
#            ('utf-8', _dir, time_label, get_time_label3())
#	print "[DEBUG:%d]" % inspect.currentframe().f_lineno; sys.exit()

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

def _create_main_rb(dir_src, directory, time_label, group_dir):
	fname = "main.rb"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	f_dst = "%s" % os.path.join(
			directory, \
			"G" + time_label, \
			os.path.basename(f_src))

	try:
		f = file(f_src, "r")
		content = f.read()

		content = content.replace("#file_info", \
                            "#v=1.0\n#created_at=%s\n#project=%s" % \
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



def _create_main_php(
				dir_src, directory, time_label, group_dir, genre="php"):
	      # open the main.php
	_dir = os.path.join(
				directory, "G" + time_label, "main.%s" % genre)

	f_src = file("%s/%s/main.%s" %
				(dir_src, group_dir, genre), "r").read()

	word_list = {
			"@created_at@": time_label,
			"@version@": "1.0",
			"@debug@": 'echo "[".basename(__FILE__).":".__LINE__."]"'
	}

	#debug
#	print "[DEBUG:%d]" % inspect.currentframe().f_lineno
#	print word_list
#	sys.exit(0)

	for key in word_list.keys():
#		f_src = f_src.replace(key, word_list[key], 1)
		f_src = f_src.replace(key, word_list[key])

	try:
          f_dst = file(_dir, "w")
          f_dst.write(f_src)
          f_dst.close()
          print "File written: %s" % _dir
	except Exception, e: print e
#//def _create_main_php(dir_src, directory, time_label, group_dir)

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

def _get_libc_version_file(directory):
	reg = re.compile('(version~lib.c)=(.+)')
	files = [item for item in os.listdir(directory) if reg.search(item)]

	if len(files) > 0:
		name = reg.search(files[0]).groups()[1]
		name = ".".join((name.split(".")[0], str(int(name.split(".")[1])-1)))
#		return reg.search(files[0]).groups()[1]
		return name
	else: return "NA"
#						os.listdir(directory) if os.path.isfile(item)
#						os.listdir(directory) if and reg.search(item)]
#	print files


def _create_lib_c(directory, dir_src, time_label, group_dir):
#	fname = "%s" % f_name
	fname = "lib.c"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	f_dst = "%s" % os.path.join(
			directory, \
			"G" + time_label, \
			os.path.basename(f_src))

	# get lib.c version file name
	libc_version_name = \
				_get_libc_version_file(
					os.path.join(dir_src, group_dir, "STOR_cpp"))

	try:
		f = file(f_src, "r")
		content = f.read()

		content = content.replace("//file_info", \
#                            "//v=1.0\n//created_at=%s\n//project=%s" % \
                            "//v=%s\n//created_at=%s\n//project=%s" % \
#                              ("_".join( libc_version_name, \
                              (libc_version_name, \
						"_".join( time_label.split("_")[:2]), \
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
#//def _create_lib_py(dir_src, directory, time_label, group_dir)

def _create_commands_txt_java(directory, dir_src, time_label, group_dir, ext='java'):
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

#		content = content.replace(
#							"@path@", \
#							os.path.dirname(f_dst),\
#							2)

		content = content.replace(
							"@path1@", \
							os.path.dirname(f_dst),\
							2)

		content = content.replace(
							"@path2@", \
							os.path.basename(os.path.dirname(f_dst)),\
							3)
#							2)
		content = content.replace("@ext@", ext, 5)
#		content = content.replace("@ext@", ext, 3)

	except Exception, e: print e

	# write a file
	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e

def _create_commands_txt(
			directory, dir_src, time_label, group_dir, ext='py'):
#	fname = "%s" % f_name
	fname = "commands.txt"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	f_dst = "%s" % os.path.join(
			directory, \
			"G" + time_label, \
			os.path.basename(f_src))
	word_list = {
			"@path1@": os.path.dirname(f_dst),
			"@path2@": os.path.basename(os.path.dirname(f_dst)),
			"@created_at@": "_".join(time_label.split("_")[:2]),
			"@ext@": ext
	}

	try:
		f = file(f_src, "r")
		content = f.read()

		for key in word_list.keys():
	#		f_src = f_src.replace(key, word_list[key], 1)
			content = content.replace(key, word_list[key])
	
#		content = content.replace(
#							"@path1@", \
#							os.path.dirname(f_dst),\
#							2)
#
#		content = content.replace(
#							"@path2@", \
#							os.path.basename(os.path.dirname(f_dst)),\
##							2)
#							3)
#		content = content.replace("@ext@", ext, 4)
#		content = content.replace("@ext@", ext, 3)
#		content = content.replace("@ext@", ext, 2)

	except Exception, e: print e

	# write a file
	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e

def _create_commands_txt_ee(directory, dir_src, time_label, group_dir, ext='asm'):
#	fname = "%s" % f_name
	fname = "commands.txt"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	if not os.path.isdir(os.path.join(directory, "PIC10_%s" % time_label)):
			os.mkdir(os.path.join(directory, "PIC10_%s" % time_label))

	f_dst = "%s" % os.path.join(
			directory, \
			"PIC10_%s" % time_label, \
#			"G" + time_label, \
			"commands.txt")
#			"PIC10_%s.asm" % time_label)
#	f_dst = "%s" % os.path.join(
#			directory, \
#			"G" + time_label, \
#			os.path.basename(f_src))

	try:
		f = file(f_src, "r")
		content = f.read()

#		content = content.replace(
#							"@path@", \
#							os.path.dirname(f_dst),\
#							2)

		content = content.replace(
							"@path1@", \
							os.path.dirname(f_dst),\
							2)

		content = content.replace(
							"@path2@", \
							os.path.basename(os.path.dirname(f_dst)),\
							2)
#							4)

		content = content.replace(
							"@path3@", \
							"_".join((os.path.basename(os.path.dirname(f_dst)).split("_")[:3])),\
#							"_".join((os.path.dirname(os.path.dirname(f_dst)).split("_")[:3])),\
#							"_".join((time_label.split("_")[:3])),\
							2)

		content = content.replace("@ext@", ext, 5)
#		content = content.replace("@ext@", ext, 3)
#		content = content.replace("@ext@", ext, 2)

	except Exception, e: print e

	# write a file
	try:
          f = file(f_dst, "w")
          f.write(content)
          print "New file created: %s" % f_dst
	except Exception, e: print e

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
#//def _create_lib_cpp(directory, dir_src, time_label, group_dir)

def _create_asm(dir_src, directory, time_label, group_dir):
	fname = "main.asm"
	f_src = "%s" % os.path.join(dir_src, group_dir, fname)

	if "pic10" in time_label.lower(): pic_type = "PIC10"
	elif "pic12" in time_label.lower(): pic_type = "PIC12"

#	if not os.path.isdir(os.path.join(directory, "PIC10_%s" % time_label)):
	if not os.path.isdir(os.path.join(directory, "%s_%s" % (pic_type, time_label))):
		os.mkdir(os.path.join(directory, "%s_%s" % (pic_type, time_label)))
#		os.mkdir(os.path.join(directory, "PIC10_%s" % time_label))

	f_dst = "%s" % os.path.join(
			directory, \
			"%s_%s" % (pic_type, time_label), \
#			"PIC10_%s" % time_label, \
#			"G" + time_label, \
			"%s_%s.asm" % (pic_type, time_label))
#			os.path.basename(f_src))

	try:
		f = file(f_src, "r")
		content = f.read()

		content = content.replace("@file_info@", \
#		content = content.replace("#file_info", \
#                            "v=1.0 created_at=%s project=%s" % \
                            "v=1.0\n;created_at=%s\n;project=%s" % \
#                            "#v=1.0\n#created_at=%s\n#project=%s" % \
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
	command3 = "md %s" % os.path.join(directory, "G" + time_label, "log")

	print "Command line will be: "
	print "\t", "%s" % command1
	print "\t", "%s" % command2
	print "\t", "%s" % command3

	while (yes_flag == False):
#	while (True):
		ans = raw_input("Execute the command? [y/n]")
		# if yes, execute
		if ans.lower() == 'n':
			print "You choose not to execute. Ok."
			logfile.write("Execution not chosen.\n")

			exit(0)
		else: break
	try:
		os.system(command1)
		print "Directory created: %s" % os.path.join(directory, "G" + time_label)
		logfile.write("Directory created: %s\n" % os.path.join(directory, "G" + time_label))
		
	except Exception, e: print e

	try:
		os.system(command2)
		print "Directory created: %s" % \
			    os.path.join(directory, "G" + time_label, "STOR_G" + time_label)
		logfile.write("Directory created: %s\n" % \
			    os.path.join(directory, "G" + time_label, "STOR_G" + time_label))

	except Exception, e: print e

	try:
		os.system(command3)
		print "Directory created: %s" % \
			    os.path.join(directory, "G" + time_label, "log")
		logfile.write("Directory created: %s\n" % \
			    os.path.join(directory, "G" + time_label, "log"))

	except Exception, e: print e

#def create_dirs_ee(directory, time_label, yes_flag):
def create_dirs_ee(directory, time_label, yes_flag):
	print "directory=", directory

	if "pic10" in time_label.lower() or "p10" in time_label.lower(): pic_type = "10"
	elif "pic12" in time_label.lower() or "p12" in time_label.lower(): pic_type = "12"
#	elif "pic12" in time_label.lower(): pic_type = "12"
	else: pic_type = "00"
#	else: pic_type = "**"

	command1 = "md %s" % os.path.join(directory, "PIC%s_%s" %(pic_type, time_label))
	command2 = "md %s" % os.path.join(directory, "PIC%s_%s" %(pic_type, time_label), "STOR_PIC%s_%s" % (pic_type, time_label))
	command3 = "md %s" % os.path.join(directory, "PIC%s_%s" %(pic_type, time_label), "log")
#	command1 = "md %s" % os.path.join(directory, "PIC10_" + time_label)
#	command2 = "md %s" % os.path.join(directory, "PIC10_" + time_label, "STOR_PIC10" + time_label)
#	command3 = "md %s" % os.path.join(directory, "PIC10_" + time_label, "log")

	print "Command line will be: "
	print "\t", "%s" % command1
	print "\t", "%s" % command2
	print "\t", "%s" % command3

	while (yes_flag == False):
#	while (True):
		ans = raw_input("Execute the command? [y/n]")
		# if yes, execute
		if ans.lower() == 'n':
			print "You choose not to execute. Ok."
			logfile.write("Execution not chosen.\n")

			exit(0)
		else: break
	try:
		os.system(command1)
		print "Directory created: %s" % os.path.join(directory, "PIC%s_%s" %(pic_type, time_label))
		logfile.write("Directory created: %s\n" % os.path.join(directory, "PIC%s_%s" %(pic_type, time_label)))
#		logfile.write("Directory created: %s\n" % os.path.join(directory, "PIC10_" + time_label))

	except Exception, e: print e

	try:
		os.system(command2)
		print "Directory created: %s" % \
			    os.path.join(directory, "PIC%s_%s" %(pic_type, time_label), "STOR_PIC%s_%s" %(pic_type, time_label))
		logfile.write("Directory created: %s\n" % \
			    os.path.join(directory, "PIC%s_%s" %(pic_type, time_label), "STOR_PIC%s_%s" %(pic_type, time_label)))
#			    os.path.join(directory, "PIC10_" + time_label, "STOR_PIC10_" + time_label))

	except Exception, e: print e

	try:
		os.system(command3)
		print "Directory created: %s" % \
			    os.path.join(directory, "PIC%s_%s" %(pic_type, time_label), "log")
#			    os.path.join(directory, "PIC10_" + time_label, "log")
		logfile.write("Directory created: %s\n" % \
			    os.path.join(directory, "PIC%s_%s" %(pic_type, time_label), "log"))
#			    os.path.join(directory, "PIC10_" + time_label, "log"))

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

	logfile.write("Python files created[%s]\n" % get_time_label3())

def create_ruby_files(directory, dir_src, time_label):
	group_dir = "ruby"
	# main.py
	_create_main_rb(dir_src, directory, time_label, group_dir)

	# create commands.txt
	_create_commands_txt(directory, dir_src, time_label, group_dir, ext='rb')

	# create main.html
	_create_main_html(directory, dir_src, time_label, group_dir)

	# create main.js
	_create_main_js(dir_src, directory, time_label, group_dir)

	logfile.write("Ruby files created[%s]\n" % get_time_label3())

def create_ee_files(directory, dir_src, time_label):
	group_dir = "ee"
	# main.py
	_create_asm(dir_src, directory, time_label, group_dir)

	# create commands.txt
	_create_commands_txt_ee(directory, dir_src, time_label, group_dir, ext='asm')
#	_create_commands_txt(directory, dir_src, time_label, group_dir, ext='asm')

	logfile.write("%s files created[%s]\n" % (group_dir, get_time_label3()))

def create_php_files(directory, dir_src, time_label):
	group_dir = "php"
	# main.php
	_create_main_php(dir_src, directory, time_label, group_dir)

	# main.py
	_create_main_py(dir_src, directory, time_label, group_dir)

	# main.html
	_create_main_html(directory, dir_src, time_label, group_dir)
	# main.js
	_create_main_js(dir_src, directory, time_label, group_dir)
	# lib.py
	_create_lib_py(dir_src, directory, time_label, group_dir)

	# create commands.txt
	_create_commands_txt(
				directory, dir_src, time_label, group_dir, ext="php")

	logfile.write("'%s' files created[%s]\n" %
								(group_dir, get_time_label3()))
#//def create_php_files(directory, dir_src, time_label)

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

	# command.txt
	_create_commands_txt_java(directory, dir_src, time_label, group_dir, ext='java')

	logfile.write("java files created[%s]\n" % get_time_label3())

def create_cpp_files(directory, dir_src, time_label):
	# setup
	group_dir = "cpp"

	# create dirs
	os.mkdir("%s" % \
			os.path.join(directory, "G" + time_label, "image"))		# image
	os.mkdir("%s" % \
			os.path.join(directory, "G" + time_label, "etc"))	# etc

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
	_create_commands_txt(directory, dir_src, time_label, group_dir, ext='c')
#	_create_file(directory, dir_src, time_label, group_dir, "commands.txt")

	# log
	logfile.write("cpp files created[%s]\n" % get_time_label3())
	
def start_project():
  # handle args
	args = sys.argv
#	logfile_path = r"C:\workspaces\ws_ubuntu_1\G20110617_095214_nbp_new\log\log_nbp.txt"
#	logfile = file(logfile_path, "a")
	logfile.write("[Session log:%s]--------------------\n" % get_time_label3())

#	directory = ""; time_label = ""
	directory, time_label, proj, yes_flag  = handle_args(args)

	while(yes_flag == False):
#  while(True):
		ans = raw_input('Create a project. Ok?[y/n]')

		#02 create path
		if ans.lower() == 'n':
			print "You chose 'n'"
			logfile.write("'Create a project' ==> 'n' chosen\n")
			logfile.write("[/Session log:%s]--------------------\n" % get_time_label3())
			sys.exit(0)
		elif ans.lower() == 'y': break
		else: pass
  #while/

	#03 make directory ------------------------
	# project mplab --> create directories
	if proj == "ee": create_dirs_ee(directory, time_label, yes_flag)
	else: create_dirs(directory, time_label, yes_flag)

	# create files ------------------------
	dir_src = os.path.dirname(__file__)

	if proj == "python": create_python_files(dir_src, directory, time_label)
	elif proj == 'cpp': create_cpp_files(directory, dir_src, time_label)
	elif proj == 'java': create_java_files(directory, dir_src, time_label)
	elif proj == 'ruby': create_ruby_files(directory, dir_src, time_label)
	elif proj == 'ee':
		create_ee_files(directory, dir_src, time_label)
		os.system("C:\\Microchip_8.50\\\"MPLAB IDE\"\\Core\\MPLAB.exe")
	elif proj == 'php': create_php_files(directory, dir_src, time_label)
	
	logfile.write("[/Session log:%s]--------------------\n" % get_time_label3())
	logfile.write("\n")

	# ending
	command = "cd %s" % os.path.join(directory, "G" + time_label)
	
	print "========================================"
	print "\t\t<nbp.py>"
	print "All the works done successfully."
	print "New directory is:"
	print "%s" % command
#	print "\t%s" % command
	print "========================================"

#	command = "cd %s" % os.path.join(directory, "G" + time_label)
#	print command
#	os.system(command)

	sys.exit(0)

if __name__ == '__main__':

  print "Content-Type: text/html"
  print ""

  start_project()



  """
  "/".join(("/var/www/cgi", os.path.basename(os.path.dirname("a/b/main.c")), os.path.splitext(os.path.basename("a/b/main.c"))[0] + ".exe"))
  """