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

#
import platform

# variables ============s============
VERSION = ["3.0", "2011/07/31-13:43:16"]

USAGE = """<<Usage>>
    <Options>
    cf
      Copy files
    md <option>
        make subdirs in the current directory
        <option>
            * => log, STOR_XXX
            sub1,sub2 => sub1, sub2 (delimited by a single comma, ',')
            sub1  => sub1
        <Example>
            util.py md log,etc => create two new dirs, 'log' and 'etc'
                                    under the current dir.
    recal
        recalibrate version signiture
    time
        show time label --> Ex: 20111127_123814
    t2
        show time label --> Ex: 2013/03/23 07:45:27
    -h
        show usage
    -J
        make jar file
                Add "~~"(double childer) at the tail of the file name
                to avoid versioning processing
                Ex: -vcomment.bat,util.py~~ -J
                    => "util.py" will not be versioned. Just Jar-nized.
        -j
                Add comment to jar file. Use "" for multiple words sentences
                Ex: -j"Nice hot garbage!"
    -k<number>
        generate passowrds with <number> of chars
        => Ex: "-k10" ---> "0eR705FIx6"
        
        -ka10
        	=> "ejcihhbjbf"	Small letters only
        
        -kA10
        	=> "GGGJFAABEB"	Capital letters only
        	
        -kn10
        	=> "5129482724"	Numbers only
        
        -kxa1n3
        	=> "g472"	Set format
        	
    -L<file name>
        name of the file for logging
    -T<sentences>
        Sentences to be written into the log file
        Use quotation if space char involved
    -v<file_name(trunk)>
        versioning
        <Option>
        * => All the files in the current dir
        *~~ => Jar all the files in the current dir. No versioning.
        <Example>
        util.py -v* -J
                => Version all the file, and jar them all.
        util.py -v*~~
                => Jar them all. No versioning.
    <Example>
    util.py -Lmain.py -T"Edit: func: do_job()"
"""

# methods ========================
def get_usage():
    return USAGE

def _handle_x_opion(option):
      """
      Desc:
      Params:
      Vars:
            kw => generated keyword <str>
            target => option string <str>
            res1 => list
            res2 => list
      """
      kw = ""; target = option[1:]
      r1 = re.compile('[a-zA-Z]{1}')
      r2 = re.compile('[0-9]+')
      res1 = r1.findall(target)
      res2 = r2.findall(target)

      #debug
      print len(res1)

      # generate keyword
      for i in range(len(res1)):
#            print generate_kw(int(res2[i]), res1[i])
            kw += generate_kw(int(res2[i]), res1[i])
#            kw += generate_kw(res2[i], res1[i])

      print res1
      print res2
      print "kw=", kw

      #debug
#      print option
#      print res1
#      print res2
#      print "len(res1)=", len(res1)
#      print "len(res2)=", len(res2)
      
#//_handle_x_opion(option)

#def generate_kw(length=10):
def generate_kw(length=10, option='all'):
      """
      Description:
            Generate keyword
      Parameters: 'option'
            all => Mix of a-z,A-Z,0-9
            a => a-z
            A => A-Z
            x => Given format
                  Ex:   xa1n3 => p371
                        xn3a2n2 => 327cr21
      Vars:
            chars: a-z <str>
            chars_l: list of 'chars' <list>
            nums: 0-9
            nums_l: list of 'nums' <list>
            kw: Generated keyword <str>
            random_char
      Return:

      """
      chars = "abcdefghijklmnopqrstuvwxyz"
      chars_l = [item for item in chars]
      nums = "1234567890"
      nums_l = [item for item in nums]
      specials = ";+*[]()#$%&"
      specials_l = [item for item in specials]
      kw_len = length
      kw = ""

      # option: all
      if option == 'all':
      	for i in range(kw_len):
      		flag = random.randint(1,3)
      		if flag == 1: kw += chars_l[random.randint(0, len(chars_l)-1)]
      		elif flag == 2: kw += chars_l[random.randint(0, len(chars_l)-1)].upper()
      		elif flag == 3: kw += nums_l[random.randint(0, len(nums_l)-1)]
      # option: 'n'
      elif option == 'special':
      	for i in range(kw_len):
      		flag = random.randint(1,4)
      		if flag == 1: kw += chars_l[random.randint(0, len(chars_l)-1)]
      		elif flag == 2: kw += chars_l[random.randint(0, len(chars_l)-1)].upper()
      		elif flag == 3: kw += nums_l[random.randint(0, len(nums_l)-1)]
      		elif flag == 4:
                        while(1):
                              random_char = \
                                    specials_l[
                                                random.randint(0, len(nums_l)-1)]
