#!/usr/bin/python
# -*- coding: %s -*-
#dir=%s
#file=v1u0
#created_at=%s

"""
2011/06/17-13:08:20

Author: Iwabuchi Ken

Aim:
    Offer utilities when creating python
    projects.
Usage:
    See variable "USAGE"

"""
import os.path

import sys
import os
import re
import shutil
import datetime
import inspect
import getopt
import traceback

import random

# variables ============s============
VERSION = ["3.0", "2011/07/31-13:43:16"]

USAGE = """<<Usage>>
<Syntax>
    <Create subversion folders>
    u2 sub <folder trunk name>

    <Copy files>
    u2 cp <j|J|java|Java>
      => copy basic java project files
         to the current dir
    u2 cp c_jissen
      => copy "c_jissen"-related files
         to the current dir
"""

# methods ========================
def create_subversin_folders(args):
    """ Variables """
    suffixes = ["master", "repo", "work"]

    # Create subversion dirs ######
    #debug
#    for i in range(len(sys.argv)):
#        print i, "=", sys.argv[i]
#    if sys.argv[1] = "sub" and not sys.argv[2] == "":
    if sys.argv[1] == "sub" and not sys.argv[2] == "":
        print "Create a dir: ", sys.argv[2]
        for string in suffixes:
            os.mkdir(sys.argv[2] + "_" + string)
            print "Dir created: %s" % \
                    (sys.argv[2] + "_" + string)
#        os.mkdir(sys.argv[2])
#//def create_subversin_folders(args):

def copy_files_java(src_dir_path, dst_dir_path):
      #debug
#      print "\n[DEBUG:%d]" \
#                        % inspect.currentframe().f_lineno;
#      print "src_dir_path=", src_dir_path
#      print "dst_dir_path=", dst_dir_path
#      sys.exit(0)

      """
      <variables>
      item => string
            file name in the source dir
      src_file => string
            full path of each file
            in the source dir
      is_successful => integer
            used for return.
            1 => successful
            -1 => at least copying of
                  one file failed
            default => 1
      <processes>
      1. Build a full source dir path
      2. Get a list of files in the source dir
      3. Build a source file path
      4. Copy the files from source dir to
            dst dir
      <Return>
      1     => successful
      -1    => unsuccessful
      """
      """ variables: declare and initialize """
      is_successful = 1

      """ build a full source path """
      src_dir_path = os.path.join(src_dir_path, "java")

      #debug
#      print "\n[DEBUG:%d]" \
#                        % inspect.currentframe().f_lineno;
#      print "src_dir_path=", src_dir_path
#      sys.exit(0)
      
      """ Get a list of the src dir """
      for item in os.listdir(src_dir_path):
            """ Build a src file path """
            src_file = os.path.join(src_dir_path, item)

            """ Copy the file to dst dir """            
            try:
                  """ Execute file copy """
                  shutil.copy(src_file, dst_dir_path)

                  """ Report the result """
                  print "File copied:"
                  print "\t", "From: %s" % src_file
                  print "\t", "To: %s" % \
                              os.path.join(dst_dir_path, item)

            except Exception, e:
                  """ If the copying failed """
                  print "\n[DEBUG:%d]" \
                        % inspect.currentframe().f_lineno;
                  print "Copy failed: %s" % item
                  print e

                  """ set the flag to -1 """
                  if is_successful == 1:
                        is_successful = -1
                  #return -1
            #//try:
      #//for item in os.listdir(src_dir_path)
      """ return value """
      return is_successful

#//def copy_files_java(src_dir_path, dst_dir_path)


def copy_files_c_jissen(src_dir_path, dst_dir_path):
      #debug
#      print "\n[DEBUG:%d]" \
#                        % inspect.currentframe().f_lineno;
#      print "src_dir_path=", src_dir_path
#      print "dst_dir_path=", dst_dir_path
#      sys.exit(0)

      """
      <variables>
      item => string
            file name in the source dir
      src_file => string
            full path of each file
            in the source dir
      is_successful => integer
            used for return.
            1 => successful
            -1 => at least copying of
                  one file failed
            default => 1
      <processes>
      1. Build a full source dir path
      2. Get a list of files in the source dir
      3. Build a source file path
      4. Copy the files from source dir to
            dst dir
      <Return>
      1     => successful
      -1    => unsuccessful
      """
      """ variables: declare and initialize """
      is_successful = 1

      """ build a full source path """
      src_dir_path = os.path.join(
                                    src_dir_path, "cpp", "c_jissen")

      #debug
