#!C:/Python26/python
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

VERSION = 3.0

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
  if len(args) < 2: return 0
  admin = ""
  if args[1] [:2] == "-A": admin = args[1] [2:]
  if args[1] == "-h": print usage

#  if admin == 'p': print "\t", os.path.dirname(os.path.realpath(__file__))
  if 'p' in admin: print "\t", os.path.dirname(os.path.realpath(__file__))
  if 'v' in admin: print "\t", "version=%s" % VERSION

  sys.exit(0)

def start_project():
  # handle args
  args = sys.argv
  res = handle_args(args)

  print "Syntax: nbp_new <directory>"
  args = sys.argv

  ans = raw_input('Create a project. Ok?[y/n]')

  #02 create path
  if ans.lower() == 'y':
    if len(args) < 2:
#      directory = "C:/workspaces/ws_ubuntu_1"
      directory = r"C:\workspaces\ws_ubuntu_1"
    else:
      directory = str(args[1])

      if directory[0] == ".":
        directory = re.sub("/.", os.getcwd(), directory, 1)
      elif directory == "$":
        directory = r"C:\workspaces\ws_ubuntu_1"

    print directory #debug
    time_label = get_time_label2()
  else:
    print "You chose 'n'"
    exit(0)

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
    _dir2 = "%s/G%s/UTIL.py" % (directory, time_label)

    try:
      f_dst = file(_dir2, "w")
  #    f2 = file("%s/G%s/UTIL.py" % (directory, time_label), "w")
      f_dst.write(text)
      f_dst.close()
      print "File written: %s" % _dir2
    except Exception, e:
      print e

    f_src = "upload.py"
    f_dst = "%s/G%s/%s" % (directory, time_label, f_src)
    try:
      shutil.copyfile(f_src, f_dst)
      print "File copied: %s" % f_src
    except Exception, e:
      print e

  else:
    print "You choose not to execute. Ok."
    exit(0)

if __name__ == '__main__':

  print "Content-Type: text/html"
  print ""

  start_project()