#                              if not random_char == kw[-1]: break
                              if not random_char in kw: break
                        kw += random_char
      # option: 'n'
      elif option.lower()[0] == 'n':
      	if len(option) > 1:
      		for i in range(int(option.lower()[1:])):
      			kw += nums_l[random.randint(0, len(nums_l)-1)]
      	else:
      		for i in range(kw_len):
      			kw += nums_l[random.randint(0, len(nums_l)-1)]
      # option: 'a'
      elif option == 'a':
      	for i in range(kw_len):
      		kw += chars_l[random.randint(0, len(nums_l)-1)]
      # option: 'A'
      elif option == 'A':
      	for i in range(kw_len):
      		kw += chars_l[random.randint(0, len(nums_l)-1)].upper()
    # option: 'x'
      elif option[0] == 'x':
      	kw = _handle_x_opion(option)

      #debug
      print kw

      return kw

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

def get_time_label2_span_v1(t1, t2):
    #
    a = t1.split("_")[1]
    b = t2.split("_")[1]
    
    a1 = a[0:2]; a2 = a[2:4]; a3 = a[4:6];
    b1 = b[0:2]; b2 = b[2:4]; b3 = b[4:6];
    
    # Seconds
    c3 = int(b3) - int(a3)
    
    if c3 < 0:
#        c3 = int(a3) - int(b3)
        c3 = int(b3) + 60 - int(a3)
        
#        if int(b2) < 1:
#            b1 = str(int(b1) - 1)
#            b2 = "59"
#        else:
        b2 = str(int(b2) - 1)
    else:
        c3 = int(b3) - int(a3)
    
    print b2, " ", c3
#    puts b2

    # Minutes
    c2 = int(b2) - int(a2)
    
    print "c2=", c2
    
    if c2 < 0:
        print "c2 < 0"
        c2 = (int(b2) + 60) - int(a2)
        
        b1 = str(int(b1) - 1)

    print b1, " ", c2, " ", c3
    print int(b1) - int(a1), " ", c2, " ", c3
#//def get_time_label2_span()

def get_time_label2_span(t1, t2):
    #
    a = t1.split("_")[1]
    b = t2.split("_")[1]
    
    a1 = a[0:2]; a2 = a[2:4]; a3 = a[4:6];
    b1 = b[0:2]; b2 = b[2:4]; b3 = b[4:6];

#    print "a=%s:%s:%s" % (a1, a2, a3)
#    print "b=%s:%s:%s" % (b1, b2, b3)

    ia1 = int(a1); ia2 = int(a2); ia3 = int(a3);
    ib1 = int(b1); ib2 = int(b2); ib3 = int(b3);
    
    ic1 = ic2 = ic3 = 0
    
    # Seconds
    ic3 = ib3 - ia3

#    print "ia1=%d ia2=%d ia3=%d" % (ia1, ia2, ia3)
#    print "ib1=%d ib2=%d ib3=%d" % (ib1, ib2, ib3)

    if ic3 < 0:
#        ic3 = ia3 - ib3
        ic3 = ib3 + 60 - ia3
        ib2 = ib2 - 1

#    print
#    print "ia1=%d ia2=%d ia3=%d" % (ia1, ia2, ia3)
#    print "ib1=%d ib2=%d ib3=%d" % (ib1, ib2, ib3)
#    print "ic1=%d ic2=%d ic3=%d" % (ic1, ic2, ic3)

    # Minutes
    ic2 = ib2 - ia2
    
    if ic2 < 0:
        ic2 = ib2 + 60 - ia2
        ib1 = ib1 - 1

