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
    lines_func          = list()
    lines_func_static   = list()
    
    """ Regular expressions """
#    reg_func1        = re.compile('^((\w|\*)*\s*(\w|\*|_)*\((\w|\s|\*|,)*\));$') # function
    reg_func1        = re.compile('^((\w|\*)*\s*(\w|\*|_)*\((\w|\s|\*|,|\[|\])*\));$') # function
#    reg_func2        = re.compile('^((\w|\*)*\s(\w|\*)*\s(\w|\*|_)*\((\w|\s|\*|,)*\));$') # function2
#    reg_func2        = re.compile('^((\w|\*)*\s*(\w|\*)*\s*(\w|\*|_)*\((\w|\s|\*|,)*\));$') # function2
    reg_func2        = re.compile('^((\w|\*)*\s*(\w|\*)*\s*(\w|\*|_)*\((\w|\s|\*|,|\[|\])*\));$') # function2
    reg3             = re.compile('^//.+$')     # "//prototypes" lines
    reg_func_static = re.compile('^static') # static-type function

    """ prepare: lines_src """
    lines_src = [line.rstrip() for line in fin.readlines()]
    lines_hdr = [line.rstrip() for line in fout.readlines()]

    """ Extract the comment lines from the header
    1. Extract the commments
    2. Close the file
    """
    #debug
    print "fout.name=", fout.name

    for line in lines_hdr:      # Extract lines other than function lines
        if not reg_func1.search(line):
            if not reg_func2.search(line):
                if not reg3.search(line):
                    lines_hdr_new.append(line)

    # 2. Close the file
    fout.close()

    #debug
    print "<lines_hdr_new>"
    print lines_hdr_new
    print 

    """ Extract function signitures from the source
    1. Redefine regexes
    2. Search
    3. Sort the results
    """
    # 1. Redefine regexes
#    reg_func1        = re.compile('^((\w|\*)*\s(\w|\*|_)*\((\w|\s|\*|,)*\))$') # function
#    reg_func2        = re.compile('^((\w|\*)*\s(\w|\*)*\s(\w|\*|_)*\((\w|\s|\*|,)*\))$') # function2
    reg_func1        = re.compile('^((\w|\*)*\s(\w|\*|_)*\((\w|\s|\*|,|\[|\])*\))$') # function
    reg_func2        = re.compile('^((\w|\*)*\s(\w|\*)*\s(\w|\*|_)*\((\w|\s|\*|,|\[|\])*\))$') # function2
    reg_func_static = re.compile('^static') # static-type function

    # 2. Search
    for line in lines_src:
        if reg_func1.search(line) or reg_func2.search(line):
            if reg_func_static.search(line):
                lines_func_static.append(line)
            else:
                lines_func.append(line)

    # 3. Sort the results
    lines_func_static.sort()
    lines_func.sort()

    """ Write to the header file
    0. Edit lines_hdr_new
    1. Reopen the header file
    2. Write
    3. Close the file
    """
    # 0. Edit lines_hdr_new
    lines_hdr_new = [line for line in lines_hdr_new if not line == '']

    # 1. Reopen the header file
    fout        = open(fout_name, 'w')

    # 2. Write
    try:
        for line in lines_hdr_new:  # comment lines
            fout.write("%s\n" % line)
        #for line in lines_hdr_new
        fout.write("\n//prototypes: static =========================\n")
        for line in lines_func_static:  # funcs: static
            fout.write("%s;\n" % line)
        #for line in lines_func_static
        fout.write("\n//prototypes: non-static =========================\n")
        for line in lines_func:         # funcs: non-static
            fout.write("%s;\n" % line)
        #for line in lines_func
    except Exception, e:
        print "\n[DEBUG:%d]" \
                        % inspect.currentframe().f_lineno;
        traceback.print_exc()
        sys.exit(0)
    print "\n[DEBUG:%d]" \
                        % inspect.currentframe().f_lineno;
    print "File written: %s" % fout.name
    #//try

    # 3. Close the file
    fout.close()

    #debug
#    print "<lines_func_static>"
#    print lines_func_static
##    print lines_func_static.sort()
#    print "<lines_func>"
##    print lines_func
#    lines_func.sort()
#    print lines_func
    
    """ close file """
    fin.close()
    fout.close()
#//create_header_file2()

def show_usage():
    print """<< Usage >>
    <Options>
        ap [current dir path]
                1. Configure Apache
                2. 'ap' only => The current path in the file will be used
                3. The new path => You will be asked after running the program
        -h      Show usage
        sub     Create subversion folders
        cp      Copy files
                ex: util2.py cp c
                => copy default C files
        hd      Create header file
                ex: util2.py hd sub1.c
                => Create a header file from sub1.c
        len <string>
                => Show the length of <string>
                ex. util2.py len http://abc.org
                    => 14
    """

#//show_usage()

def show_string_length(args):
    """ validate arguements """
    if len(args) < 3:
        print "Input the string. Your input: ", args
        sys.exit(0)
    #//if len(args) < 3

    """ Show length """
    print "Given string: ", args[2]
    print "\t", "Length: ", len(args[2])

    """ Closing """
    sys.exit(0)
