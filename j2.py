#!/usr/bin/python
# -*- coding: utf-8 -*-
"""************************************`
 * Q2.java
 * Author: Iwabuchi Ken				*
 * Date:
 * Aim:								*
 * 	1.
 * <Usage>
 *	1. Run the program
 * <Source>
 * 	1.
 ************************************"""
#from multiprocessing import join
import os.path
import os
import sys
import inspect

def get_java_path():
    """ get parameters """
    class_path  = sys.argv[1]   #   get the class path input

    """ split by "\" """
    ary1        = class_path.split("\\")
    
    """ split by "." """
    ary2        = ary1[-1].split(".")
    
    """ construct a path """
    if len(ary1) == 0:      # class file is in the current dir
        java_path   = ary2[0]

        #debug
        print "[%s:%d]" % (os.path.basename(__file__), 
                                        inspect.currentframe().f_lineno),
        print "java_path=", java_path

    elif len(ary1) == 1:    # class file is in the sub dir
        java_path   = ".".join((ary1[0], ary2[0]))
#        java_path   = ".".join((ary1, ary2[0]))

        #debug
        print "[%s:%d]" % (os.path.basename(__file__), 
                                        inspect.currentframe().f_lineno),
        print "java_path=", java_path

    elif len(ary1) == 2:     # class file is in the 2-or-more-order-below sub dir
        
        java_path   = ".".join((ary1[0], ary2[0]))
#        java_path   = ".".join((ary1[:-2], ary2[0]))
        
        #debug
        print "[%s:%d]" % (os.path.basename(__file__), 
                                        inspect.currentframe().f_lineno),
        print "java_path=", java_path

    elif len(ary1) > 2:     # class file is in the 2-or-more-order-below sub dir
#        tmp = ".".join(ary1[:-2])
        tmp = ".".join(ary1[:-1])
#        print "ary1[:-2]=", ary1[:-2]
#        print "ary1[:-1]=", ary1[:-1]
#        print "ary1[-1]=", ary1[-1]
#        print "ary1=", ary1
#        print "tmp=", tmp
        java_path   = ".".join((tmp, ary2[0]))
#        java_path   = ".".join((ary1[:-2], ary2[0]))

        #debug
        print "[%s:%d]" % (os.path.basename(__file__), 
                                        inspect.currentframe().f_lineno),
        print "java_path=", java_path
    else:
        print "[%s:%d]" % (os.path.basename(__file__), 
                                        inspect.currentframe().f_lineno),
        print "Sorry. The given path is not legible: %s" \
                % sys.argv[1]
#        print "ary1=%s(len=%d)" % (ary1, len(ary1))
#        print "ary2=%s(len=%d)" % (ary2, len(ary2))
        
        sys.exit(1)
    #//if len(ary1) == 1
#    java_path   = ".".join((ary1[-2], ary2[0]))

    """ return """
    return java_path
#//get_java_path()

def do_java():
    """ get java_path """
    java_path = get_java_path()

    """ get current path """
    cur_path = os.getcwd()

    """ build a command line """
    if len(sys.argv) > 2:
        cmd_line = "%s %s %s" % ("java", java_path, " ".join(sys.argv[2:]))
    else:    #len(sys.argv) > 2
        cmd_line = "%s %s" % ("java", java_path)
    #//if len(sys.argv) > 2
        #cmd_line = "%s %s" % ("java", java_path)
    #debug
    print "[%s:%d]" % (os.path.basename(__file__), 
                                        inspect.currentframe().f_lineno),
    print "cmd_line=", cmd_line

    #debug
    #sys.exit(0)

    """ execute java """
    os.system(cmd_line)
    
#//do_java()

if __name__ == '__main__':
    #debug
    #print "sys.argv=", sys.argv
    #sys.exit(0)
    
#    for item in sys.argv:
#        print item
#    sys.exit(0)
    
    #debug
#    print "__file__=", __file__
#    sys.exit(0)
    """
    javac
    1. if "-c" option given, execute "javac" 
    """
#    if len(sys.argv) > 1 and sys.argv[1] == "-c":
#        if len(sys.argv) < 3:       # if a package string not given
#            print "A package string not given."
#            sys.exit(0)
#        else:    #len(sys.argv) < 3
#            packages = sys.argv[2].split(".")
#            command = "javac %s" % os.path.join("\\".join(packages), sys.)
#        #//if len(sys.argv) < 3
#    else:    #len(sys.argv)
#    
#    #//if len(sys.argv)
#    
    do_java()