#    print
#    print "ia1=%d ia2=%d ia3=%d" % (ia1, ia2, ia3)
#    print "ib1=%d ib2=%d ib3=%d" % (ib1, ib2, ib3)
#    print "ic1=%d ic2=%d ic3=%d" % (ic1, ic2, ic3)
    
    # Hours
    ic1 = ib1 - ia1
    
#    print
#    print "ic1=%d ic2=%d ic3=%d" % (ic1, ic2, ic3)
    
    # Modify length
    c1 = c2 = c3 = ""
    
    c1 = str(ic1)
    
    if len(str(ic3)) < 2:
        c3 = "0" + str(ic3)
    else:
        c3 = str(ic3)
    
    if len(str(ic2)) < 2:
        c2 = "0" + str(ic2)
    else:
        c2 = str(ic2)
    
    return "%s:%s:%s" % (c1, c2, c3)
#//def get_time_label2_span()

def handle_STOR_dir(dir_name):
	print "./STOR_%s" % dir_name
	if os.path.isdir("./STOR_%s" % dir_name) == False:
		os.mkdir("STOR_%s" % dir_name)
		print "STOR dir created"
	else: print "STOR directory exists."

def handle_version_file(dir_name, target_file, list):
    """
    list: os.listdir()
    target_file: Ex: main.py
    """
    reg = re.compile("^version~%s" % target_file)

    flag = 0
    for item in list:
        if reg.search(item):  # if version file exists
            print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
            print "Version file exists: %s" % item
            flag = 1          # turn the flag to 1
            version_file = item
            break

    if flag == 0: # if the version file doesn't exist
        f = file("./STOR_%s/version~%s=1.0" % (dir_name, target_file), "w")
        version_file = "version~%s=1.0" % target_file
        print "New file created: ./STOR_%s/%s" % \
                (dir_name, version_file)
        f.close()

    return version_file

def get_version_number(version_file):
	version_num = version_file.split("=")[1]
	ver = version_num.split(".")[0]
	update = version_num.split(".")[1]

	return version_num, ver, update

def copy_files(target_file, dir_name, ver, update):
#	items = target_file.split(".")
	trunk, ext = os.path.splitext(target_file)
#	if len(items) > 1:
	if len(ext) > 0:
#		copy_name = "%s~v%su%s.%s" % (trunk, ver, update, ext)
		copy_name = "%s~v%su%s%s" % (trunk, ver, update, ext)
#			(target_file.split(".")[0], ver, update, target_file.split(".")[1])
	else:
		copy_name = "%s~v%su%s" % (target_file, ver, update)

	try:
		print "File copying..."
		
		shutil.copyfile(target_file, os.path.join("STOR_%s" % dir_name, copy_name))
		print "File copied"
		print "\t", "From: ", target_file
		print "\t", "To: ", os.path.join("STOR_%s" % dir_name, copy_name)

	except Exception, e:
		print e
		print e.args
		sys.exit(-1)

	return os.path.join("STOR_%s" % dir_name, copy_name)
#	return copy_name

def update_version_file(dir_name, version_file, ver, update):
	try:
		cur_name = "./STOR_%s/%s" % (dir_name, version_file)
		new_name = "./STOR_%s/%s" % (dir_name, version_file.split("=")[0] + "="  \
				+ ver + "." + str(int(update)+1))

		os.rename(cur_name, new_name)
		print "Version file renamed"
		print "\t", "From: %s" % cur_name
		print "\t", "To: %s" % new_name
#		print "Version file renamed to: %s" % os.path.basename(new_name)
#		print "File renamed to: %s" % version_file
#		print "Version file renamed to: %s" % os.path.basename(new_name)
	except Exception, e: print e

	return new_name

def do_job(target_file='main.py'):
    #01 setup ==========================
    dir_name = os.path.basename(os.getcwd())

    handle_STOR_dir(dir_name)

    #02 version file exists? ==========================
    list = os.listdir("./STOR_%s" % dir_name)
    version_file = handle_version_file(dir_name, target_file, list)

    #03 get version number ==========================
    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
    print "version_file=", version_file

    version_num, ver, update = get_version_number(version_file)
