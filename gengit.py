#!/usr/bin/python
# -*- coding: utf-8 -*-
####################################`
 # MyUtil.java
 # Author: Iwabuchi Ken                #
 # Date: 20120319_094131
 # Aim:                                #
 #     1.
 # <Usage>
 #    1. Run the program
 # <Source>
 #     1.
 ####################################/

import os
import sys
#import datetime
import inspect
#import getopt
import traceback
#import random
import re
#import win32api

#import lib

# variables ========================
VERSION = ["1.3", "2011/08/04 13:49:04"]

USAGE = """<<Usage>>

"""

# methods ========================
#def do_job(target_list=[], exempt_list=[]):
def do_job \
    (target_list=[], exempt_list=[], ignore_file_name=".gitignore", flags={}):
    """ vars """
    if not target_list == [] :
        dir_list = target_list
    else:
        dir_list        = \
            [x for x in os.listdir(os.getcwd())
            if not x in exempt_list] # list of dirs: OS separator
    #//if not target_list == []

    dir_list_git    = list()   # list of dirs: git separator
    fname           = ignore_file_name
    fout            = open(fname, "w")

    """ modify list
        => if the item is a dir, add "/*"
    """
    dir_list_new    = list()
    for item in dir_list:
        if os.path.isdir(item):
            if "-z" in sys.argv:
                print item
                if flags["add-asterisk"] == 1:
                    print os.path.join(item, "*")
            else:
                dir_list_new.append(item)
                if flags["add-asterisk"] == 1:
#                    #debug
#                    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
#                    print flags
#                    sys.exkt(0)
                    
                    dir_list_new.append(os.path.join(item, "*"))
            #//if "-z" in sys.argv
        else:
            if "-z" in sys.argv:
                print item
            else:
                dir_list_new.append(item)
            #//if "-z" in sys.argv
#            dir_list_new.append(item)

    """ replace the separator """
    if not "-z" in sys.argv:
    #    for item in dir_list:
        for item in dir_list_new:
            item_new = item.replace("\\", "/")
    #        dir_list_git.append(item_new)
    #        fout.write("%s\\n" % item_new)
            fout.write("%s" % item_new)
            fout.write('\n')
        """ message """
        print "File written: %s" % fname
    #//if not "-z" in sys.argv
#//def do_job

def show_usage():
    print """<<Usage>>
    <Syntax>
        gengit.py go
            => execute
        gengit.py [options] [file name(s)]
            => execute
        gengit.py [-h]
            => show usage
    <Options>
        -a <pattern1> <pattern2> ...
            => add the patterns to the ".gitignore" file
            <Example> gengit.py -a class tds exe
        -b
        -basic
            => create the default file
            => tds obj exe class pyc pyd etc
        -d  => Only dirs will be in the list
        -d1 => Only dirs will be in the list.
                No "*" expression added
        -d2 <Dir name>
            => Add directory
        -e abc def
            => The files "abc" and "def" will not be
                in the ".gitignore" file
        -f  => Only files will be in the list
        -h  => Show help
        -n  => Name the ".gitignore" file
        -z  => Only display the list to be written.
                File will not be written.
        -rm <File name>
            => Remove the file from the list
    """

#//show_usage()

#//do_job()

"""
    start_job()

"""

def option_a():
    if "-a" in sys.argv:    # add new patterns
        if not ".gitignore" in os.listdir(os.getcwd()):     # ".gitignore" exists?
            print "\".gitignore\" file doesn't exist."
            ans = raw_input("Create?(y/n)")
            if ans == "y":
                f = open(".gitignore", "w"); f.close()
            else:
                print "Program ends."
                sys.exit(0)
            #//if ans == "y"
#                sys.exit(0)
        #//if not ".gitignore" in os.listdir(os.getcwd())
        """ patterns designated?
            if yes,
            1. open the file
            2. write new patterns
            3. close the file
        """
        index = sys.argv.index("-a")
        if len(sys.argv) > index + 1:
