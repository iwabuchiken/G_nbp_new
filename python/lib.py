#file_info

import os
import datetime


# variables ==================================
VERSION = []

# methods ==================================
def get_encoding_type(string):
      """
      Description:
      1. Return the encoding name of the given
                  string.
            2. The registered encoding names are:
                  utf-8
                  shift-jis
                  euc-jp
            3. If the encoding type of the string
                  doesn't match either of the above,
                  returns "Neither of..." message
                  as a string
            4. If the string is a unicode object,
                  then returns "unicode"
    """
      encoding_types = [
            "utf-8", "shift-jis", "euc-jp"
      ]

      if type(string) == unicode: return "unicode"

      for item in encoding_types:
            try:
                  string.decode(item)
                  return item
            except:
                  pass

      return "Neither of %s" % encoding_types

def get_time_label2():
	t = datetime.datetime.today()
	t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
	t2 = [str(item) for item in t1]

	for i in range(len(t2)):
		if len(t2[i]) < 2: t2[i] = "0" + t2[i]

	return "".join(t2[:3]) + "_" + "".join(t2[3:])

def get_url_path(fname):
	return "".join(["%s"]*4) % (os.sep, os.path.basename(os.getcwd()), os.sep, fname)

def get_fs_path():
	# 01 =============
#	cur_dir = os.getcwd()
	# 02 =============
	cur_dir_l = os.getcwd().split(os.sep)
#	cur_dir_l = cur_dir.split(os.sep)
	# 03 =============
#	ind1 = os.getcwd().split(os.sep).index("www")
	ind1 = cur_dir_l.index("www")
	# 04 =============
#	ind2 = len(os.getcwd().split(os.sep).index("www")[1:])
	ind2 = len(cur_dir_l[1:])
	# 05 =============
#	str1 = os.sep.join([".."] * (ind2 - ind1))
	return os.sep.join((
				os.sep.join([".."] * (ind2 - ind1)), \
				"html", \
				cur_dir_l[-1]))
#	return os.sep.join((str1, "html", cur_dir_l[-1]))
#	inc_path = os.sep.join((str1, "html", cur_dir_l[-1]))
#	return inc_path
#	print "inc_path=", inc_path