#    print version_num, ver, update

    #04 copy 'main.py' to STOR ==========================
    new_file_path = copy_files(target_file, dir_name, ver, update)

    #05 update the number of the version file ==================
    new_version_file = update_version_file(dir_name, version_file, ver, update)

    #06 log ========================================
    if not os.path.isdir("log"): os.mkdir("log")
#    if not os.path.isdir("log"): os.path.mkdir("log")

    if len(target_file.split(".")) > 1:
        f = file(r"log\%s_%s.log" % (target_file.split(".")[0], target_file.split(".")[1]), "a")
    else:
        f = file(r"log\%s.log" % (target_file), "a")
    f.write("[log %s] ------------------------\n" % get_time_label3())
    f.write("<job>: Versioning\n")
    f.write("File: %s\n" % target_file)
    f.write("\tVersion file: %s\n" % version_file)
    f.write("\tNew version file: %s\n" % os.path.basename(new_version_file))
#            f.write("\t%s\n" % options['-T'])
    f.write("[/log %s] ------------------------\n\n" % get_time_label3())

    f.close()

    return new_file_path
#//def do_job(target_file='main.py'):

def _do_recalibrate(f, fname, dir_STOR):
  res = f.readlines()
  reg1 = re.compile('^#file=v(\d+)(u|p)(\d+)')
  reg2 = re.compile('v(\d+)(u|p)(\d+).py')
  res2 = reg2.search(fname)
  counter = 0

  new_lines = list()
  for line in res:
    res1 = reg1.search(line)
    if res1:  #if "#file" detected
      ver_line = (res1.group(1), res1.group(3))
      ver_name = (res2.group(1), res2.group(3))

      if ver_line == ver_name:
        new_lines.append(line)
      else:
#        ver_info = "#file=v%su%s\n" % ver_name
        ver_info = "#file=v%su%s\n" % ver_name
        new_lines.append(ver_info)
        counter += 1
    else:
      new_lines.append(line)
    #/if
  #/for
  try:
#    f2 = file(dir_STOR + "/" + fname.split(".")[0] + "_new" + ".py", "w")
    f2 = file(dir_STOR + "/" + fname, "w")
  except Exception, e:
    print e
  try:
    f2.write("".join(new_lines))
    print "File written: %s" % fname
#    counter += 1
  except Exception, e:
    print e

  print "%d item(s) of '%s' files recalibrated" %       (counter, fname.split(".")[0].split("~")[0])


def recalibrate():
  #01 find the STOR directory
  dir_main = os.path.realpath(os.getcwd())

  items = os.listdir(dir_main)
  dir_STOR = ""
  reg1 = re.compile('^STOR')
  for item in items:
    if reg1.search(item):
      dir_STOR = item
  if dir_STOR == "":
    print "STOR directory not found"
    exit(0)

  #02 get items in STOR dir
  items2 = os.listdir(dir_STOR)

  #03 open if Python file
  reg2 = re.compile('v(\d+)(u|p)(\d+).py')
  for item in items2: # files in STOR dir
    res2 = reg2.search(item)
    if res2:  # if item is a python file
      f = file(dir_STOR + "/" + item, "r")  # open the python file
      _do_recalibrate(f, item, dir_STOR)
#      _do_versioning(f, item, dir_STOR)
    #/if
    #debug
#    break

def handle_k_option(options):
      if options['-k'].isdigit():
                  print generate_kw(length=int(options['-k']))
      elif options['-k'][0] == 'a':
              print generate_kw(
                              length=int(options['-k'][1:]), option='a')
      elif options['-k'][0] == 'A':
              print generate_kw(
                              length=int(options['-k'][1:]), option='A')
      elif options['-k'][0].lower() == 'n':
              print generate_kw(
                              length=int(options['-k'][1:]), option='n')
      elif options['-k'][0].lower() == 's':
              print generate_kw(
                              length=int(options['-k'][1:]), option='special')
      else:
            print generate_kw(option=options['-k'])
      sys.exit(0)

