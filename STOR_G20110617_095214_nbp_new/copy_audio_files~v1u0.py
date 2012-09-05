#!/usr/bin/python
# -*- coding: utf-8 -*-
#dir=C:\workspaces\ws_ubuntu_1\G20110804_134902_audio_prepare_files\main.py
#file=v1u0
#created_at=20110804_134902

import os
import sys
import datetime
import inspect
import getopt
import traceback
import random
import re

#import lib

# variables ========================
VERSION = ["1.3", "2011/08/04 13:49:04"]

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

def do_job():
	# 01 get dir list ----------------
	directory_src = r"C:\workspaces\ws_audio_video_1\_STORAGE_ws_audio_video_1\folders"
	list_dirs = get_dir_list(directory_src)

	# 04 get max_num ----------------
	max_num = get_max_num(directory_src)

	# 02 get random nums ----------------
	num = 5
	random_nums = get_random_numbers(int(max_num), num)
	random_nums  = [str(item)for item in random_nums]

	# 03 get list_dirs_audio ----------------
	list_dirs_audio = get_dirs_audio(list_dirs)

	#debug
#	for i in list_dir: print i
#	sys.exit()

	# 04 get_candidate_list ----------------
	candidate_list = get_candidate_list(random_nums, list_dirs_audio)

	#debug
#	for i in candidate_list: print i
#	sys.exit()

	# 05 copy_dirs ----------------
	dir_dst = r"G:\Audio\SELECT_%s" % get_time_label2()
	os.system("md %s" % dir_dst)
	copy_dirs(directory_src, candidate_list, dir_dst)
	#debug
	print "Dirs copied"
#	for i in candidate_list: print i
#	sys.exit()

#	dir_src = "71_TMP_innovation_creativity_Larry_Keeley_0"
#	dir_dst = r"G:\Audio"
#
#	copy_dir(dir_src, dir_dst)

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
