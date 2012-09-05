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

"""
Variables

"""

# vars and constants ========================
VERSION = [1.0, "2011/06/28-14:29:35"]

usage = """<<Usage>>
  <Options>
    -D<path> download path: default=os.getcwd()
      "." => os.getcwd()
    -F<path> file path from which to upload
        :default=/var/www/cgi-bin/Gxxx/main.py
    -U<name> user name: default="root"
    -P<password> password: default=~
  <Example>
    1. download.py -D. -FUTIL.py
      => upload "UTIL.py" in the current dir to
          "/var/www/cgi-bin/Gxxxxxx_xxxxxx_xxxxxx/UTIL.py"    
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

def handle_args(args):
  # initiate the variables
  username = ""
  passwd = ''
  f_path_src = list()
  f_path_dst = ""
  dir_path_dst = ""

#  kw = "hU:F:D:"
  kw = "hU:F:D:P:"
  opts, strings = getopt.getopt(args[1:], kw)

#  print opts
#  sys.exit(0)

  if "-h" in [list(i)[0] for i in opts]:
    print usage
    print VERSION
    sys.exit(0)
  
  for x, y in opts:
      if x == "-h": print VERSION#; sys.exit(0)
      if x == "-U": username = y
      if x == "-F": f_path_src.append(y)
#          if y == '*': file_path_src = get_file_list()
#          else:
#              files = y.split(",")
#              for item in files:
#                  file_path_src.append(os.path.join(os.getcwd(), item))
      if x == "-D": #f_path_dst = y
          if y == '.': f_path_dst = os.path.join(os.getcwd(), os.path.basename(f_path_src[0]))
          else: f_path_dst = y
#          if y == '.': dir_path_dst = "/var/www/cgi-bin/%s" % \
#                    os.path.basename(os.getcwd())
#          else: dir_path_dst = y
      if x == "-P": passwd = y
      else: pass
  #for/

  # set defaults
  if username =="": username = "root"
#  if len(f_path_src) == 0: file_path_src.append(\
#                                        os.path.join(os.getcwd(), "main.py"))
#  if len(file_path_dst) == 0:  file_path_dst = "/var/www/cgi-bin/%s" % \
#                                      "/".join((os.path.basename(os.getcwd()), "main.py"))
#  if dir_path_dst == "":
#      dir_path_dst = "/var/www/cgi-bin/%s" % \
#                                    os.path.basename(os.getcwd())

  # build file_path_src
  # single file
#  if len(file_path_src) == 1:
#      if not ":" in file_path_src[0][:4]: file_path_src[0] = os.path.join(os.getcwd(), file_path_src[0])
  # multiple files
#  if len(file_path_src) > 1:
#      for i in range(len(file_path_src)): # on each file path
#          # such as "main.js"
#          if len(file_path_src[i]) > 2 and not ":" in file_path_src[i][:2]:
#              file_path_src[i] = os.path.join(os.getcwd(), file_path_src[i])
#          else: file_path_src[i] = os.path.join(os.getcwd(), file_path_src[i])

#  for item in file_path_src:
#    file_path_dst.append(dir_path_dst + "/" + os.path.basename(item))

  return username, f_path_src, f_path_dst, passwd
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

def do_job(): 
  # setup variables
  args = sys.argv
  if len(args) < 2:
    print usage
    sys.exit(0)
  username, f_path_src, f_path_dst, passwd = handle_args(args)

#  #debug
#  print username
#  print f_path_src
#  print f_path_dst
#  print passwd
#  sys.exit(0)
  
  #debug
  print "username=%s" % username
  
  # create an ssh instance ----------------------------
  ssh = get_ssh(username, passwd)

  # Dir exists? --------------------------------------
#  res = is_dir(ssh, os.path.dirname(file_path_dst[0]))

  # if dir exists ---------------
#  if res == 1: print "Dir exists: %s" % os.path.dirname(file_path_dst[0])
  # if not exist ---------------
#  elif res == -1:
#    print "Dir does not exist: %s" % os.path.dirname(file_path_dst[0])
    # create a new dir?
#    while (True):
#      ans = raw_input("Create a dir?[y/n]")
#      if ans.lower() == 'n': break
#      # create a dir
#      if ans.lower() == 'y':
#        res_makedir = makedir(ssh, os.path.dirname(file_path_dst[0]))
#        if res_makedir == 1: print "Dir created: %s" % os.path.dirname(file_path_dst[0])
#        else: print res_makedir
#        break
#  else: print res

  # download file -----------------------------------
  try:      
      sftp = ssh.open_sftp()
      print "sftp opened"
  except Exception, e: print e

  for item in f_path_src:
      try:
          print "File downloading:"
          print "\t", "From: %s" % item
          print "\t", "To: %s" % f_path_dst

          sftp.get(item, f_path_dst)

          print "File downloaded:"
          print "\t", "From: %s" % item
          print "\t", "To: %s" % f_path_dst
      except Exception, e: print e

#  for i in range(len(file_path_dst)):
#
#
#    res = is_file(ssh, file_path_dst[i])
#
#    if res == 1:
#      print "File exists: %s" % file_path_dst[i]
#      ans = raw_input("Overwrite a file?[y/n]")
#      # Overwrite
#      if ans.lower() == 'y':
#        print "Overwrite"
#        try:
#          sftp.put(file_path_src[i], file_path_dst[i])
#          print "File uploaded"
#          print "\t", "From: %s" % file_path_src[i]
#          print "\t", "To: %s" % file_path_dst[i]
#        except Exception, e: print e
#
#      if ans.lower() == 'n': print "Not overwrite"
#    # file does not exist
#    if res == -1:
#      try:
#          sftp.put(file_path_src[i], file_path_dst[i])
#          print "File uploaded:"
#          print "\t", "From: %s" % file_path_src[i]
#          print "\t", "To: %s" % file_path_dst[i]
#      except Exception, e: print e

    
# execute ========================
if __name__ == '__main__':
  print "Content-Type: text/html"
  print ""

  do_job()
