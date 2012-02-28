#!/usr/bin/python
# -*- coding: utf-8 -*-
#dir=C:\workspaces\ws_ubuntu_1\G20110704_131057_PIL_line\main.py
#file=v1u0
#created_at=20110704_131057

import os
import sys
import datetime
import getopt
import traceback
import platform
import inspect

from PIL import Image
from PIL import ImageDraw

# variables ========================
VERSION = ["1.6", "2011/07/05-13:15:56"]
USAGE = """<<Usage>>
  <Options>
    -A: admin items
      v: show version
      h: show help
    -a: how many cols and rows to crop
          => syntax: <left>,<top>,<right>,<bottom>
          => ex: 1,0,0,1 (four numbers with ',' between each)
    -c: the color of the grid line
		=> default: green
		=> 6 digits, hex number: ex: ff0000 (no '#')
    -h: show help
    -i: input file path
    -n: number to divide the longer edge of the image
    -s: theme of the created image file (str)
    -w: line thickness
    -v: show version    
  <Example>
    1) python main.py -w1 -i3.jpg -n13 -a1,0,0,1 -scropped
        => 13 units on the longer edge, thickness 1,
            cropping on left and bottom
    2) python main.py -Avh
        => show version and help
"""
# methods ========================
def get_time_label2():
  t = datetime.datetime.today()
  t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
  t2 = [str(item) for item in t1]

  for i in range(len(t2)):
    if len(t2[i]) < 2: t2[i] = "0" + t2[i]

  return "".join(t2[:3]) + "_" + "".join(t2[3:])

def save_imagefile(img, outfile):
    try:
        img.save(outfile)
        print "Image saved: %s" % outfile
        os.system("%s" % outfile)
        return 1
    except Exception, e:
        print e
        print traceback.print_exc()
        return -1

def get_larger(num1, num2):
    if num1 > num2: return num1
    elif num1 < num2: return num2
    else: return num1

def do_line(img, start_p, end_p, fill_color, wid=1):
#    #debug
#    c = inspect.currentframe(); print "DEBUG:%d" % c.f_lineno
#    print fill_color; sys.exit() #debug
    
    draw = ImageDraw.Draw(img)
    draw.line((start_p + end_p), fill="#%s" % fill_color, width=wid)
#    draw.line((start_p + end_p), fill="#00ff00", width=wid)
#    draw.line((start_p + end_p), fill="#ff0000", width=wid)
#    draw.line((start_p + end_p), fill=(0xff, 0x00, 0x00), width=wid)

    return img

def exec_line(img, interval, fill_color, wid=1):
#    #debug
#    c = inspect.currentframe(); print c.f_lineno
#    print fill_color; sys.exit() #debug

    size_w, size_h = img.size
    larger = get_larger(size_w, size_h)
    unit = larger / interval

    if larger != size_h:
        print "larger is not size_h"; sys.exit(0)
    elif larger == size_h:
        i = 0
        while(i < size_h):
            start_p = (0, i)
            end_p = (size_w, i)
            img = do_line(img, start_p, end_p, fill_color, wid=wid)
            i += unit

        i = 0
        while(i < size_w):
            start_p = (i, 0)
            end_p = (i, size_h)
            img = do_line(img, start_p, end_p, fill_color,  wid=wid)
            i += unit

    return img, size_w, size_h, unit, interval

def handle_args():
    args = sys.argv
    if len(args) < 2: print USAGE; sys.exit(0)
    
    kw = "w:i:ho:n:a:s:vA:c:"
    opts, strings = getopt.getopt(args[1:], kw)
    infile = outfile = ""
    theme = ""
    fill_color = ""
    wid = interval = 0
    area_list = []

    for x, y in opts:
        if x == '-h': print USAGE; sys.exit(0)
        elif x == '-v': print VERSION; sys.exit(0)
        elif x == '-A':
            if 'v' in y: print VERSION
            if 'h' in y: print USAGE
            if not y == '': sys.exit(0)
        elif x == '-i': infile = y
        elif x == '-c': fill_color = "%s" % y
#        elif x == '-c': fill_color = "#%s" % y
        elif x == '-o': outfile = y
        elif x == '-w': wid = int(y)
        elif x == '-n': interval = int(y)
        elif x == '-s': theme = y
        elif x == '-a':
            s1 = y.split(",")
            if len(s1) < 4: print "'-a' option needs four numbers"; sys.exit(0)
            area_list = [ int(num) for num in s1]

    if infile == "":
        list = os.listdir()
        for item in list:
            if ".jpg" or ".jpeg" in item: infile = item
            break
        if infile == "": print "Please specify the input file"; sys.exit(-1)
    if outfile == "" and infile != "":
        outfile = "%s_%s.jpg" % (infile.split(".")[0], get_time_label2())
    if wid == 0: wid = 1
    if interval == 0: interval = 10
    if len(area_list) == 0: area_list = [0,0,0,0]
    if fill_color == "": fill_color = "00ff00"

    return infile, outfile, wid, interval, area_list, theme, fill_color


def str2tuple(num_str):
    nums = num_str.split(",")
    nums_int = [ int(num) for num in nums]

    return nums_int

def do_crop(img, area):
#	print "area=", area; sys.exit() #debug

	if area == (0,0,0,0): return img
	else: return img.crop(area)

def exec_crop(img, area):
    return do_crop(img, area)

def get_filename(outfile, items):
    f_name = outfile.split(".")[0]

    f_name += "_" + "-".join(items)

    f_name += ".%s" % outfile.split(".")[1]

    return f_name

def variable_length(num, *args):
    print "num=", num
    print "type(num)=", type(num)
    print "args=", args

def do_job():

    infile, outfile, wid, interval, area_list, theme, fill_color = handle_args()
#    #debug
#    c = inspect.currentframe(); print c.f_lineno
#    print fill_color, type(fill_color); sys.exit() #debug
    
#    fill_color = "#%s" % fill_color
#    print fill_color, type(fill_color) ; sys.exit() #debug

    img = Image.open(infile)

    # do line
    img_lined, size_w, size_h, unit, interval = exec_line(
														img, interval, fill_color, wid)

    # do crop
#    print area_list; sys.exit() #debug
    if area_list == [0,0,0,0]:
	    area = (0,0,0,0)
    else:
	    area = (unit*area_list[0],unit*area_list[1], \
			  unit*(size_w/unit - area_list[2]), unit*(size_h/unit - area_list[3]))
    
    img_cropped = exec_crop(img_lined, area)

    if theme == "":
        f_name = get_filename(outfile, \
                  ("thick%d" % wid, "u%d" % unit, \
                    "w%d" % (unit*(size_w/unit)), "h%d" % (unit*(size_h/unit)),\
                    "col%d" % (size_w/unit), "row%d" % (size_h/unit), "n%d" % interval))
    else:
        f_name = get_filename(outfile, \
                  (theme, "thick%d" % wid, "u%d" % unit, \
                    "w%d" % (unit*(size_w/unit)), "h%d" % (unit*(size_h/unit)),\
                    "col%d" % (size_w/unit), "row%d" % (size_h/unit), "n%d" % interval))
#    print "f_name=%s" % f_name; sys.exit(0) #debug

    res = save_imagefile(img_cropped, outfile=f_name)

# execute ========================
if __name__ == '__main__':
    if platform.system() == 'Linux':
        print "Content-Type: text/html"
        print ""

    do_job()