def handle_L_option(options):
      if len(options['-L'].split(".")) == 1:
                f = file(r"log\%s.log" % options['-L'], "a")
      else:
                f = file(r"log\%s_%s.log" % \
                      (options['-L'].split(".")[0],
                      options['-L'].split(".")[1]), "a")
      f.write("[log %s] ------------------------\n" % get_time_label3())
      f.write("<job>: Logging\n")
      f.write("File: %s\n" % options['-L'])
      f.write("\t%s\n" % options['-T'])
      f.write("[/log %s] ------------------------\n\n" % get_time_label3())

def handle_args():
      """
      
      """
    # preliminaries ==========================
      args = sys.argv

      """
      If option 'v' is used, show the message,
      informing that '-v'(hyphen v) should be
      used.
      """
      if args[1] == 'v':
            print \
                  "Option 'v' was deprecated. ", \
                  "Please use '-v' option."
            sys.exit(0)

      """ command 'recal' """
      if args[1] == "recal":
            recalibrate()
            sys.exit()

      # 01 ==========================
      """ set option keychars """
      kw = "v:hJL:T:k:j:"
      """ Use 'getopt' command """
      try: opts, strings = getopt.getopt(args[1:], kw)
      except Exception, e:
            print "\n[DEBUG:%d]" % \
                  inspect.currentframe().f_lineno
            print e
            traceback.print_exc()
            sys.exit()

      # option: -v ====================
      """ list of files for 'do_job()' """
      do_files = list()
      """ list of files for jar """
      for_jar_files = list()

      """ Format opts variable into a dictionary """
      options = dict(opts)

      """ '-k' option """
      if '-k' in options.keys():    # generate password
            handle_k_option(options)

      """ options other than '-k' """
      for x,y in opts:
#        if x == "-h" or x == "help": print USAGE; sys.exit()
        if x == "-h": print USAGE; sys.exit()
        if x == "-v":
            """
        y will be
        1. "*~~"
        2. "*"
        3. "", "."
        4. ","
        5. None of the above
      """
            if y == "*~~": # version all file in the current dir
                        for_jar_files = \
                              [item for item in os.listdir(os.getcwd()) \
                              if os.path.isfile(item)]
            # "*" => version all file in the current dir #
            elif y == "*":
                target_files = \
                              [item for item in os.listdir(os.getcwd())
                              if os.path.isfile(item)]
                for item in target_files:
                          if not "~~" in item: do_files.append(item)
                          else: item = item.split("~")[0]
                          for_jar_files.append(item)
                
            elif y == "" or y == ".": do_files.append("main.py")
            ## "," => multiple files ##
            elif "," in y :
                  files = y.split(",")
                  for i in files:
                        if not "~~" in i: do_files.append(i)
                        else: i = i.split("~")[0]
                        for_jar_files.append(i)
            ## single file ##
            else:
                        if not "~~" in y: do_files.append(y)
                        else: y = y.split("~")[0]
                        for_jar_files.append(y)

        #/if x == "-v":
        
        if x == "-L" and "-T" in options.keys():  # logging
            handle_L_option(options)

      #/for x,y in opts:
      
      return do_files, for_jar_files, opts
#/def handle_args():

def get_final_jar_files(jar_files):
    name_trunk = os.path.basename(os.getcwd())
    dir_STOR = "STOR_%s" % name_trunk

    final_jar_files = list()
    each_files = list()
    dict_jar_files = dict()

    for name in jar_files:
        #debug
        print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
        print "name=", name
#        sys.exit(0)
        
        if len(name.split(".")) > 1:
            reg = re.compile("^%s~v[\d]+u[\d]+\.%s"
                    % (name.rsplit(".", 1)[0], name.rsplit(".", 1)[1]))
#                                    % (name.split(".")[0], name.split(".")[1]))
        else :
            reg = re.compile("^%s~+v[\d]+u[\d]+" % name.split(".")[0])

        items = [item for item in os.listdir(dir_STOR) if re.search(reg, item)]
        # if no version file in STOR_XXX, then the current version is chosen
        if len(items) == 0: items.append(name)

        if len(name.split(".")) > 1 and not "~" in name:
            print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
