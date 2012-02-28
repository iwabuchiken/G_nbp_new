#!/usr/bin/python
# -*- coding: %s -*-
#dir=%s
#file=v1u0
#created_at=%s

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

# variables ========================
"""
FULLEXEC:
    If set True, all the code will be executed, including
        those which are coded for individual execution.
DEBUG:
    Set True, debug info codes will be executed, such as
        showing exec line numbers (e.g. '[main.py:27]')
"""
#FULLEXEC = False
FULLEXEC = True
DEBUG = False
# methods ========================

def show_usage():
#    return """<<Usage>>
    print """<<Usage>>
    <Options>
    time
        show time label --> Ex: 20111127_123814
    -h
        show usage    
"""

#def generate_kw(length=10):
def get_time_label3():
  t = datetime.datetime.today()
  t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
  t2 = [str(item) for item in t1]

  for i in range(len(t2)):
    if len(t2[i]) < 2: t2[i] = "0" + t2[i]

  return "/".join(t2[:3]) + " " + ":".join(t2[3:])

def get_time_label2():
  t = datetime.datetime.today()
  t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
  t2 = [str(item) for item in t1]

  for i in range(len(t2)):
    if len(t2[i]) < 2: t2[i] = "0" + t2[i]
      
  return "".join(t2[:3]) + "_" + "".join(t2[3:])


def handle_args(optDict, optListA, optListB, optListC, dir_root):
    """
    <Options>
    -V <directory1[,directory2]>
      Backup all the files in the directory.
      Example: webdev_util.py -V control,view

    """
    # vars
    target_dirs = list()

    # handle options
    for key in optDict.keys():
        if key == "-V":
            target_dirs = optDict[key].split(",")
            flag = 0
            for target in target_dirs:
#                target_dir = os.path.join(dir_root, optDict[key])
                target_dir = os.path.join(dir_root, target)
                if not os.path.isdir(target_dir):
                    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
                    print "Directory doesn' t exist: %s" \
                        % target_dir
                    flag = 1
#                    sys.exit()
            if flag == 1: sys.exit(0)
            else:
                print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
                print "Start processing versioning on the directories: %s" \
                    % target_dirs
    return target_dirs

#//def handle_args(optDict, optListA, optListB, optListC, dir_root):

def get_opt():
    # preliminaries ==========================
    args = sys.argv[1:]

    """
    'optDict' => Contains string-bound options.
    'optListA' contains option chars which are declared as
        the string-less option.
    'optListB' for those args that have no option flags.
    'optListC' covers those option flags that are not registered
        in the program.
       """
    optDict = dict()
    optListA = list()
    optListB = list()
    optListC = list()
    i = 0
    """
       'flag' is used to indicate the error status in the option handling
           procedures.
       The key '1' indicates the number of incidents where string-bound
           option was given no corresponding value
       The key '2' for incidents where unregistered option character(s)
           was/were supplied in the parameter.
       """
    flag = {1:0, 2:0}

    """
       'opt_listA' is for those options which has corresponding values
           whereas 'opt_listB' handles those which doesn't.
       """
    opt_listA = "avsV"; opt_listB = "h"
    
    while (i < len(args)):
        """
        return:
            0 => no error
            1 => option doesn't have a corresponding string
            2 => unregistered option
        """
        if args[i][0] == "-":
            if args[i][1] in opt_listB:
                optListA.append(args[i])
                if (i+1) < len(args): i += 1
                else: break
            elif args[i][1] in opt_listA and (i+1) < len(args) :
                if args[i+1][0] == "-":
                    optDict[args[i]] = ""
                    i += 1
                else:
                    optDict[args[i]] = args[i+1]
                    if (i+2) < len(args):
                        """
                                 => Have used 2 args in the above line.
                                       So 'i' progress 2 steps
                               """
                        i += 2
                    else: break
                """
                        'args[i][1] in opt_listA'
                     => The last arg is declared as a string-bound option
                       Hence, the last arg being one of them, the corresponding value
                       is set as ""(empty).
                   """
            elif args[i][1] in opt_listA:
                optDict[args[i]] = ""
                flag[1] += 1
                break
            else:
                optListC.append(args[i])
                flag[2] += 1
                i += 1
        else:
            optListB.append(args[i])
            if (i+1) < len(args): i += 1
            else: break

    #debug
    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
    print "optDict=", optDict
    print "optListA=", optListA
    print "optListB=", optListB
    print "optListC=", optListC
    print "flag=", flag
