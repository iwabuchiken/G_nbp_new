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

# vars and constants ========================
VERSION = [4.2, "2011/06/23-07:12:02"]

usage = """<Usage>
  -D destination path
    . /var/www/cgi-bin
  -F file path to upload
  -U user name
<Example>
  python main.py -D. -FUTIL.py
  => upload UTIL.py in the current dir to /var/www/cgi-bin/<dir name>/UTIL.py
"""
# methods ========================
def get_time_label2():
  t = datetime.datetime.today()
  t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
  t2 = [str(item) for item in t1]

  for i in range(len(t2)):
    if len(t2[i]) < 2: t2[i] = "0" + t2[i]

  return "".join(t2[:3]) + "_" + "".join(t2[3:])

def get_ssh(username=''):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  if username == '': username = raw_input("Username: ")
#  msg = "Password for %s: " % username
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
  username = ""; file_path_src = list(); dir_path_dst = ""; file_path_dst = list()

  if len(args) < 2: username = "root"
  else:
    for item in args:
      if item[:2] == "-h":
        print VERSION; sys.exit(0)
      if item[:2] == "-U":      username = item[2:]
      elif item[:2] == "-F":
        if item[2:] == '*': file_path_src = get_file_list()
        else: file_path_src.append(item[2:])
      elif item[:2] == "-D":
        if item[2:] == '.': dir_path_dst = "/var/www/cgi-bin/%s" % \
                  os.path.basename(os.getcwd())
        else: dir_path_dst = "%s" % item[2:]
      else: pass
  if username =="": username = "root"

  # build file_path_src
  if len(file_path_src) == 1:
    if not ":" in file_path_src[0][:4]: file_path_src[0] = os.path.join(os.getcwd(), file_path_src[0])
  if len(file_path_src) > 1:
    for i in range(len(file_path_src)):
      if len(file_path_src[i]) > 2 and not ":" in file_path_src[i][:2]:
        file_path_src[i] = os.path.join(os.getcwd(), file_path_src[i])
      else: file_path_src[i] = os.path.join(os.getcwd(), file_path_src[i])

  # change the file name?
#  ans = raw_input("Change the file name?[y/n]")
#  if ans.lower() == 'y':
#    new_name = raw_input("Please type the new name(ex. main2.py): ")
#  else:
#    new_name = os.path.basename(file_path_src)

#  file_path_dst = dir_path_dst + "/" + new_name
#  print "file_path_src"
  for item in file_path_src:
    file_path_dst.append(dir_path_dst + "/" + os.path.basename(item))
#    print item

#  print "dir_path_dst=", dir_path_dst
#  for item in file_path_dst:
#    print item
#  sys.exit(0) #debug

  return username, file_path_src, file_path_dst


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
  username, file_path_src, file_path_dst = handle_args(args)
  
  #debug
  print "username=%s" % username
  
  # create an ssh instance ----------------------------
  ssh = get_ssh(username)

  # Dir exists? --------------------------------------
  res = is_dir(ssh, os.path.dirname(file_path_dst[0]))

  # if dir exists ---------------
  if res == 1: print "Dir exists: %s" % os.path.dirname(file_path_dst[0])
  # if not exist ---------------
  elif res == -1:
    print "Dir does not exist: %s" % os.path.dirname(file_path_dst[0])
    # create a new dir?
    while (True):
      ans = raw_input("Create a dir?[y/n]")
      if ans.lower() == 'n': break
      # create a dir
      if ans.lower() == 'y':
        res_makedir = makedir(ssh, os.path.dirname(file_path_dst[0]))
        if res_makedir == 1: print "Dir created: %s" % os.path.dirname(file_path_dst[0])
        else: print res_makedir
        break
  else: print res

  # file exists? -----------------------------------
  for i in range(len(file_path_dst)):
    try:
      sftp = ssh.open_sftp()
      print "sftp opened"
    except Exception, e: print e

    res = is_file(ssh, file_path_dst[i])

    if res == 1:
      print "File exists: %s" % file_path_dst[i]
      ans = raw_input("Overwrite a file?[y/n]")
      # Overwrite
      if ans.lower() == 'y':
        print "Overwrite"
        try:
          sftp.put(file_path_src[i], file_path_dst[i])
          print "File uploaded"
          print "\t", "From: %s" % file_path_src[i]
          print "\t", "To: %s" % file_path_dst[i]
        except Exception, e: print e

      if ans.lower() == 'n': print "Not overwrite"
    # file does not exist
    if res == -1:
      try:
          sftp.put(file_path_src[i], file_path_dst[i])
          print "File uploaded:"
          print "\t", "From: %s" % file_path_src[i]
          print "\t", "To: %s" % file_path_dst[i]
      except Exception, e: print e

  # exec fromdos --------------------------------
  ans = raw_input("Exec 'fromdos'?[y/n]")
  if ans.lower() == 'y':
    for item in file_path_dst:
      try:
        ssh.exec_command("fromdos %s" % item)
        print "'fromdos' done to: %s" % item
      except Exception, e: print e
  else:
    pass
#    print "All the work done. Thank you for working with me. See you again"
#    sys.exit(0)
  # exec chmod --------------------------------
  ans = raw_input("Exec 'chmod'(755)?[y/n]")
  if ans.lower() == 'y':
    for item in file_path_dst:
      try:
#        ssh.exec_command("C %s" % item)
        ssh.exec_command("chmod 755 %s" % item)
        print "'chmod'(755) done to: %s" % item
      except Exception, e: print e
  else:
    pass
  print "All the work done. Thank you for working with me. See you again"
  sys.exit(0)
    
# execute ========================
if __name__ == '__main__':
  print "Content-Type: text/html"
  print ""

  do_job()