#            print r"reg=^(%s)~v([\d]+)u([\d]+)\.(%s)"
            regex = "^(%s)~v([\d]+)u([\d]+)\.(%s)" \
                    % (name.rsplit(".", 1)[0], name.rsplit(".", 1)[1])
#                            % (name.split(".")[0], name.split(".")[1])
            reg = re.compile(regex)
            print "regex=%s" % regex
#            reg = re.compile("^(%s)~v([\d]+)u([\d]+)\.(%s)"
#                            % (name.split(".")[0], name.split(".")[1]))
        elif len(name.split(".")) > 1:
#            print r'"reg = re.compile("^(%s)\.(%s)"'
            regex = "^(%s)\.(%s)" \
                    % (name.rsplit(".", 1)[0], name.rsplit(".", 1)[1])
            print "regex=%s" % regex
            reg = re.compile(regex)
#            reg = re.compile("^(%s)\.(%s)"
#                                        % (name.split(".")[0], name.split(".")[1]))
        else:
            print r"reg=^(%s)~v([\d]+)u([\d]+)"
            reg = re.compile("^(%s)~v([\d]+)u([\d]+)" % name)

        a_reg = [re.search(reg, item).groups() for item in items if re.search(reg, item)]

        if len(a_reg) == 0:
            print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno; #sys.exit()
            print "Warning: '%s' has no versioned file" % name
            sys.exit(0)
        print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno; #sys.exit()
        print "a_reg=", a_reg
        print "len(a_reg)=", len(a_reg)
        print "reg=", reg

        print "a_reg=%s" % a_reg
        print

#        if len(a_reg_int[0]) >= 4:
        if len(a_reg[0]) >= 4:
            a_reg_int = [(a, int(b), int(c), d) for (a,b,c,d) in a_reg]
        else:
            a_reg_int = [(a, int(b), int(c)) for (a,b,c) in a_reg]
        print "a_reg_int=%s" % a_reg_int
        print

        a_reg_int.sort(key=lambda x: (int(x[1]), int(x[2])), reverse=True)

        if len(a_reg_int) == 0: a_reg_int.append(name)

        print "a_reg_int[0]=", a_reg_int[0]
        print

        final_jar_files.append(a_reg_int[0])

        dict_jar_files[name] = "%s~v%su%s.%s" %  \
                (a_reg_int[0][0], a_reg_int[0][1], a_reg_int[0][2], a_reg_int[0][3])

    #debug
    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno; #sys.exit()
    print "dict_jar_files=", dict_jar_files

    # back to original file name
    final_jar_files2 = list()
    for item in final_jar_files:
        if type(item) == tuple:
            if len(item) >= 4:
                final_jar_files2.append(
                        "%s~v%su%s.%s" % (item[0], item[1], item[2], item[3]))
            else:
                final_jar_files2.append(
                        "%s~v%su%s" % (item[0], item[1], item[2]))
        else: final_jar_files2.append(item)

    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno; #sys.exit()
    print "final_jar_files=%s" % final_jar_files
    print "final_jar_files2=%s" % final_jar_files2

    return final_jar_files2, dict_jar_files
#//def get_final_jar_files(jar_files):

def write_jarlog(
                  jarlog_file, final_files, jar_file_path):
#    jarlog_file = "%s\\jar.log" % dir_STOR
    time_label = get_time_label2()

    f = open(jarlog_file, "a")
    f.write("[log %s] ------------------------\n" % time_label)
    f.write("    " + "Jar file: %s\n" % jar_file_path)
    for item in sys.argv:
        if "-j" in item:
            f.write("    " + "Comment: %s\n" %
                        item.split("-j", 1)[1])
            break
    f.write("    " + "Content: %d\n" % len(final_files))
    for item in final_files:
#        f.write("        " + "%s\n" % final_files)
        f.write("        " + "%s    %s\n" % (item.split("\\")[0], item.split("\\")[1]))
    f.write("[/log %s] ------------------------\n" % time_label)
    f.write("\n")

    f.close()