#//show_string_length()

def config_apache():
#    #debug
#    print "\n[DEBUG:%d]" \
#                            % inspect.currentframe().f_lineno
#    print "len(sys.argv)=", len(sys.argv)
#    sys.exit(0)
    
    """ Procedure
        1. Set up
        2. Replace 
            1) 'DocumentRoot' value
            2) 'Directory' directive
        3. Close and reopen the conf file
        4. Write the new content to the file
    """
    
    """ 1. Set up *********************************************
            1) Set the current doc root path
            2) Set the new doc root path
            3) Open the config file
            4) Read the content
            
    """
    
    """ 1) Set the current doc root path
            => If the second arguement given, set the arguement
                    as the current root path
    """
    """ the current doc root path """
    current_path = ""
    
    if len(sys.argv) > 2:
        current_path = sys.argv[2]
    else:
        current_path = "C:/xampp2/htdocs"
    #//if len(sys.argv) > 2
    
    """ 2) Set the new doc root path """
    print "Input the new document root path: ",
    new_string = raw_input()    # the new doc root path
    
    """ open the config file """
    file_path = r"C:\xampp2\apache\conf\httpd.conf"    # file path for the config file
    config_file = open(file_path, "r")      # file object
    #config_file = open(current_path, "r")      # file object
    
    """ read the content """
    file_content = config_file.readlines()  # content of the config file
    
    """ 2. Replace the 'DocumentRoot' value *********************
    """
    
    """ setup the regular expression """
    reg1 = re.compile("^DocumentRoot \"(.*)\"")
    #reg2 = re.compile("^<Directory \"(C:/xampp2/htdocs)\">")
    reg2 = re.compile("^<Directory \"(%s)\">" % current_path)
    
    #debug
    print "\n[DEBUG:%d]" \
                            % inspect.currentframe().f_lineno
    print "reg2=", "^<Directory \"(%s)\">" % current_path
    
    #debug
    print "\n[DEBUG:%d]" \
                            % inspect.currentframe().f_lineno
    print "current_path=", current_path
    
    
    
    """ setup variables """
    line_counter = 0        # line number of the file content
    new_content = list()    # content for the new file
    
    """ search for the line """
    for line in file_content:
        if reg1.search(line):
            """ increment the counter """
            line_counter += 1
            
            """ show the original line """
            print "\n[DEBUG:%d]" \
                                    % inspect.currentframe().f_lineno
            
            print "Original=", line            
            
            """ replace the string """
            line = line.replace(reg1.search(line).group(1), new_string)
            
            """ show the new line """
            print "\n[DEBUG:%d]" \
                                    % inspect.currentframe().f_lineno
            print "New line=", line
            
        elif reg2.search(line): # if reg2.search(line)
            """ increment the counter """
            line_counter += 1
            """ show the original line """
            print "\n[DEBUG:%d]" \
                                    % inspect.currentframe().f_lineno
            
            print "Original=", line            
            
            """ replace the string """
            line = line.replace(reg2.search(line).group(1), new_string)
            
            """ show the new line """
            print "\n[DEBUG:%d]" \
                                    % inspect.currentframe().f_lineno
            print "New line=", line
        else:
            """ increment the counter """
            line_counter += 1

        """ append the new line  """
        new_content.append(line)
        #//if reg1.search(line)
    #//for line in file_content:
    
    """ 4. Close and reopen the conf file ***************************** 
    """

    """ Close and reopen the file """
    config_file.close()
    
    """ Reopen the file """
    try:
        config_file = open(file_path, "w")      # file object
    except IOError, e:
        #debug
        print "\n[DEBUG:%d]" \
                                % inspect.currentframe().f_lineno;
        traceback.print_exc()
        sys.exit(1)
    
    """ 5. Write the new content to the file
    """
    """ Write to the file """
    try:
        config_file.write("".join(new_content))
        print "File written: ", os.path.dirname(file_path)
        
    except Exception, e:
        traceback.print_exc()
        
    finally:
        config_file.close()
#//def config_apache()

def dispatch():
    """ commands
        1. Show usage
        2. Create subversion folders
        3. Copy basic files: java
    """
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

    """ Show string length """
    if sys.argv[1] == "len":
            show_string_length(sys.argv)

    """ Configure Apache """
    if sys.argv[1] == "ap":
        config_apache()
    #//if sys.argv[1] == "ap"
#//dispatch()

if __name__ == '__main__':
    # 00 =============================
    dispatch()

#    """ Show usage """
#    if len(sys.argv) < 2 or sys.argv[1] == "-h":
#        show_usage()
#        sys.exit(0)
#
#    """ Create subversion folders """
#    if sys.argv[1] == "sub":
#            create_subversin_folders(sys.argv)
#
#    """ Copy basic files: java """
#    if sys.argv[1] == "cp":
#            if len(sys.argv) > 2:
#
#                  copy_files(sys.argv[2])
#            else:
#                  print "sys.argv[2] is empty"
#    elif sys.argv[1] == "hd":
##        create_header_file()
#        create_header_file2()
