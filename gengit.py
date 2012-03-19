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
        gengit.py [options] [file name(s)]
            => execute
        gengit.py -h
            => show usage
    <Options>
        -a <pattern1> <pattern2> ...
            => add the patterns to the ".gitignore" file
            <Example> gitgen.py -a class tds exe
        -b
        -basic
            => create the default file
            => tds obj exe class pyc pyd etc
        -d  => Only dirs will be in the list
        -d1 => Only dirs will be in the list.
                No "*" expression added
        -e abc def
            => The files "abc" and "def" will not be
                in the ".gitignore" file
        -f  => Only files will be in the list
        -h  => Show help
        -n  => Name the ".gitignore" file
        -z  => Only display the list to be written.
                File will not be written.
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

def option_b():
    """ vars """
    ignore_list     = \
            ["tds", "obj", "exe", "class", "pyc", "pyd", "etc", "zip"]
    ignore_file     = ".gitignore"

    """ write to file """
    f = open(ignore_file, "w")
    for item in ignore_list:
        f.write("*.%s" % item)
        f.write("\n")

    """ report """
    print "File written: %s" % ignore_file

    """ exit """
    sys.exit(0)
#//option_b()

def start_job():
    """ vars """
    exempt_list     = list()    # items to be exempted
    target_list     = list()    # items to be gitignore-d
    ignore_file_name    = ".gitignore"
    flags = dict()
    flags["add-asterisk"]    = 1

    """ handle options """
    if len(sys.argv) > 1:
        if "-a" in sys.argv:    # add new patterns
            option_a()

#        if "-b" "-basic" in sys.argv or "-basic" in sys.argv:    # add new patterns
        if "-b" in sys.argv or "-basic" in sys.argv:    # add new patterns
#            #debug
#            print "[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
#            print "sys.argv=", sys.argv
#            sys.exit(0)
            
            option_b()

        if "-n" in sys.argv:
            ignore_file_name = option_n()

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
        pass
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
#    #debug
#    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
#    print sys.argv
#    if len(sys.argv) > 1:
#        print "sys.argv[1]=", sys.argv[1]
#        print "if sys.argv[1] == \"-h\"=", (sys.argv[1] == "-h")
#    else:
#        print "len(sys.argv)=", len(sys.argv)
#    sys.exit(0)

    start_job()