def do_jar(jar_files):
    #debug
    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
    print "jar_files=", jar_files

    final_files = list()    # path-added file names
    final_jar_files, dict_jar_files = get_final_jar_files(jar_files) # non-path-added names

    # get STOR dir
    name_trunk = os.path.basename(os.getcwd())
    dir_STOR = "STOR_%s" % name_trunk

    reg = re.compile("^.+~+v[\d]+u[\d]+")
    for item in final_jar_files:
        if re.search(reg, item):
            final_files.append(os.path.join(dir_STOR, item))
        else: final_files.append(item)
    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno; #sys.exit()
    print "final_jar_files=", final_jar_files
    print "final_files=", final_files

    files = " ".join(final_jar_files)
    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno; #sys.exit()
    print "files=", files

    jar_file_path = "%s\\%s%s%s.jar" % (dir_STOR, name_trunk, "_", get_time_label2())
    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno; #sys.exit()
    print "jar_file_path=", jar_file_path
#    sys.exit(0)

    # prepare jar command line arguments
    jar_args = ""
    for item in final_files:
        if "STOR" in item:
            jar_args += " ".join(("-C", item.split("\\")[0], item.split("\\")[1]))
#            jar_args += " "
        else:
            jar_args += item
#            jar_args += " "
        jar_args += " "

#    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno; #sys.exit()
#    print "jar_args=", jar_args
#    sys.exit()

#    command = "jar cvf %s %s" % (jar_file_path, " ".join(final_files))
    command = "jar cvf %s %s" % (jar_file_path, jar_args)

    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno; #sys.exit()
#    print "command=", command
#    sys.exit()

    try:
        os.system(command)
        # write jar log
#        write_jarlog(dir_STOR, final_files, jar_file_path)
#        jarlog_file = "%s\\jar.log" % dir_STOR
        jarlog_file = r'log\jar.log'
        write_jarlog(jarlog_file, final_files, jar_file_path)
        print "Jar log written: %s" % jarlog_file
        print "Jar file created: %s" % jar_file_path

        # log each file ================================
        for item in jar_files:
            if not os.path.isdir("log"): os.mkdir("log")
            try:
                if len(item.split(".")) > 1:
                    file_name = r"log\%s_%s.log" % \
                            (item.rsplit(".", 1)[0], item.rsplit(".", 1)[1])
#                        f = file(r"log\%s_%s.log" %
#                            (item.rsplit(".", 1)[0], item.rsplit(".", 1)[1]), "a")
                else:
                    file_name = r"log\%s.log" % item
#                    f = file(r"log\%s.log" % item, "a")
                f = file(file_name, "a")
            except Exception, e:
                traceback.print_exc()
                return
            time_label = get_time_label3()
            f.write("[log %s] ------------------------\n" % time_label)
            f.write("<job>: Jar file\n")
            f.write("File: %s\n" % item)
            f.write("\tJar file: %s\n" % jar_file_path)            
            f.write("\tVersion: %s\n" % dict_jar_files[item])
            f.write("[/log %s] ------------------------\n\n" % time_label)

            f.close()
            print "log file written: %s" % file_name
    except Exception,e :
        print e
        traceback.print_exc()
        sys.exit()

#//def do_jar(jar_files):

def make_util_dirs(proj_dir, dirs):
    default_dirs = ["log", "STOR_%s" % os.path.basename(proj_dir)]

#    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
#    print "default_dirs=", default_dirs
#    sys.exit(0)

    if dirs == "*":
        for item in default_dirs:
            try:
                os.mkdir(item)
                print "New dir created: %s" % item
            except Exception, e:
                traceback.print_exc()
                continue
    elif "," in dirs:
        for item in dirs.split(","):
            try:
                os.mkdir(item)
                print "New dir created: %s" % item
            except Exception, e:
                traceback.print_exc()
                continue
    else:
        item = dirs
        try:
            os.mkdir(item)
            print "New dir created: %s" % item
        except Exception, e:
            traceback.print_exc()
#            continue
#//make_util_dirs(os.getcwd(), sys.argv[2])

