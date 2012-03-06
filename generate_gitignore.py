####################################`
 # MyUtil.java
 # Author: Iwabuchi Ken                #
 # Date: 20120306_075522
 # Aim:                                #
 #     1.
 # <Usage>
 #    1. Run the program
 # <Source>
 #     1. "null"	=> http://d.hatena.ne.jp/monajiro/20100317
 ####################################/
import os
import sys


def write_to_file(file, ignore_set):
	for item in ignore_set:
		file.write("*%s\n" % item)
#//write_to_file

def second():
	##############################
	# Processes
	#    1. Open the file
	#    1. write the first lines for the current dir
	#    2. get the list of the current dir
	#    3. if the item in the list is of a file, generate 
	#           a path, write to the file
	#	99. close the file
	##############################
	
	# variables			#####
	file_name		= ".gitignore"					# file name
	# if the file exists, open with 'a'
	# if not, with 'w'
	if file_name in os.listdir(os.getcwd()):
		f_out	= open(file_name, "a")			# file exists
	else:
		f_out	= open(file_name, "w")			# not exist
	
#	if (os.path.isfile(file(file_name))):
#		file	= open(file_name, "a")
#	else:
#		file	= open(file_name, "w")
	ignore_set	= [".tds", ".exe", ]
	
	# write the first lines	#
	#write_to_file(f_out, ignore_set)
	for item in ignore_set:
		f_out.write("*%s\n" % item)
	# get the list			#####
	dir_list    = os.listdir(os.getcwd());
	
	### write the first order paths ###
	for item in dir_list:
		# if the item is a dir, write the path
		if (os.path.isdir(item)):
			for ext in ignore_set:
				pass
				line	= "./%s/*%s\n" % (item, ext)
				#line	= "/".join((".%s" % item, "*%s" % ext)
				f_out.write(line)
				#f_out.write(line)
			
			#//for
	#//for

	### close the file ###
	f_out.close()

	
#//second()

def open_file():
	##############################
	# Processes
	#    1. Open the file
	#    1. write the first lines for the current dir
	#    2. get the list of the current dir
	#    3. if the item in the list is of a file, generate 
	#           a path, write to the file
	#	99. close the file
	##############################
	
	# variables			#####
	file_name		= ".gitignore"					# file name

	# if the file exists, open with 'a'
	# if not, with 'w'
	if file_name in os.listdir(os.getcwd()):
		f_out	= open(file_name, "a")			# file exists
	else:
		f_out	= open(file_name, "w")			# not exist
	
	ignore_set	= [".tds", ".exe", ]
	
	# write the first lines	#
	for item in ignore_set:
		f_out.write("*%s\n" % item)
	# get the list			#####
	dir_list    = os.listdir(os.getcwd());
	
	### write the first order paths ###
	for item in dir_list:
		# if the item is a dir, write the path
		if (os.path.isdir(item)):
			for ext in ignore_set:
				pass
				line	= "./%s/*%s\n" % (item, ext)
				#line	= "/".join((".%s" % item, "*%s" % ext)
				f_out.write(line)
				#f_out.write(line)
			
			#//for
	#//for

	### close the file ###
	f_out.close()

	
#//open_file()

def get_gitignore_path(root_path, target_path):
	### variables ###
	p1						= root_path.split("\\")
	p2						= target_path.split("\\")
	p3						= list()
	i						= 0	# index for p2
	
	### processes ###
	# reverse
	p1.reverse()
	p2.reverse()

	# compare and generate
	for i in range(len(p1)):
		# if the length of the target path is 1,
		#	and the elements of p1 and p2 don't
		#	match, add "." to p3 and break the
		#	for loop.
		if (p2[0] != p1[i] and len(p2) == 1):
			p3.append(p2[0])
			p3.append(".")
			break
		elif (p2[0] == p1[i]):
			#p3.append(p2[i])
			p3.append(p2[0])
			p3.append(".")
			break
		else:
			p3.append(p1[i])	
	#//for
	
	# show
	p3.reverse()

	# return
	return "/".join(p3)

#//get_gitignore_path()

def do_listing\
	(file, ROOT_PATH, parent_path, target_dirs):
	for item in target_dirs:
		path	= get_gitignore_path(parent_path, item)
		#debug
		print path
		
		### new target_dirs	###
		#new_dirs	= [x for x in os.listdir(item)]
		new_dirs	= [x for x in os.listdir(item)]
		
		#debug
		#print new_dirs, ": ", os.path.abspath(new_dirs[0])
		print new_dirs
		
		
		### recurse listing	###
		#do_listing(file, root_path, target_dirs)
	
#//do_listing(file, ROOT_PATH, parent_path, target_dirs)

if __name__ == '__main__':
	### variables ###
	ROOT_PATH	= os.getcwd()		# root path
	target_dirs		= [item for item in os.listdir(ROOT_PATH) if os.path.isdir(item)]
	path1	= ""		# path
	
	# debug
#	print target_dirs
#	sys.exit(0)
	
	### setup
	file		= open_file()
	
	### processes
	do_listing(file, ROOT_PATH, ROOT_PATH, target_dirs)
	
	
#	for item in dirs:
#		print "item=", item
#		if (os.path.isdir(item)):
#			path1		= get_gitignore_path(ROOT_PATH, item)
#			print "path1=", path1
			
	#second()