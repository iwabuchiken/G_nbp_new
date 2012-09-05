#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import inspect
import os
import sys
import traceback

# variables ========================

def do_job():
      opts = sys.argv
      if len(opts) < 3:
            print "We need 3 args"
            print "You game me: %s" % opts
            sys.exit(0)
#      print opts
      try:
            print "git co -b %s" % opts[1]
            os.system("git co -b %s" % opts[1])
      except Exception, e:
            print e
#      re.compile("#\t(.+)")search(a[re.compile("Untracked
#      files").search(a).end()+2:].split("\n")[2]).group(1)
      print "[INFO]Checking out branch: %s" % opts[1]
      os.system("git co %s" % opts[1])
      os.system("git status")
      print "[INFO]Adding new files"
      os.system("git add .")
      print("[INFO]Committing: git commit -a -m \"%s\"" % opts[2])
      os.system("git commit -a -m \"%s\"" % opts[2])
      print "[INFO]Retun to masteer"
      os.system("git co master")
#      print "[INFO]Merging..."
#      os.system("git merge %s" % opts[1])
#      print "[INFO]Done"
#      print("git co %s" % opts[1]) print("git status") print("git commit -m -a
#      \"%s\"" % opts[2]) print("git co master") print("git merge %s" % opts[1])
#      os.system("git co %s" % opts[1]) os.system("git status") os.system("git
#      commit -m -a %s" % opts[2]) os.system("git co master") os.system("git
#      merge %s" % opts[1])
      
#      print "ok"
#      print "git co -b %s" % opts[1]
#      os.system("git co -b %s" % opts[0])

# execute ========================


if __name__ == '__main__':
    do_job()
    #debug
    do_some()
    
#    print "abc"
    print "defgha"