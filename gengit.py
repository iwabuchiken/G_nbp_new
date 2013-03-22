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

                    
                    dir_list_new.append(os.path.join(item, "*"))
            #//if "-z" in sys.argv
        else:
            if "-z" in sys.argv:
                print item
            else:
                dir_list_new.append(item)
            #//if "-z" in sys.argv

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
        -d3 => Add directories: Only unlisted ones
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

        #//if not ".gitignore" in os.listdir(os.getcwd())
        """ patterns designated?
            if yes,
            1. open the file
            2. write new patterns
            3. close the file
        """
        index = sys.argv.index("-a")
        if len(sys.argv) > index + 1:

            f = open(".gitignore", "a")     # open the file
            for item in sys.argv[(index + 1):]:
                f.write("*.%s" % item)
                f.write("\n")
            """ report """
            print "New patterns written: %s" % ["*." + x for x in sys.argv[(index + 1):]]
        else:
            pass

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

""" option_rm()
<Resource>
1. paper memo   => P.G.2b: 20120405_142420
"""

def option_rm():
    """ validate the length of argv """
    if len(sys.argv) < 3:
        print "File name missing"
        sys.exit(0)
    #//if len(sys.argv) < 3

    """ prepare: vars """
    target      = sys.argv[2]
    file_name   = ".gitignore"
    lines_original  = list()
    lines_new   = list()
    flag        = False     # True if the target file is in ".gitignore"

    """ processes
        1. ".gitignore" => exists?
        2. Open the file
        3. Read text from the file
        4. Close the file
        5. Prepare new text
        6. Reopen the file
        7. Write the new text into the file
        8. Report the result: Deleted the line?
        9. Close the file
        10. Exit
    """

    """ 1. ".gitignore" => exists? """
    if os.path.isfile(os.path.join(os.getcwd(), file_name)):
        #debug
        print os.path.join(os.getcwd(), file_name)
    else:
        #debug
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        print "\".gitignore\" doesn't exist."
        sys.exit(0)

    #//if os.path.isfile(os.path.join(os.getcwd(), file_name))

    """ 2. Open the file """
    try:
        f = open(file_name, "r")
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        print "File opened: %s" % file_name
    except Exception, e:
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        traceback.print_exc()

        sys.exit(0)

    """ 3. Read text from the file """
    lines_original = [line.rstrip() for line in f.readlines()]

    """ close file """
    f.close()

    """ 5. Prepare new text """

    for line in lines_original:
        if not line == target:
            lines_new.append(line)
            if flag == False:

                flag = True
        #//if not line == target:

    """ 6. Reopen the file """
    try:
        f = open(file_name, "w")
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        print "File opened: %s" % file_name
    except Exception, e:
        traceback.print_exc()
        sys.exit(0)

    """ 7. Write the new text into the file """
    try:
        for line in lines_new:
            f.write("%s\n" % line)        
    except Exception, e:
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        traceback.print_exc()

        sys.exit(0)

    """ 8. Report the result: Deleted the line? """
    if flag == True:
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        print "The line removed: %s" % target

    else:
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        print "flag=", flag
        print "The given file is not found in \".gitignore\""
    #//if falg == True
    
    """ 9. Close the file """
    f.close()
    print "File closed: %s" % file_name

    """ 10. Exit """
    sys.exit(0)

#//option_rm()