#      print "\n[DEBUG:%d]" \
#                        % inspect.currentframe().f_lineno;
#      print "src_dir_path=", src_dir_path
#      sys.exit(0)

      """ Get a list of the src dir """
      for item in os.listdir(src_dir_path):
            """ Build a src file path """
            src_file = os.path.join(src_dir_path, item)

            """ Copy the file to dst dir """
            try:
                  """ Execute file copy """
                  shutil.copy(src_file, dst_dir_path)

                  """ Report the result """
                  print "File copied:"
                  print "\t", "From: %s" % src_file
                  print "\t", "To: %s" % \
                              os.path.join(dst_dir_path, item)

            except Exception, e:
                  """ If the copying failed """
                  print "\n[DEBUG:%d]" \
                        % inspect.currentframe().f_lineno;
                  print "Copy failed: %s" % item
                  print e

                  """ set the flag to -1 """
                  if is_successful == 1:
                        is_successful = -1
                  #return -1
            #//try:
      #//for item in os.listdir(src_dir_path)
      """ return value """
      return is_successful

#//def copy_files_c_jissen(src_dir_path, dst_dir_path)


def copy_files(args):
      
      """ Symbols
      1. Java
      2. C: c_jissen
      """
      symbols_j = ["j", "java", "J", "Java"]
      symbols_c_jissen = ["c_jissen"]

      """ Source dir root """
      #src_dir_path = r"C:\workspaces\ws_ubuntu_1\G20110617_095214_nbp_new_work\java"
      src_dir_path = \
                  r"C:\workspaces\ws_ubuntu_1\G20110617_095214_nbp_new_work"

      """ Dest dir path """
      dst_dir_path = os.getcwd()

      """ If files are of a
      1. java project
      2. C: c_jissen
      """

      """ switching """
      if args in symbols_j:
            """ 1. java project """
            copy_files_java(src_dir_path, dst_dir_path)
      elif args in symbols_c_jissen:
            """ 2. C: c_jissen """
            copy_files_c_jissen(src_dir_path, dst_dir_path)
            
#//def copy_files(options):

"""
create_header_file()
<Parameters>

<Return>

<Descriptioins>
1. prepare: lines_src[]
2. prepare: lines_header[]
3. write: lines_header[]
"""
def create_header_file():
    """ vars """
    if len(sys.argv) < 3:
        print "<Usage> util.py hd <source file>"
        sys.exit(0)

    fin_name   = sys.argv[2]
#    fout_name   = "%s.h.test" % os.path.splitext(fin_name)[0]
    fout_name   = "%s.h" % os.path.splitext(fin_name)[0]
    """ prepare: output file """
    if not os.path.isfile(fout_name):
        f = open(fout_name, "w")
        f.close()
        print "File created: %s" % fout_name
#        print "Output file not prepared: %s" % fout_name
#        sys.exit()
    #//if not os.path.isfile(fout_name)

    fin         = open(fin_name, 'r')
    fout        = open(fout_name, 'r')
    lines_src       = list()
    lines_header    = list()
#    regex = re.compile('^((\w|\s)*\((\w|\s)*\))$')
    regex = re.compile('^((\w|\s|\*)*\((\w|\s|\*)*\))$')

    """ prepare: lines_src """
    line = fin.readline()
    while line:
        result = regex.search(line)
        if result:
#            print result.group()
            lines_src.append(result.group().rstrip())
        line = fin.readline()

    #debug
#    print lines_src, "(%d)" % len(lines_src)

    """ prepare: lines_header[] """
    line = fout.readline()
    regex = re.compile('^((\w|\s|\*)*\((\w|\s|\*)*\));$')
    while line:
        print "line=%s" % line
        result = regex.search(line)
        print "result=", result
        if not result:
            lines_header.append(line.rstrip())
        line = fout.readline()
    #debug
    print "<lines_header>"
    print lines_header
    print len(lines_header)

    """ write: lines_header[] 
        1.
        2.
    """
    fout        = open(fout_name, 'w')
    """ 1. lines from the original header file """
    for line in lines_header:
        fout.write(line)
        fout.write('\n')

    """ 2. lines from the source file """
    for line in lines_src:
        fout.write("%s;\n" % line)
#        fout.write('\n')

    """ show message """
    print "File written: %s" % fout_name

    """ close file """
    fin.close()
    fout.close()
#//create_header_file()

def show_usage():
    print """<< Usage >>
    <Options>
        -h      Show usage
        sub     Create subversion folders
        cp      Copy files
                ex: util2.py cp c
                => copy default C files
        hd      Create header file
                ex: util2.py hd sub1.c
                => Create a header file from sub1.c
    """

#//show_usage()

if __name__ == '__main__':
    # 00 =============================
#    if len(sys.argv) < 2: print USAGE; sys.exit(0)

    """ Show usage """
    if len(sys.argv) < 2 or sys.argv[1] == "-h":
        show_usage()
        sys.exit(0)

    """ Create subversion folders """
    if sys.argv[1] == "sub":
            create_subversin_folders(sys.argv)

    """ Copy basic files: java """
    if sys.argv[1] == "cp":
            if len(sys.argv) > 2:
#                  print len(sys.argv)
                  copy_files(sys.argv[2])
            else:
                  print "sys.argv[2] is empty"
    elif sys.argv[1] == "hd":
        create_header_file()
