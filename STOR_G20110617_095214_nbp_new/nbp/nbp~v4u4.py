#!/usr/bin/python
# -*- coding: utf-8 -*-
#dir=C:/workspaces/ws_ubuntu_1/G20110617_095214_nbp_new/nbp.py
#file=v2u2
"""
2011/06/17-10:42:39
'nbp_new' command
"""

import sys
import os
import datetime
import re
import shutil
import getopt

VERSION = [4.4, "2011/06/24-17:59:56"]

usage = """Usage: options
  -A  administer
    p: file path
    v: file version
    <EXAMPLE>: python nbp.py -Avp
  -h  help
"""

def get_time_label2():
  t = datetime.datetime.today()
  t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
  t2 = [str(item) for item in t1]

  for i in range(len(t2)):
    if len(t2[i]) < 2: t2[i] = "0" + t2[i]
      
  return "".join(t2[:3]) + "_" + "".join(t2[3:])


def handle_args(args):
  # set time label
  kw = "S:A:hD:"
  opts, strings = getopt.getopt(args[1:], kw)

  time_label = ""; directory = ""

  print "opts=",; print opts
  
  for x, y in opts:
#    if x == 'S': time_label = get_time_label2() + "_" + y
    if x == '-A':
      admin = y
      if 'p' in admin: print "\t", os.path.dirname(os.path.realpath(__file__))
      if 'v' in admin: print "\t", "version=%s" % VERSION
      ans = raw_input("Continue creating a project directory?[y/n]")
      if not ans.lower() == 'y': sys.exit(0)
    if x == '-S': time_label = get_time_label2() + "_" + y
    if x == '-D': directory = y
    
  if time_label == "": time_label = get_time_label2()
#  if directory == "": directory = os.getcwd()
  print directory #debug
  if directory == "" or directory == "$":
      directory = os.path.join("C:","workspaces", "ws_ubuntu_1")
  elif directory[0] == "." and not len(directory) == 1:
      directory = re.sub(".", os.getcwd(), directory, 1)
#      directory = re.sub("/.", os.getcwd(), directory, 1)
  elif directory == ".": directory = os.getcwd()

  return directory, time_label

#  print time_label
#  print directory
#  sys.exit(0)

def start_project():
  # handle args
  args = sys.argv
  directory = ""; time_label = ""

  if len(args) > 1:
    directory, time_label = handle_args(args)
  else:
    directory = os.path.join("C:","workspaces", "ws_ubuntu_1")
    time_label = get_time_label2()

#  print "Syntax: nbp_new <directory>"
  while(True):
      ans = raw_input('Create a project. Ok?[y/n]')

      #02 create path
      if ans.lower() == 'n':
          print "You chose 'n'"
          sys.exit(0)
      elif ans.lower() == 'y':
          break
      else: pass
  #while/

  #03 make directory ------------------------
  command1 = r"md %s\G%s" % (directory, time_label)
  command2 = r"md %s\G%s\STOR_G%s" % (directory, time_label, time_label)
  
  print "Command line will be: "
  print "\t", "%s" % command1
  print "\t", "%s" % command2
  ans = raw_input("Execute the command? [y/n]")

  # if yes, execute
  if ans.lower() == 'y':
    try:
      os.system(command1)
      print r"Directory created: %s\G%s" % (directory, time_label)
    except Exception, e:
      print e

    try:
      os.system(command2)
    except Exception, e:
      print e
    print "Directory created: %s/G%s/STOR_G%s" % \
                      (directory, time_label, time_label)

    # create files ------------------------
    dir_src = os.path.dirname(__file__)
#    print dir_src

    # main.py
    # open the main.py
    _dir = "%s/G%s/main.py" % (directory, time_label)
    f_src = file("%s/main.py" % dir_src, "r").read() % ('utf-8', _dir, time_label )

    try:
        f_dst = file(_dir, "w")
        f_dst.write(f_src)
        f_dst.close()
        print "File written: %s" % _dir
    except Exception, e:
      print e

    # scup
#    current_dir = os.path.dirname(os.path.realpath(__file__))
#    shutil.copyfile("%s/scup" % current_dir, /
#            "%s/G%s/scup" % (directory, time_label))
#
    # UTIL.py
    # prepare text
    f_src = file(r"%s\UTIL.py" % dir_src, "r").readlines()
    text = ""
#    reg1 = re.compile('# -*- coding')
    reg1 = re.compile('# -\*- coding')
    reg2 = re.compile('#dir')
    reg3 = re.compile('#created_at')

    for line in f_src:
      if reg1.search(line): text += line % 'utf-8'
      elif reg2.search(line): text += line % ("%s/UTIL.py" % directory)
      elif reg3.search(line): text += line % get_time_label2()
      else: text += line

    # Write a new file: UTIL.py
    _dir2 = "%s%sG%s%sUTIL.py" % (directory, os.sep, time_label, os.sep)

    try:
      f_dst = file(_dir2, "w")
  #    f2 = file("%s/G%s/UTIL.py" % (directory, time_label), "w")
      f_dst.write(text)
      f_dst.close()
      print "File written: %s" % _dir2
    except Exception, e:
      print e

##    f_src = "upload.py"
##    f_src = r"C:\workspaces\ws_ubuntu_1\G20110617_095214_nbp_new\upload.py"
#    f_src = r"%s%supload.py" % (dir_src, os.sep)
#    f_dst = "%s%sG%s%s%s" % \
#            (directory, os.sep, time_label, os.sep, os.path.basename(f_src))
#    try:
#      shutil.copyfile(f_src, f_dst)
#      print "File copied: %s" % f_src
#    except Exception, e:
#      print e

#    f_src = "main.html"
    f_src = r"%s%smain.html" % (dir_src, os.sep)
    f_dst = "%s%sG%s%s%s" % \
            (directory, os.sep, time_label, os.sep, os.path.basename(f_src))
    try:
      shutil.copyfile(f_src, f_dst)
      print "File copied: %s" % f_dst
#      print "File copied: %s" % f_src
    except Exception, e:
      print e

  else:
    print "You choose not to execute. Ok."
    exit(0)

if __name__ == '__main__':

  print "Content-Type: text/html"
  print ""

  start_project()