def option_d3():
    """ prepare: vars """
    target_list = list()
    file_name   = ".gitignore"
    lines_original  = list()
    lines_new   = list()
    flag        = False     # True if new line(s) written
    flags = dict()          # flags for "Add asterisk"
    
    """ processes
        1. ".gitignore" => exists?
        2. Open the file
        3. Read text from the file
        4. Close the file
        5. Prepare new text
        6. Reopen the file
        7. Write the new text into the file
        8. Report the result: Deleted the line?
        9. Close the file
        10. Exit
    """

    """ 1. ".gitignore" => exists? """
    if os.path.isfile(os.path.join(os.getcwd(), file_name)):
        #debug
        print os.path.join(os.getcwd(), file_name)
    else:
        #debug
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        print "\".gitignore\" doesn't exist."
        sys.exit(0)

    #//if os.path.isfile(os.path.join(os.getcwd(), file_name))

    """ 2. Open the file """
    try:
        f = open(file_name, "r")
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        print "File opened in \"r\": %s" % file_name
    except Exception, e:
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        traceback.print_exc()

        sys.exit(0)

    """ 3. Read text from the file """
    lines_original = [line.rstrip() for line in f.readlines()]

    """ close file """
    f.close()

    # message
    print "File closed: %s" % file_name

    """ 5. Prepare new text 
    1. Set flag: add-asterisk => 1
    2. Judge: A line in target_list[]
            => exist in lines_original[]?
                => (if no) Append the line to lines_original[]
                => (if yes) Next line (if exists)
    2. Flag is ?   => if false, return
    3. Open the file ".gitignore": mode => "w"
    4. target_list[] => write to the file
    5. Close the file
    """
    """ 1. Set flag: add-asterisk => 1 """
    flags["add-asterisk"] = 1
    target_list = [x for x in os.listdir(os.getcwd())
                    if os.path.isdir(x)]

    """ 2. Judge: A line in target_list[] """
    #debug
#    for line in lines_original:
#        print "line=", line

    for line in target_list:
        if not line in lines_original:
            lines_original.append(line)
            lines_original.append("%s/*" % line)

            #message
            print "A new line: %s" % line

            if flag == False:
                flag = True
            #//if flag == False
            #debug
#            print "line=", line
        #//if not line in lines_original
    #//for line in target_list:

    if flag == False:
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        print "No new directories"
        return
    #//if flag == False

    #debug
#    for line in lines_original:
#        print "line=", line

#        debug
#        print "line=", line
    """ 3. Open the file ".gitignore": mode => "w" """
    try:
        f = open(file_name, "w")
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        print "File opened in \"w\": %s" % file_name
    except Exception, e:
        print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
        traceback.print_exc()

        sys.exit(0)

    """ 4. target_list[] => write to the file """
    for line in lines_original:
        #debug
#        print "line=", line

        try:
            f.write("%s\n" % line)
            #message
#            print "Line written: %s" % line
        except Exception, e:
            print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
            traceback.print_exc()

            sys.exit(0)

    # message
    print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
    print "File written: %s" % file_name
            
    """ 5. Close the file """
    f.close()

    # message
    print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
    print "File closed: %s" % file_name

#//option_d3()

def start_job():
    """ vars """
    exempt_list     = list()    # items to be exempted
    target_list     = list()    # items to be gitignore-d
    ignore_file_name    = ".gitignore"
    flags = dict()
    flags["add-asterisk"]    = 1    # 1 => Add asterisk; 0 => No asterisk
    flags["display-only"]    = 0    # 1 => Dislay only; 0 => Generate file

    """ handle options """
    if len(sys.argv) > 1 and sys.argv[1] == "go":
        pass
    elif len(sys.argv) > 1:
        if "-rm" in sys.argv:    # flags
            option_rm()
        if "-d2" in sys.argv:    # flags
            option_d2()
            sys.exit(0)
        if "-d3" in sys.argv:    # flags
            option_d3()
            sys.exit(0)
        if "-z" in sys.argv:    # flags
            flags["display-only"]    = 1
        if "-a" in sys.argv:    # add new patterns
            option_a()
        if "-n" in sys.argv:
            ignore_file_name = option_n()

        if "-b" in sys.argv or "-basic" in sys.argv:    # add new patterns

            

            option_b(ignore_file_name, flags)

        if sys.argv[1] == "-h":     # show usage
            print "[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
            show_usage()
            sys.exit(0)
        else:
            pass

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

        pass
    #//if len(sys.argv) > 1

    """ do job """

    do_job(target_list, exempt_list, ignore_file_name, flags)

#//start_job()

if __name__ == '__main__':

    start_job()

#    #debug
#    print "\n[DEBUG:%d]\n" % inspect.currentframe().f_lineno;
#    ^(.*)(?:(?:\r?\n|\r)\1)+$