#                #debug
#                print "[DEBUG:%d] " % inspect.currentframe().f_lineno
#                print sys.argv[(index + 1):]
#                sys.exit(0)
            f = open(".gitignore", "a")     # open the file
            for item in sys.argv[(index + 1):]:
                f.write("*.%s" % item)
                f.write("\n")
            """ report """
            print "New patterns written: %s" % ["*." + x for x in sys.argv[(index + 1):]]
        else:
            pass
#            #debug
#            print "[DEBUG:%d] " % inspect.currentframe().f_lineno
#            print
#            print "Option \"-a\" given. Patterns not given."
#            sys.exit(0)

        """ program ends """
        sys.exit(0)
        #//if "-a" in sys.argv

#//option_a()


def option_n():
    if "-n" in sys.argv:
        index = sys.argv.index("-n")
        if len(sys.argv) > index + 1:
            ignore_file_name = sys.argv[index + 1]
        else:
            print "We got \"-n\" option, but no file name designated."
            sys.exit(0)
    #//if "-n" in sys.argv

    return ignore_file_name
#//option_n()

#def option_b():
#def option_b(ignore_file=".gitignore"):
def option_b(ignore_file=".gitignore", flags={}):
    """ vars """
    ignore_list     = \
            ["tds", "obj", "i", "exe", "class", "pyc", "pyd", "etc", "zip"]
            #["tds", "obj", "exe", "class", "pyc", "pyd", "etc", "zip"]
#    ignore_file     = ".gitignore"

    if flags["display-only"] == 1:
        for item in ignore_list:
            print "*.%s" % item
    else:
        """ write to file """
        f = open(ignore_file, "w")
        for item in ignore_list:
            f.write("*.%s" % item)
            f.write("\n")
        """ ignore the .git dir """
        f.write(".git\n")
        f.write(".git/*\n")
    #//if flags["add-asterisk"] == 1

    """ report """
    print "File written: %s" % ignore_file

    """ exit """
    sys.exit(0)
#//option_b()

def option_d2():
    """ validate the length of argv """
    if len(sys.argv) < 3:
        print "Dir name missing"
        sys.exit(0)
    #//if len(sys.argv) < 3

    """ prepare: vars """
    target_dir = sys.argv[2]
    file_name = ".gitignore"

    """ processes
        1. Is dir?
    """
    """ is dir """
    if not os.path.isdir(target_dir):
        print "The argument is not a directory: %s" % target_dir
        sys.exit(0)
    #//if not os.path.isdir(sys.argv[2])

    """ open the file """
    try:
        f = open(file_name, "a")
        print "File opened: %s" % file_name
    except Exception, e:
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        traceback.print_exc()
#        e.print_exc()
        sys.exit(0)

    """ write to the file """
    f.write("%s/\n" % target_dir)
    print "%s/\n" % target_dir
    f.write("%s/*\n" % target_dir)
    print "%s/*\n" % target_dir

    """ close the file """
    f.close()
    print "File closed: %s" % file_name

#//option_d2()

def option_rm():
    """ validate the length of argv """
    if len(sys.argv) < 3:
        print "File name missing"
        sys.exit(0)
    #//if len(sys.argv) < 3

    """ prepare: vars """
    target_file = sys.argv[2]
    file_name = ".gitignore"
    lines_new   = list()
    flag        = False     # True if the target file is in ".gitignore"

    #debug
    print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
    print "target_file=", target_file

    """ processes
        1.
    """
#    """ is dir """
#    if not os.path.isdir(target_file):
#        print "The argument is not a directory: %s" % target_file
#        sys.exit(0)
#    #//if not os.path.isdir(sys.argv[2])

    """ open the file """
    try:
        f = open(file_name, "r")
        print "File opened: %s" % file_name
    except Exception, e:
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        traceback.print_exc()
#        e.print_exc()
        sys.exit(0)

    """ prepare: text """
    lines = f.readlines()

    """ close file """
    f.close()

    """ edit text """
#    lines_new = [line for line in lines if not line == target_file]

    #debug
