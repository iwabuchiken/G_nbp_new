#!/usr/bin/python
# -*- coding: utf-8 -*-
#dir=C:\workspaces\ws_ubuntu_1\G20110908_145540_nbp_GUInize_1\main.py
#file=v1u0
#created_at=20110908_145540

import os
import sys
import datetime
import inspect
import getopt

import Tkinter

#import lib

# variables ========================
VERSION = ["1.0", "2011/09/08 14:55:53"]

# classes ========================
class Nbp(Tkinter.Frame):
	def __init__(self, master=None):
		Tkinter.Frame.__init__(self, master)
		self.buildGUI()

	def create_F1(self):
		# Frame: 1
			# Frame
		self.F1 = Tkinter.Frame(self.master)
		self.F1.pack()
			# label
		self.dispLabel1 = Tkinter.Label(
				self.F1,
				width = 30,
				text = u"Option: String".encode('utf-8'))
		self.dispLabel1.pack(side = Tkinter.LEFT)
#		self.dispLabel.pack(side = Tkinter.RIGHT)
			# StringVars
		self.inText1 = Tkinter.StringVar()
			# Entries
		self.inputBox1 = Tkinter.Entry(
				self.F1,
				textvariable = self.inText1,
				width = 40)
		self.inputBox1.pack(side = Tkinter.RIGHT)

		return self.F1, self.dispLabel1, self.inText1, self.inputBox1



	def create_F2(self):
		# Frame: 1
			# Frame
		self.F2 = Tkinter.Frame(self.master)
		self.F2.pack()
			# label
		self.dispLabel2 = Tkinter.Label(
				self.F2,
				width = 30,
				text = u"Option: Project type".encode('utf-8'))
		self.dispLabel2.pack(side = Tkinter.LEFT)
#		self.dispLabel.pack(side = Tkinter.RIGHT)
			# StringVars
		self.inText2 = Tkinter.StringVar()
			# Entries
		self.inputBox2 = Tkinter.Entry(
				self.F2,
				textvariable = self.inText2,
				width = 10)
		self.inputBox2.pack(side = Tkinter.RIGHT)

		return self.F2, self.dispLabel2, self.inText2, self.inputBox2

	def create_F3(self):
		# Frame: 1
			# Frame
		self.F3 = Tkinter.Frame(self.master)
		self.F3.pack()
			# label
		self.dispLabel3 = Tkinter.Label(
				self.F3,
				width = 50,
				text = u"Messages will be shown here".encode('utf-8'))
		self.dispLabel3.pack(side = Tkinter.LEFT)
#		self.dispLabel.pack(side = Tkinter.RIGHT)

		return self.F3, self.dispLabel3

	def create_F4(self):
		# Frame: 1
			# Frame
		self.F4 = Tkinter.Frame(self.master)
		self.F4.pack()
			# label
		self.dispLabel4 = Tkinter.Label(
				self.F4,
				width = 30,
				text = u"Option: Enter 'y' if to set all to 'yes'".encode('utf-8'))
		self.dispLabel4.pack(side = Tkinter.LEFT)
#		self.dispLabel.pack(side = Tkinter.RIGHT)
			# StringVars
		self.inText4 = Tkinter.StringVar()
			# Entries
		self.inputBox4 = Tkinter.Entry(
				self.F4,
				textvariable = self.inText4,
				width = 40)
		self.inputBox4.pack(side = Tkinter.RIGHT)

		return self.F4, self.dispLabel4, self.inText4, self.inputBox4

	def create_F5(self):
		# Frame: 1
			# Frame
		self.F5 = Tkinter.Frame(self.master)
		self.F5.pack()

		return self.F5

	def create_btn_1(self, F5):
		self.execButton = Tkinter.Button(
				self.F5,
				text=u"Exec".encode('utf-8'),
				command=self.do_nbp)
#				command=self.do_upload)
#				command=self.do_upload(text="hello", msg="message"))
		self.execButton.pack(side = Tkinter.RIGHT)

#	def do_upload(self, text='hello', msg='message'):

	def create_btn_2(self, F5):
		self.quitButton = Tkinter.Button(
				self.F5,
				text=u"Quit".encode('utf-8'),
				command=self.quit)
#				command=self.do_upload(text="hello", msg="message"))
		self.quitButton.pack(side = Tkinter.RIGHT)

	def quit(self):
		sys.exit()
#	def do_upload(self, text='hello', msg='message'):
	def do_upload(self):
		dir = self.inText1.get()
		files = self.inText2.get()
		yes_flag = self.inText4.get()

		if dir == '': dir = "."
#		elif dir == 'html': dir = "html"
		if files == '': files = "*"
		if yes_flag == '': yes_flag = "-y"

		self.dispLabel3.configure(
					text = "dir=%s files=%s yes_flag=%s" % (dir, files, yes_flag))

		command = "upload.py -D%s -F%s -P5n6WW09Y -M755 %s" % (dir, files, yes_flag)
		print "command=", command
		os.system(command)

#		if dir == '': print "dir is ''"
#		print type(dir)
#		print type(files)
#		print type(yes_flag)

#		self.dispLabel3.configure(
#					text = "dir=%s files=%s yes_flag=%s" % (dir, files, yes_flag))
		#debug
#		sys.exit()
#
#		command = "upload.py -D%s -F%s -P5n6WW09Y -M755" % (dir, files)
#		os.system(command)
#		sys.exit()
#		self.dispLabel3.configure(text = self.inText1.get() + u": message".encode('utf-8'))
#		self.dispLabel3.configure(text = type(self.inText1.get()))
#		self.dispLabel3.configure(text = "hello")
#		print text

	def do_nbp(self):
		label_string = self.inText1.get()
#		dir = self.inText1.get()
		project_type = self.inText2.get()
#		files = self.inText2.get()
		yes_flag = self.inText4.get()

#		if dir == '': dir = "."
#		elif dir == 'html': dir = "html"
		if project_type == '': project_type = "p"
#		if files == '': files = "*"
		if yes_flag == '' or yes_flag.lower() == 'y': yes_flag = "-y"
		elif yes_flag == 'n': yes_flag = ""

		self.dispLabel3.configure(
					text = "label=%s project type=%s" % \
						(label_string, project_type))
#					text = "dir=%s files=%s yes_flag=%s" % (dir, files, yes_flag))

		command = "nbp.py -S%s -p%s %s" % (label_string, project_type, yes_flag)
#		command = "upload.py -D%s -F%s -P5n6WW09Y -M755 %s" % (dir, files, yes_flag)
		print "command=", command
		os.system(command)

		# ending
		print "==========================================="
		print "\t\t<nbp_g.py>"
		print "All the work done successfully."
		print "==========================================="

		sys.exit(0)

	def buildGUI(self):
		self.F1, self.dispLabel1, self.inText1, self.inputBox1 = self.create_F1()
		self.F2, self.dispLabel2, self.inText2, self.inputBox2 = self.create_F2()
		self.F4, self.dispLabel4, self.inText4, self.inputBox4 = self.create_F4()
		self.F3, self.dispLabel3 = self.create_F3()
		self.F5 = self.create_F5()

#		F5 = self.F5
#		self.execButton = self.create_btn_1(F5)
		self.execButton = self.create_btn_1(self.F5)
		self.quitButton = self.create_btn_2(self.F5)


# methods ========================
def do_job():
	pass

# execute ========================
if __name__ == '__main__':

	f = Nbp()
	f.pack()
	f.mainloop()

"""
print "[DEBUG:%d]" % inspect.currentframe().f_lineno; sys.exit()
"""