import sys
#!/usr/bin/python
# -*- coding: utf-8 -*-
#dir=C:\workspaces\ws_ubuntu_1\G20110716_070837_GUI_for_upload\main.py
#file=v1u0
#created_at=20110716_070837

import os

# variables ========================
VERSION = ["2.3", "2011/07/18-08:31:22"]

# methods ========================

if __name__ == '__main__':
	#src_path = r"C:\workspaces\ws_ubuntu_1\G20110617_095214_nbp_new"
	src_path = os.path.dirname(__file__)

        #debug
        #print src_path
        #sys.exit(0)

	if (len(sys.argv) > 1) and sys.argv[1] == "-h":
		os.system("upload.py -h")
	else: os.system("python %s/upload_g.py" % src_path)
	
"""
print "[DEBUG:%d]" % inspect.currentframe().f_lineno
sys.exit()
"""