#    sys.exit(0)

    return optDict, optListA, optListB, optListC, flag
#//def get_opt():

def set_util_dir(dir_root):
#    dir_root = os.getcwd()
    root_name = os.path.basename(dir_root)
    stor_dir_name = "STOR_%s" % root_name
    log_dir_name = "log_%s" % root_name
    tmp_dir_name = "tmp"

    dir_STOR = os.path.join(dir_root, stor_dir_name)
    dir_log = os.path.join(dir_root, log_dir_name)
    dir_tmp = os.path.join(dir_root, tmp_dir_name)

    if not (os.path.isdir(dir_STOR)):
        os.mkdir(dir_STOR)
        print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno,
        print "Dir created: %s" % stor_dir_name
    else: print "Dir exists: %s" % stor_dir_name
    if not (os.path.isdir(dir_log)):
        os.mkdir(dir_log)
        print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno,
        print "Dir created: %s" % log_dir_name
    else: print "Dir exists: %s" % log_dir_name
    if not (os.path.isdir(dir_tmp)):
        os.mkdir(dir_tmp)
        print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno,
        print "Dir created: %s" % tmp_dir_name
    else: print "Dir exists: %s" % tmp_dir_name
#//def set_util_dir():

def __check_util_dirs(target_dir_path):
    # STOR
    stor_dir_path = os.path.join(target_dir_path, "STOR_%s" % \
                            os.path.basename(target_dir_path))
    if not (os.path.isdir(stor_dir_path)):
        os.mkdir(stor_dir_path)
        print "Dir created: %s" % stor_dir_path
    else:
        print "Dir exists: %s" % stor_dir_path

def manage_versioning(target_dir_path, target_files):
    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno
    print "Start versioning"
    print "\t", "Target directory: %s" % target_dir_path
    print "\t", "Target files: %s" % target_files

    __check_util_dirs(target_dir_path)
#//def manage_versioning(target_dir_path, target_files)

def backup_dir(target_dirs, dir_root):
    for target_dir in target_dirs:
        target_dir_path = os.path.join(dir_root, target_dir)
        target_files = [x for x in os.listdir(target_dir_path)
                if os.path.isfile(os.path.join(target_dir, x))]

        manage_versioning(target_dir_path, target_files)

    #debug
    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno
    sys.exit(0)
        #debug
#        print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno
#        print "target_dir_path=", target_dir_path
#        print "target_files=", target_files

def create_project_dirs(project_root=os.getcwd()):
    """
    Functions:
        Create project dirs under the given directory.

    Vars:
        project_root    The directory under which to create dirs
        paths           Names of all the 4 project dirs
        path            Item in 'paths'
        fullpath        full path for 'path'; used in the for statement

    """
    paths = ['control', 'view', 'tools', 'db']

    for path in paths:
#        fullpath = os.path.isdir(os.path.join(project_root, "control"))
        fullpath = os.path.join(project_root, path)
        if not (os.path.isdir(fullpath)):
            try:
                os.mkdir(fullpath)
                print "Dir created: %s" % fullpath
            except Exception, e:
                traceback.print_exc()
        else: print "Dir exists: %s" % fullpath

#def copy_file(fullpath_dst_file, fin_name, item, page_templ_path, project_root, dir_name):
def copy_file(fullpath_src_file, fullpath_dst_file):
    """
    Description:
        1. Called from def 'create_pages()'
    Vars:
        fullpath_src_file
        fullpath_dst_file
    """
    if os.path.isfile(fullpath_dst_file):
        print "File exists: %s" % fullpath_dst_file
    else:
        print "Page creating...: %s" % fullpath_dst_file
        try:
            fin = file(fullpath_src_file, "r")
            fout = file(fullpath_dst_file, "w")
        except Exception, e:
            traceback.print_exc()
        try:
            shutil.copyfile(fullpath_src_file, fullpath_dst_file)
            print "File created:"
            print "\t", fullpath_dst_file
        except Exception, e:
            traceback.print_exc()

        fin.close()
        fout.close()

