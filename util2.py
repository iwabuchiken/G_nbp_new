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
    

    if sys.argv[1] == "sub" and not sys.argv[2] == "":
        print "Create a dir: ", sys.argv[2]
        for string in suffixes:
            os.mkdir(sys.argv[2] + "_" + string)
            print "Dir created: %s" % \
                    (sys.argv[2] + "_" + string)

#//def create_subversin_folders(args):

def copy_files_java(src_dir_path, dst_dir_path):
      

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

    fout_name   = "%s.h" % os.path.splitext(fin_name)[0]
    """ prepare: output file """
    if not os.path.isfile(fout_name):
        f = open(fout_name, "w")
        f.close()
        print "File created: %s" % fout_name

    #//if not os.path.isfile(fout_name)

    fin         = open(fin_name, 'r')
    fout        = open(fout_name, 'r')
    lines_src       = list()
    lines_header    = list()

    regex = re.compile('^((\w|\s|\*)*\((\w|\s|\*)*\))$')

    """ prepare: lines_src """
    line = fin.readline()
    while line:
        result = regex.search(line)
        if result:

            lines_src.append(result.group().rstrip())
        line = fin.readline()

    

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

    """ show message """
    print "File written: %s" % fout_name

    """ close file """
    fin.close()
    fout.close()
#//create_header_file()

"""
create_header_file2()
<Parameters>

<Return>

<Descriptioins>
1. prepare: lines_src[]
2. prepare: lines_header[]
3. write: lines_header[]

<Notes>
1. Macro lines   => Ignored
"""
def create_header_file2():
    """  Steps
        1. Open the files
        2. Extract lines from the header file
        3. Extract lines from the source file
    """
    """ vars """
    if len(sys.argv) < 3:
        print "<Usage> util.py hd <source file>"
        sys.exit(0)

    fin_name   = sys.argv[2]

    fout_name   = "%s.h" % os.path.splitext(fin_name)[0]
    """ prepare: output file """
    if not os.path.isfile(fout_name):
        f = open(fout_name, "w")
        f.close()
        print "File created: %s" % fout_name

    #//if not os.path.isfile(fout_name)

    fin         = open(fin_name, 'r')
    fout        = open(fout_name, 'r')
    """ Arrays
    """
    lines_src       = list()    # lines from the source file
    lines_hdr       = list()    # lines from the header file
    lines_hdr_new   = list()    # lines for the new header file
    lines_hdr_comment   = list()
    lines_func_static   = list()
    lines_func_non_static   = list()
#    lines_hdr_macro   = list()
#    lines_hdr_func   = list()
    
    """ Regular expressions """
#    reg1 = re.compile('^((\w|\s|\*)*\((\w|\s|\*)*\))$') # functions
#    reg1 = re.compile('^((!struct)(\w|\s|\*)*\((\w|\s|\*)*\))$') # functions
#    reg_static      = re.compile('^static\s(\w|\s|\*)*;$') # static-type function
#    reg_static  = re.compile('^static\s(\w|\*|_)*\((\w|\s|\*|,)*\);$') # non static-type function
#    reg_static  = re.compile('^static\s(\w|\*)*\s(\w|_)\((\w|\s|\*|,)*\);$') # non static-type function
    reg_static  = re.compile('^static\s(\w|\*)*\s(\w|_)*\((\w|\s|\*|,)*\);$') # non static-type function
#    reg_non_static  = re.compile('^((\w|\s|\*|)*(\w|\s|\*|_)*\((\w|\s|\*|,)*\));$') # non static-type function
#    reg_non_static  = re.compile('^((\w|\s|\*|)*\s(\w|\s|\*|_)*\((\w|\s|\*|,)*\));$') # non static-type function
    reg_non_static  = re.compile('^((\w|\*)*\s(\w|\*|_)*\((\w|\s|\*|,)*\));$') # non static-type function
#    reg3 = re.compile('^\#(define|include|ifdef|endif)(\w|\s|\*)*$') # macro
    reg4 = re.compile('^((\w|\s|\*)*\((\w|\s|\*)*\));$')    # lines in the header file

    """ prepare: lines_src """
    lines_src = fin.readlines()
    lines_hdr = fout.readlines()
    lines_hdr = [line.rstrip() for line in lines_hdr]

    """ Extract the comment lines from the header """
    #debug
    print "fout.name=", fout.name

    for line in lines_hdr:
        if reg_static.search(line):
            #debug            
            print "line=", line
#//if reg_static.search(line)
#    for line in lines_hdr:
#        if not reg_static.search(line) or \
#                not reg_non_static.search(line):
##        if not reg_non_static.search(line) or \
##                not reg_static.search(line):
#            lines_hdr_new.append(line)

    #debug
    print "<lines_hdr_new>"
    print lines_hdr_new

    #for line in lines_hdr
#    for line in lines_src:
#        if reg1.search(line):   # append: function
#            lines_hdr_func.append(line)
##        elif reg2.search(line): # append: struct
#        if reg2.search(line): # append: struct
#            lines_hdr_struct.append(line)
##        elif reg3.search(line): # append: macro
##            lines_hdr_macro.append(line)

    #debug
#    print "<lines_hdr_func>"
#    print lines_hdr_func
#    print "<lines_hdr_struct>"
#    print lines_hdr_struct
#    print "<lines_hdr_macro>"
#    print lines_hdr_macro

#    """ Extract the comment lines from the header
#        1. Redefine: Regex
#        2.
#    """
#    """ Regular expressions """
#    reg1 = re.compile('^((\w|\s|\*)*\((\w|\s|\*)*\));$') # functions
#    reg2 = re.compile('^struct\s(\w|\s|\*)*;$') # struct
#    reg3 = re.compile('^\#(define|include|ifdef|endif)(\w|\s|\*)*$') # macro
#    reg4 = re.compile('^((\w|\s|\*)*\((\w|\s|\*)*\));$')    # lines in the header file
#
#    for line in lines_hdr:
#        if reg1.search(line) or \
#            reg2.search(line) or \
#            reg3.search(line) or \
#            reg4.search(line):
#                continue
#        else:
#            lines_hdr_new.append(line)


    #for line in lines_hdr

    """ close file """
    fin.close()
    fout.close()
#//create_header_file2()

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

                  copy_files(sys.argv[2])
            else:
                  print "sys.argv[2] is empty"
    elif sys.argv[1] == "hd":
#        create_header_file()
        create_header_file2()
