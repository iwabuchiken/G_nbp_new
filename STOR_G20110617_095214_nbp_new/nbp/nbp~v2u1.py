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

def get_content_UTIL(enc_type='utf-8', dir='', time_label=''):
  return """#!/usr/bin/python
# -*- coding: """ + enc_type + """ -*-
#dir=""" + dir + """/""" + time_label + """UTIL.py""" + """
#file=v1u0
#created_at=""" + time_label + """

import sys
import os
import re
import shutil

# methods ========================
def do_job(target_file='main.py'):

  #01 setup ==========================
  dir_name = os.path.basename(os.path.realpath(os.path.dirname(".")))

  if os.path.isdir("./STOR_%s" % dir_name) == False:
    print "STOR directory does not exist"
    exit(0)

  list = os.listdir("./STOR_%s" % dir_name)

  #02 version file exists? ==========================
  reg = re.compile("^version~%s" % target_file)

  flag = 0
  for item in list:
    if reg.search(item):  # if version file exists
      flag = 1          # turn the flag to 1
      version_file = item

  if flag == 0: # if the version file doesn't exist
#    f = file("./STOR_%s/version~%s=1.0" %       (dir_name, target_file.split(".")[0]), "w")
    f = file("./STOR_%s/version~%s=1.0" % (dir_name, target_file), "w")
#    print "New file created: ./STOR_%s/version~%s=1.0" %       (dir_name, target_file.split(".")[0])
    version_file = "version~%s=1.0" % target_file
    print "New file created: ./STOR_%s/%s" % //
            (dir_name, version_file)
  else:
    print "version file for '%s' exists" % target_file
#    print "version file for '%s' exists" % target_file.split(".")[0]

  #03 get version number ==========================
  version_num = version_file.split("=")[1]
  ver = version_num.split(".")[0]
  update = version_num.split(".")[1]

  #04 copy 'main.py' to STOR ==========================
#  copy_name = "%s~v%su%s.py" % (target_file.split(".")[0], ver, update)
  copy_name = "%s~v%su%s.%s" % /
        (target_file.split(".")[0], ver, update, target_file.split(".")[1])
  print "copy_name=", copy_name #debug
  try:
#    shutil.copyfile("./%s.py" % target_file.split(".")[0],       "./STOR_%s/%s" % (dir_name, copy_name))
    shutil.copyfile("./%s.%s" % (target_file.split(".")[0], target_file.split(".")[1]),
                "./STOR_%s/%s" % (dir_name, copy_name))
    print "File copied"
  except Exception, e:
    print e
    print e.args
#    print dir(e)

  #05 update the number of the version file
  try:
    os.rename("./STOR_%s/%s" % (dir_name, version_file),         "./STOR_%s/%s" % (dir_name, version_file.split("=")[0] + "="         + ver + "." + str(int(update)+1)))
  except Exception, e:
    print e


def _do_recalibrate(f, fname, dir_STOR):
  res = f.readlines()
  reg1 = re.compile('^#file=v(/d+)(u|p)(/d+)')
  reg2 = re.compile('v(/d+)(u|p)(/d+).py')
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
#        ver_info = "#file=v%su%s//n" % ver_name
        ver_info = "#file=v%su%s//n" % ver_name
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
#  [1]Variables
#    dir_main  dir of G...
#    dir_STOR  dir of STOR...
#    reg1: '^STOR'
#    reg2: 'v(/d+)(u|p)(/d+).py'
#    reg3: '^#file=v(/d+)(u|p)(/d+)'
#    res1: re.search of reg1
#    res2: re.search of reg2
#    res3: re.search of reg3
#    items: list of G...
#    items2: list of STOR...
#    line: python file in STOR..., each line
#    f: python file in STOR...
#    ver_line: version number extracted from "#file" line
#    ver_name: version number extracted from the name of the python file

  #00 variables
#  new_lines = list()

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
  reg2 = re.compile('v(/d+)(u|p)(/d+).py')
  for item in items2: # files in STOR dir
    res2 = reg2.search(item)
    if res2:  # if item is a python file
      f = file(dir_STOR + "/" + item, "r")  # open the python file
      _do_recalibrate(f, item, dir_STOR)
#      _do_versioning(f, item, dir_STOR)
    #/if
    #debug
#    break
# execute ========================

if __name__ == '__main__':
  args = sys.argv
  if len(args) < 2:
    print "Please input at least one argument"
    exit(0)

  if args[1] == 'v':
    if len(args) == 3:
      do_job(args[2])
    else:
      do_job()
  elif args[1] == "recal":
    recalibrate()
  else:
    print "Usage:"
    print "	", "v <file_name(trunk)> : versioning"
    print "	", "recal : recalibrate version signiture"
""" #% (enc_type, dir, time_label)

def get_time_label2():
  t = datetime.datetime.today()
  t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
  t2 = [str(item) for item in t1]

  for i in range(len(t2)):
    if len(t2[i]) < 2: t2[i] = "0" + t2[i]
      
  return "".join(t2[:3]) + "_" + "".join(t2[3:])


def start_project():
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
