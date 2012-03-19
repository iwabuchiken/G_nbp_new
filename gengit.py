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
    (target_list=[], exempt_list=[], ignore_file_name=".gitignore"):
    """ vars """
    if not target_list == [] :
        dir_list = target_list
    else:
        dir_list        = \
            [x for x in os.listdir(os.getcwd())
            if not x in exempt_list] # list of dirs: OS separator
    #//if not target_list == []

#    #debug
#    print "dir_list=", dir_list
#    sys.exit(0)

#    dir_list        = [os.path.join(os.getcwd(), x, "*")
#                        for x in os.listdir(os.getcwd())] # list of dirs: OS separator
    dir_list_git    = list()   # list of dirs: git separator
#    fname           = ".gitignore"
    fname           = ignore_file_name
    fout            = open(fname, "w")

    """ modify list
        => if the item is a dir, add "/*"
    """
    dir_list_new    = list()
    for item in dir_list:
        if os.path.isdir(item):
#            #debug
#            print "item=", item
#            print "\t", os.path.join(item, "/*")
            if "-z" in sys.argv:
                print item
                print os.path.join(item, "*")
            else:
                dir_list_new.append(item)
                dir_list_new.append(os.path.join(item, "*"))
            #//if "-z" in sys.argv
#            dir_list_new.append(item)
#            dir_list_new.append(os.path.join(item, "*"))
#            dir_list_new.append(os.path.join(item, "/*"))
        else:
#            print item
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

def show_usage():
    print """<<Usage>>
    <Syntax>
        gengit.py [options] [file name(s)]
            => execute
        gengit.py -h
            => show usage
    <Options>
        -d  => Only dirs will be ignored
        -e abc def
            => The files "abc" and "def" will not be
                in the ".gitignore" file
        -f  => Only files will be ignored
        -z  => Only display the list to be written.
                File will not be written.
    """

#//show_usage()

#//do_job()

def start_job():
    """ vars """
    exempt_list     = list()    # items to be exempted
    target_list     = list()    # items to be gitignore-d
    ignore_file_name    = ".gitignore"

    """ handle options """
#    print sys.argv
#    sys.exit(0)
    if len(sys.argv) > 1:
        if "-n" in sys.argv:
            index = sys.argv.index("-n")
            if len(sys.argv) > index + 1:
                ignore_file_name = sys.argv[index + 1]
            else:
                print "We got \"-n\" option, but no file name designated."
                sys.exit(0)

        #//if "-n" in sys.argv
        if sys.argv[1] == "-h":     # show usage
            show_usage()
            sys.exit(0)
        elif sys.argv[1] == "-e":     # register exempt files
            exempt_list = sys.argv[2:]
        #//if sys.argv[1] == "-e"
        elif sys.argv[1] == "-d":     # targets are dirs only
            target_list = [x for x in os.listdir(os.getcwd())
                        if os.path.isdir(x)]
        elif sys.argv[1] == "-f":     # targets are files only
            target_list = [x for x in os.listdir(os.getcwd())
                        if os.path.isfile(x)]
        elif sys.argv[1] == "-n":     # designate the name of the file
            pass
        else:
            pass
        #//if sys.argv[1] == "-d"
    #//if len(sys.argv) > 1 and sys.argv[1] == "-h"

    """ do job """
    do_job(target_list, exempt_list, ignore_file_name)

#//start_job()

if __name__ == '__main__':
#    #debug
#    if "-n" in sys.argv:
#        index = sys.argv.index("-n")
#        if len(sys.argv) > index + 1:
#            print index, " : ", sys.argv[index + 1]
#        else:
#            print "We got \"-n\" option, but no file name designated."
#    #//if "-n" in sys.argv
#    sys.exit(0)

#    print sys.argv[1]

    start_job()
#    """ vars """
#    exempt_list     = list()    # items to be exempted
#    target_list     = list()    # items to be gitignore-d
#
#    """ handle options """
##    print sys.argv
##    sys.exit(0)
#    if len(sys.argv) > 1:
#        if sys.argv[1] == "-h":     # show usage
#            show_usage()
#            sys.exit(0)
#        elif sys.argv[1] == "-e":     # register exempt files
#            exempt_list = sys.argv[2:]
#        #//if sys.argv[1] == "-e"
#        elif sys.argv[1] == "-d":     # targets are dirs only
#            target_list = [x for x in os.listdir(os.getcwd())
#                        if os.path.isdir(x)]
#        elif sys.argv[1] == "-f":     # targets are files only
#            target_list = [x for x in os.listdir(os.getcwd())
#                        if os.path.isfile(x)]
#        else:
#            pass
#        #//if sys.argv[1] == "-d"
#    #//if len(sys.argv) > 1 and sys.argv[1] == "-h"
#
#    """ do job """
#    do_job(target_list, exempt_list)
