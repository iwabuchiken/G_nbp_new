#!/usr/bin/python
# -*- coding: utf-8 -*-
#dir=C:\workspaces\ws_ubuntu_1\G20110804_134902_audio_prepare_files\main.py
#file=v1u9
#created_at=20110804_134902

import os
import sys
import datetime
import inspect
import getopt
import traceback
import random
import re
import win32api

#import lib

# variables ========================
VERSION = ["1.3", "2011/08/04 13:49:04"]

USAGE = """<<Usage>>
	<Options>
	-h : show help
	-n<number> : number of auio titles to be copied
	-d<drive name> : name of the drive
	<Example>
	caf.py -n7 -dH: => copy 7 titles to the H drive
"""

# methods ========================
def get_time_label2():
	t = datetime.datetime.today()
	t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
	t2 = [str(item) for item in t1]

	for i in range(len(t2)):
		if len(t2[i]) < 2: t2[i] = "0" + t2[i]

	return "".join(t2[:3]) + "_" + "".join(t2[3:])

def copy_dir(dir_src, dir_dst):
	command = "xcopy %s %s" % (dir_src, dir_dst)
	print "Dir copy starting..."
	print "\t", "From: %s" % dir_src
	print "\t", "To: %s" % dir_dst

	try: os.system(command)
	except Exception, e:
		print e
		traceback.print_exc()
		while(1):
			ans = raw_input("Error. Type 'y' to exit: ")
			if ans.lower() == 'y': sys.exit(0)

	print "Dir copied"

def get_dir_list(directory):
	list1 = os.listdir(directory)
	list_dirs = list()

	for item in list1:
		if os.path.isdir(os.path.join(directory, item)): list_dirs.append(item)
#		if os.path.isdir(item): list_dirs.append(item)

	return list_dirs

def get_file_list(directory):
#	list1 = os.listdir(directory)
	list_files = list()

#	list_files = [item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))]
	

#	for item in list1:
	for item in os.listdir(directory):
		if os.path.isfile(os.path.join(directory, item)): list_files.append(item)
#		if os.path.isdir(item): list_dirs.append(item)

	return list_files

def get_random_numbers(max_num, num):
	random_nums = list()
	
	for i in range(num):
		random_nums.append(random.randrange(1, max_num))

	return random_nums
#	return random.randrange(1, max_num)

def get_dirs_audio(list_dirs):
	list_dirs_audio = list()
	
	for item in list_dirs:
		if (item.split("_")[0].isdigit()): list_dirs_audio.append(item)
#		if (len(item.split("_")) > 1): list_dirs_audio.append(item)
	
	return list_dirs_audio

def get_max_num(directory):
#	list_files = get_file_list(directory)
	num_file = ""
	for item in get_file_list(directory):
		if item.isdigit():
			num_file = item; break

	if num_file == "": return "100"
	else: return num_file

def get_candidate_list(random_nums, list_dirs_audio):
	candidate_list = list()

	for item in random_nums:
		reg = re.compile("^%s_" % item)
		for item2 in list_dirs_audio:
			if (reg.search(item2)):
				candidate_list.append(item2)
				break
				
	return candidate_list

def copy_dirs(directory_src, candidate_list, dir_dst):
	time_label = get_time_label2()
	i = 1 # counter
	for item in candidate_list:
#		command1 = "md \"%s\"" % os.path.join(dir_dst, "test_" + get_time_label2(), item)
#		command1 = "md \"%s\"" % os.path.join(dir_dst, "test_" + time_label, item)
		command1 = "md \"%s\"" % os.path.join(dir_dst, item)
		print "command1=", command1
		os.system(command1)
		print "--------------------------------------------------------(%d)" % i
		print "Dir created: %s" % os.path.join(dir_dst, item)
		print "Dir copying..."
		print "\t", "From: %s" % os.path.join(directory_src, item)
		print "\t", "To: %s" % os.path.join(dir_dst, item)
		
		command2 = "xcopy /E \"%s\" \"%s\"" % \
				(os.path.join(directory_src, item), \
					os.path.join(dir_dst, item))
#					os.path.join(dir_dst, "test_" + time_label, item))
#					os.path.join(dir_dst, "test_" + get_time_label2(), item))
		print "command2=", command2
		os.system(command2)

		i += 1


	print "Copy done."

def get_dir_volume(directory):
	total = 0
	for root, dirs, files in os.walk(directory):
		dir_size = sum(os.path.getsize(os.path.join(root, name)) for name in files)
		total += dir_size

	return total

def get_dir_empty_space(directory):
	empty, used, _ = win32api.GetDiskFreeSpaceEx(directory)
	print "used=", used
	print "empty=", empty

	return empty

def handle_args(args):
	# setup
	num = 5
