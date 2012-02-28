#!/usr/bin/python
# -*- coding: utf-8 -*-
#dir=C:\workspaces\ws_ubuntu_1\G20110722_140400_create_configure_file_1\main.py
#file=v1u0
#created_at=20110722_140400

import os
import sys
import datetime
import inspect
import getopt
import re

from configure_in import *

# variables ========================
VERSION = [1.0, "2011/07/22 14:07:37"]

USAGE = """<<Usage>>
	<Options>
	-h: show help
	-M<name> : name of the MAINFILE in the Makefile

"""
# methods ========================
def get_time_label2():
	t = datetime.datetime.today()
	t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
	t2 = [str(item) for item in t1]

	for i in range(len(t2)):
		if len(t2[i]) < 2: t2[i] = "0" + t2[i]

	return "".join(t2[:3]) + "_" + "".join(t2[3:])

def do_job():
#	from configure_in import *

	f1 = file("Makefile.in")
	content = f1.read()
#	reg = re.compile('@.+?@')

	for item in kw.keys():
		reg = re.compile(r"@%s@" % item)
#		if reg.match(content):
		if reg.search(content):
			content = content.replace(
					"@%s@" % item,
					kw[item]
			)
			print "'%s' was replaced to '%s'" % \
					("@%s@" % item, kw[item])
	#for item in kw.keys():/

	f2 = file("Makefile", "w")
	f2.write(content)
#	for word in kw.keys():


#	print kw.keys()

#	print kw

# execute ========================
if __name__ == '__main__':
#	print "Content-Type: text/html"
#	print ""

	do_job()
