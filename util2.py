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

def create_header_file():
    """ vars """
    content = ""    # content of the source file
    line    = ""    # line from the input file
    if len(sys.argv) > 2:
        src_file_name = sys.argv[2] # source file name
    else:
        print "Usage: util2.py hd sub1.c"
        sys.exit(0)
    #//if len(sys.argv) 2
    src_file_name = sys.argv[2]
    out_file_name = "%s_test.h" % \
            os.path.splitext(src_file_name)[0]

    """ Open the output file """
    fin = file(src_file_name, "r")
#    fout = file(out_file_name, "w+")
    fout = file(out_file_name, "r+")
    print "Files opened"

    """ set the reg expression """
    regex = re.compile("^((\w|\s)*\((\w|\s)*\))$")

    """ read, search, write """
    line = fin.readline()
    while line:
        result = regex.search(line)
#        if regex.search(line)
        if result:
#            line[-1] = ";"
#            line[-1] = ';'
#            print line[-1]
#            print line[-2]
#            fout.write("%s;\n" % line)
            line_out = fout.readline()
            fout.write("%s;\n" % line.rstrip())
        line = fin.readline()
    print "File written: %s" % out_file_name
    
    """ Close the output file """
    fout.close()
    fin.close()
    print "Files closed"

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