#//def copy_file

def create_lib(project_root, page_names, webpage_templates_dir):
    """
    Vars:
        content                 content of the input file   <str>
        fin                     file object <file>
        fout                    file object <file>
        fin_name
        fout_name
        fullpath_fin
        fullpath_fout
        item                    receiver for 'for' statement
        kw_set                  dictionary of replacements  <dict>
        project_root
        page_names
        TEMPLATE_FILE           string of variable for control files   <str>
        VAR_LIST_CONTROL        string of variables for control files   <str>
        webpage_templates_dir

    Flow:
        1. Open files
        2. Read
        3. Replace strings
        4. Write
        5. Close files
    """
    #01
    fin_name = "lib.php"
    fout_name = "lib.php"
    fullpath_fin = os.path.join(webpage_templates_dir, fin_name)
    fullpath_fout = os.path.join(project_root, "control", fout_name)
    fin = open(fullpath_fin, "r")
    fout = open(fullpath_fout, "w")

    #02
    content = fin.read()

    #03 Replace
    VAR_LIST_CONTROL = ""
    VAR_LIST_VIEW = ""
    for item in page_names:
        VAR_LIST_CONTROL += \
                (" " * 4 + "$cnt_%s = \"%s.php\";" + "\n") % (item, item)
#                ("\s"*4 + "$cnt_%s = \"%s.php\";" + "\n") % (item, item)
        VAR_LIST_VIEW += \
                (" " * 4 + "$tpl_%s = \"%s.tpl.php\";" + "\n") % (item, item)
#        TEMPLATE_FILE = "join(DIRECTORY_SEPARATOR, array (%s, \"view\", $cnt_%s))" \
#                    % (project_root, item)
    kw_set = {
        "@VAR_LIST_CONTROL@": VAR_LIST_CONTROL,
        "@VAR_LIST_VIEW@": VAR_LIST_VIEW,
#        "@TEMPLATE_FILE@": TEMPLATE_FILE
    }
    content = content.replace("@VAR_LIST_CONTROL@", VAR_LIST_CONTROL)
    content = content.replace("@VAR_LIST_VIEW@", VAR_LIST_VIEW)
#    content = content.replace("@TEMPLATE_FILE@", TEMPLATE_FILE)

    #04 Write
    try:
        fout.write(content)
        print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
        print "File created: %s" % fullpath_fout
    except Exception, e:
        traceback.print_exc()
        
    #05 Close
    fin.close()
    fout.close()

#//def create_lib