# execute ========================
def copy_rails_config_file(
                            directory, filename, flag=0):
    """
    Description:

    Vars:
        1. f_dst: source file name
        2. f_src: dst file name
        3. flag
            1 => copy ".project"
            2 => copy "do_heroku.bat"
        4. content: content of ".project"
        5. fin: file object
        6. fout: file object
        7. directory: full directory path
    """
    f_dst = os.path.join(os.getcwd(), filename)
    f_src = os.path.join(os.path.dirname(
                    inspect.currentframe()
                    .f_code.co_filename), directory,
                    filename)
    if flag == 1:
        fin = open(f_src, "r")
#        content = f.read()
        content = fin.read()
        content = content.replace(
                    "@project_name@",
                    os.path.basename(os.getcwd()))
#                    os.path.basename(f_dst))
        fout = open(f_dst, "w")
        fout.write(content)

        fin.close()
        fout.close()

    else:
        shutil.copyfile(f_src, f_dst)
    print "File copied"
    print "\t", "From: %s" % f_src
    print "\t", "To: %s" % f_dst

def copy_individual_files():
    """
    Desc:
        Copy specific files from "nbp_new" directory
    Vars:
        ans => receive raw_input()
    """
    files_list = {
            "1": "/rails/.project",
            "2": "/rails/do_heroku.bat"
    }
    if len(sys.argv) < 3:
            while(1):
#                    print "Which file to copy?['0' to quit]:",
                for item in files_list.keys():
                    print "%s => %s" % (item, files_list[item])
#                    for k, v in item:
#                        print "%s => %s" % (k, v)
#                    print "1 => /rails/.project"
#                    print "2 => /rails/do_heroku.bat"
                ans = raw_input(
                        "Which file to copy?\n" +
                        "['0' to quit]:")
                if ans == "0": sys.exit(0)
                else:
                    if ans == "1":
                        copy_rails_config_file(
                                        "rails", ".project", flag=1)
                    if ans == "2":
                        copy_rails_config_file(
                                        "rails", "do_heroku.bat")

def etc_commands():
      # 00-1 ============================
      """ option: md """
      if sys.argv[1] == "md":
        make_util_dirs(os.getcwd(), sys.argv[2])

    # 00-2 ============================
      """ option: time """
      if sys.argv[1] == "time" or sys.argv[1] == "t":
#        #debug
#        print "len(sys.argv)=", len(sys.argv)
        
        if platform.system() == "Linux":
            if len(sys.argv) > 3:
                print "\t", get_time_label2_span(sys.argv[2], sys.argv[3])
            else:
                print "\t", get_time_label2()
        else:
            if len(sys.argv) > 2:
                print "\t", get_time_label2_span(sys.argv[2], sys.argv[3])
            else:
                print "\t", get_time_label2()
            
        sys.exit(0)

      """ option: time """
      if sys.argv[1] == "t2":
          
          print "\t", get_time_label3()
          
          sys.exit(0)

    # 00-3 ============================
      """ option: cf """
      if sys.argv[1] == "cf":
        copy_individual_files()

#//def etc_commands():

if __name__ == '__main__':
    # 00 =============================
    """
    Command only, then the usage is shown
    """
    if len(sys.argv) < 2: print USAGE; sys.exit(0)

    # 00-1 ============================
    """
    Handle options:
      md => Create utility directories
      time => Show time label
      cf => Copy specific files
    """
    etc_commands()

    # 01 handle args ================
    """
    Handle options other than those
    handled in "etc_commands()"
    1. do_files => Files for versioning
    2. for_jar_files => Files for jar file
    """
    do_files, for_jar_files, opts = handle_args()

        # 02 do job ================
        # setup files list for jar
    for i in do_files: do_job(i)
        # output
    print "\n[DEBUG:%d]" % \
                inspect.currentframe().f_lineno; #sys.exit()
    print "\t", "do_files = ", do_files

    print "\n[DEBUG:%d]" % \
                inspect.currentframe().f_lineno; #sys.exit()
    print "\t", "for_jar_files = ", for_jar_files
    # 03 jar file ================
    """
    Create jar file
    """
    if "-J" in sys.argv or "-v*~~" in sys.argv:
                do_jar(for_jar_files)

"""
    #debug
    print "\n[DEBUG:%d]" % inspect.currentframe().f_lineno;
    sys.exit()
"""