#	kw = "hn:"
	kw = "hn:d:"
	opts, strings = getopt.getopt(args[1:], kw)

	time_label = ""; directory = ""; proj = ""; yes_flag = False

	for x, y in opts:
		if x == '-h': print USAGE; sys.exit()
		elif x == '-n' and y.isdigit(): num = int(y)
		elif x == '-d': directory = y

	return num, directory

def do_log_1(logfile_path, candidate_list, logfile):
#	logfile = file(logfile_path, "a")
	logfile.write("[Session log:%s]--------------------\n" % get_time_label2())
	logfile.write("<Candidate list>\n")
#	for item in list_dirs_audio:
	for item in candidate_list:
		logfile.write("\t%s\n" % item)

def do_job():
	# handle args ----------------------
	args = sys.argv
#	if len(args) > 1: num = handle_args(args)
	if len(args) > 1: num, directory = handle_args(args)
	else: num = 5

	# variables ----------------------
	directory_src = r"C:\workspaces\ws_audio_video_1\_STORAGE_ws_audio_video_1\folders"
	logfile_path = r"C:\workspaces\ws_ubuntu_1\G20110617_095214_nbp_new\log\log_copyaudio.txt"
#	directory = r"G:"
	dir_dst = r"%s\Audio\SELECT_%s" % (directory, get_time_label2())
#	dir_dst = r"G:\Audio\SELECT_%s" % get_time_label2()

	# 01 get dir list ----------------
#	directory_src = r"C:\workspaces\ws_audio_video_1\_STORAGE_ws_audio_video_1\folders"
	list_dirs = get_dir_list(directory_src)

	# 04 get max_num ----------------
	max_num = get_max_num(directory_src)

	# 02 get random nums ----------------
#	num = 5
	random_nums = get_random_numbers(int(max_num), num)
	random_nums  = [str(item)for item in random_nums]

	# 03 get list_dirs_audio ----------------
	list_dirs_audio = get_dirs_audio(list_dirs)

	# 04 get_candidate_list ----------------
	candidate_list = get_candidate_list(random_nums, list_dirs_audio)

	# do logging ------------------------------
#	logfile_path = r"C:\workspaces\ws_ubuntu_1\G20110617_095214_nbp_new\log\log_copyaudio.txt"

	logfile = file(logfile_path, "a")

	do_log_1(logfile_path, candidate_list, logfile)

#	logfile.write("[Session log:%s]--------------------\n" % get_time_label2())
#	logfile.write("<Candidate list>\n")
##	for item in list_dirs_audio:
#	for item in candidate_list:
#		logfile.write("\t%s\n" % item)

	# get dir volume --------------------
	dirs_size = 0
	for item in candidate_list:
		dir_size = get_dir_volume(os.path.join(directory_src, item))
		print "\t", item, " => ", dir_size/1000000, "MB"
		logfile.write("\t%s => %d MB" % (item, dir_size/1000000))
		dirs_size += dir_size

	#debug
	print "sum=", dirs_size/1000000, "MB"
	logfile.write("sum = %d MB" % (dirs_size/1000000))
#	print candidate_list[0], "\t",
#	print dir_size/1000000, "MB"
#	sys.exit()

	# get dir empty space --------------------
#	directory = r"G:"
	empty = get_dir_empty_space(directory)

	#debug
	print "empty space in %s = %d MB" % (directory, empty/1000000)
	logfile.write("empty space in %s = %d MB" % (directory, empty/1000000))
#	sys.exit()


	# 05 copy_dirs ----------------
	if empty < dirs_size:
		print "Size of the copying directories larger than that of the target directory"
		print "Sorry. We must stop here."
		sys.exit(-1)
	else:
		print "The target directory has enough empty space for the copying directories."
		print "The job continues..."
		
#	dir_dst = r"G:\Audio\SELECT_%s" % get_time_label2()
	os.system("md %s" % dir_dst)
	try:
		copy_dirs(directory_src, candidate_list, dir_dst)
		# do logging ------------------------------
#		logfile.write("[LOG:%s]" % get_time_label2())
		logfile.write("<Dirs copied>\n")
		logfile.write("\tTo: %s\n" % dir_dst)
		logfile.write("[/Session log: %s]--------------------\n" % get_time_label2())
		
	except Exception, e:
		print e
		traceback.print_exc()
		while(1):
			ans = raw_input("Error occurred. Type 'y' to exit: ")
			if ans.lower() == 'y': sys.exit(0)

	#debug
	print "Dirs copied"

	while(1):
		ans = raw_input("All the work done. Type 'y' to exit: ")
		if ans.lower() == 'y': sys.exit(0)

# execute ========================
if __name__ == '__main__':
	print "Content-Type: text/html"
	print ""

	do_job()

	#02 ------------------
#	while(1):
#		ans = raw_input("Job done. Type 'y' to exit: ")
#		if ans.lower() == 'y': sys.exit(0)