def create_pages(project_root=os.getcwd(), page_names=[
                'main', 'show_db', 'add_db', 'show_tables',
                'add_table', 'show_data', 'add_data', 'report_addition']):
    """
    Vars:
        content             content of the input file
        dir_name            individual directory name: e.g. 'control'
        dirs
        flag                Set to '1' if the the project dirs do not exist
        fin                 Input file object
        fout                Output file object
        fin_name            Input file name
        fout_name           Output file name
        fin_fullpath        Full path of the input file
        fout_fullpath       Full path of the output file
        kw_set              key-value dictionary for replacement    <dict>
        page_templ_path     path to template page directory
        project_root
        TEMPLATE_FILE       string for 'require' in the control file    <str>
        webpage_root        Dirname of pages under 'nbp' dir
#        target_file_name    Target file name in 'webpage_templates'
#                            e.g. 'view.tpl.php'
    Flow:
        1. Check if the project dirs exist.
        2. Create pages
            1. control
        3. Create: lib.php ==> 'control' directory
    """
    #01
    dirs = ['control', 'view', 'tools', 'db']
    flag = 0
    for item in dirs:
        fullpath = os.path.join(project_root, item)
        if not os.path.isdir(fullpath):
            print "Dir does not exist: %s" % fullpath
            flag = 1
        else: print "Dir exists: %s" % fullpath
    if flag == 1: sys.exit(0)

    #02
    webpage_root = os.path.dirname(inspect.getfile(inspect.currentframe()))
        #=> script from: http://stackoverflow.com/questions/50499/in-python-how-do-i-get-the-path-and-name-of-the-file-that-is-currently-executin

    for item in page_names:
        for directory in ["control", "view"]:
            #01 open file
            if directory == "view":
                fin_name = "%s.tpl.php" % directory
                fout_name = "%s.tpl.php" % item
            else:
                fin_name = "%s.php" % directory
                fout_name = "%s.php" % item

            fullpath_src_file = os.path.join(
                            webpage_root, "webpage_templates", fin_name)
            fullpath_dst_file = os.path.join(project_root, directory, fout_name)
            fin = open(fullpath_src_file, "r")
            fout = open(fullpath_dst_file, "w")

            # Read content
            content = fin.read()

            # Replace
            TEMPLATE_FILE = "join(DIRECTORY_SEPARATOR, array ($dir_root, \"view\", $tpl_%s))" \
                        % item
            FILE_NAME = os.path.basename(fullpath_dst_file)
            CREATED_AT = get_time_label3()
            VERSION = "1.0"
            kw_set = {
                "@TEMPLATE_FILE@": TEMPLATE_FILE,
                "@FILE_NAME@": FILE_NAME,
                "@CREATED_AT@": CREATED_AT,
                "@VERSION@": VERSION,
            }
            for key in kw_set.keys():
                content = content.replace(key, kw_set[key])
#                content = content.replace("@TEMPLATE_FILE@", TEMPLATE_FILE)

            # Write
            try:
                fout.write(content)
            except Exception, e:
                traceback.print_exc()

            # Close file
            fin.close()
            fout.close()
#            copy_file(fullpath_src_file, fullpath_dst_file)

    #03 lib.php
    create_lib(project_root, page_names, 
            webpage_templates_dir=os.path.join(webpage_root, "webpage_templates"))

#//def create_pages

def do_main():
    """
    Vars:
        dir_root        Root directory of the project
    """
    # set vars =============================
    dir_root = os.getcwd()

    # 00 =============================
    """
    If no argument given(i.e. 'len(sys.argv) < 2'),
        the program understands that the user requires
        to show the help message.
    """
    if len(sys.argv) < 2 or sys.argv[1] == "-h":
        show_usage()
        sys.exit(0)

    # 00-2 ============================
    """
    If the first argument is the constant string 'time',
        the program shows the current time string.
    """
    if sys.argv[1] == "time":
        print "\t", get_time_label2()
        sys.exit(0)

    # 00-3 ================================
    """
    The first argument being 'md', the program creates
        the 4 project directories, which are, 'control',
        'view', 'tools' and 'db'.
    """
    if sys.argv[1] == "project":
        create_project_dirs()
    
    # 00-4 ================================
    """
    The first argument: 'create'; the second one 'pages',
        then the program creates pages with the name given in
        the 3rd argument
    Example: >>create pages abc,def
        => Creates 3 x 2 pages with names 'abc.php', 'abc.tpl.php',
            'def.php', 'def.tpl.php'
    """
    """
    The below 'if' condition given, for the following line is
        supposed to be execu
    """
    if (FULLEXEC == True):
        create_pages()
    """
    If both the arguments given and the first one not being
        'time', then the program moves on to handle options.
    """
    
    # 01 handle options ================
    if len(sys.argv) >= 2:
        optDict, optListA, optListB, optListC, flag = get_opt()

    # 02 set STOR directory =======================
    """
    Next, the program prepares the util directories, which are,
        'log', 'STOR' and 'tmp'.
    """
    set_util_dir(dir_root)

    #debug
#    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
#    print dir_STOR
#    sys.exit(0)

    # 03 =======================
    target_dirs = handle_args(optDict, optListA, optListB, optListC, dir_root)

    # ==================================
    if DEBUG == True:
        if len(target_dirs) > 0:
            backup_dir(target_dirs, dir_root)

    #debug
#    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
#    sys.exit()

if __name__ == '__main__':
    do_main()
    
"""
    #debug
    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
    sys.exit()
"""
