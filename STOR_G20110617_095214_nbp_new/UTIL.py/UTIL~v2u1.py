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

VERSION = ["1.0", "2011/07/06-12:08:34"]
USAGE = """<<Usage>>
	<Syntax>

	<Options>

	<Examples>

"""

# methods ========================
def get_time_label2():
  t = datetime.datetime.today()
  t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
  t2 = [str(item) for item in t1]

  for i in range(len(t2)):
    if len(t2[i]) < 2: t2[i] = "0" + t2[i]
      
  return "".join(t2[:3]) + "_" + "".join(t2[3:])

def do_job(target_file='main.py'):

  #01 setup ==========================
  dir_name = os.path.basename(os.path.realpath(os.path.dirname(".")))
#  print dir_name #debug

  if os.path.isdir("./STOR_%s" % dir_name) == False:
    print "STOR directory does not exist"
    exit(0)

  list = os.listdir("./STOR_%s" % dir_name)
  print list #debug

  #02 version file exists? ==========================
  reg = re.compile("^version~%s" % target_file)

  flag = 0
  for item in list:
    if reg.search(item):  # if version file exists
      flag = 1          # turn the flag to 1
      version_file = item

#  print "flag: ", str(flag)
#  print "version_file: ", version_file

  if flag == 0: # if the version file doesn't exist
#    f = file("./STOR_%s/version~%s=1.0" %       (dir_name, target_file.split(".")[0]), "w")
    f = file("./STOR_%s/version~%s=1.0" % (dir_name, target_file), "w")
#    print "New file created: ./STOR_%s/version~%s=1.0" %       (dir_name, target_file.split(".")[0])
    version_file = "version~%s=1.0" % target_file
    print "New file created: ./STOR_%s/%s" % \
            (dir_name, version_file)
  else:
    print "version file for '%s' exists" % target_file
#    print "version file for '%s' exists" % target_file.split(".")[0]

  #03 get version number ==========================
  version_num = version_file.split("=")[1]
  ver = version_num.split(".")[0]
  update = version_num.split(".")[1]

#  print version_num, ver, update
  #04 copy 'main.py' to STOR ==========================
#  copy_name = "%s~v%su%s.py" % (target_file.split(".")[0], ver, update)
  copy_name = "%s~v%su%s.%s" %         (target_file.split(".")[0], ver, update, target_file.split(".")[1])
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
    os.rename("./STOR_%s/%s" % (dir_name, version_file),\
            "./STOR_%s/%s" % (dir_name, version_file.split("=")[0] + "="  \
            + ver + "." + str(int(update)+1)))
    print "File renamed to: %s" % version_file
  except Exception, e:
    print e


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
#  [1]Variables
#    dir_main  dir of G...
#    dir_STOR  dir of STOR...
#    reg1: '^STOR'
#    reg2: 'v(\d+)(u|p)(\d+).py'
#    reg3: '^#file=v(\d+)(u|p)(\d+)'
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