#    print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
#    print "target_file=", target_file

    for line in lines:
        print "line=%s target_file=%s" % (line, target_file)
        if not line == target_file:
            lines_new.append(line)
            #debug
            print "\t", "line appended: %s" % line
        else:
            print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
            print "\t", "line: %s" % line
            print "\t", "target_file: %s" % target_file
            if flag == False: flag = True

    #debug
    print 
    print "------------------------------------"
    print lines_new
    print "------------------------------------"
    
    """ open file: write """
    f = open(file_name, "w")
    print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
    print "File opened: %s" % file_name

    """ write to the file """
    try:
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        print "------------------------------------- lines_new"
        for line in lines_new:
            print "line=", line
            f.write("%s\n" % line)
        print "-------------------------------------"
    except Exception, e:
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        traceback.print_exc()
#        e.print_exc()
        sys.exit(0)

    if flag == True:
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        print "The line removed: %s" % target_file
    else:
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        print "flag=", flag
        print "The given file is not in \".gitignore\""
    #//if falg == True
    
    """ close the file """
    f.close()
    print "File closed: %s" % file_name

#//option_rm()

def start_job():
    """ vars """
    exempt_list     = list()    # items to be exempted
    target_list     = list()    # items to be gitignore-d
    ignore_file_name    = ".gitignore"
    flags = dict()
    flags["add-asterisk"]    = 1
    flags["display-only"]    = 0

    """ handle options """
    if len(sys.argv) > 1 and sys.argv[1] == "go":
        pass
    elif len(sys.argv) > 1:
        if "-rm" in sys.argv:    # flags
            option_rm()
        if "-d2" in sys.argv:    # flags
            option_d2()
            sys.exit(0)
        if "-z" in sys.argv:    # flags
            flags["display-only"]    = 1
        if "-a" in sys.argv:    # add new patterns
            option_a()
        if "-n" in sys.argv:
            ignore_file_name = option_n()

#        if "-b" "-basic" in sys.argv or "-basic" in sys.argv:    # add new patterns
        if "-b" in sys.argv or "-basic" in sys.argv:    # add new patterns
#            #debug
#            print "[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
#            print "sys.argv=", sys.argv
#            sys.exit(0)
            
#            option_b()
#            option_b(ignore_file_name)
            option_b(ignore_file_name, flags)

#        if "-n" in sys.argv:
#            ignore_file_name = option_n()

        if sys.argv[1] == "-h":     # show usage
            print "[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
            show_usage()
            sys.exit(0)
        else:
            pass
#            #debug
#            print "[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
#            print "option \"-h\" is not given"
#            sys.exit(0)
#        #debug
#        print "[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
#        sys.exit(0)

        if "-e" in sys.argv:     # register exempt files
            exempt_list = sys.argv[2:]

        if "-d" in sys.argv:     # targets are dirs only
            if "-d1" in sys.argv:   # No "*" line. Flag add-asterisk will be 0
                flags["add-asterisk"] = 0
            target_list = [x for x in os.listdir(os.getcwd())
                        if os.path.isdir(x)]
        elif "-f" in sys.argv:     # targets are files only
            target_list = [x for x in os.listdir(os.getcwd())
                        if os.path.isfile(x)]

        if "-n" in sys.argv:     # designate the name of the file
            option_n()
    else:
        show_usage()
        sys.exit(0)
#        #debug
#        print "[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
#        sys.exit(0)

        pass
    #//if len(sys.argv) > 1

    """ do job """
#    do_job(target_list, exempt_list, ignore_file_name)
    do_job(target_list, exempt_list, ignore_file_name, flags)

#//start_job()

if __name__ == '__main__':
    #debug
#    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
#    print sys.argv
#    if len(sys.argv) > 1:
#        print "sys.argv[1]=", sys.argv[1]
#        print "if sys.argv[1] == \"-h\"=", (sys.argv[1] == "-h")
#    else:
#        print "len(sys.argv)=", len(sys.argv)
#    sys.exit(0)

    start_job()
