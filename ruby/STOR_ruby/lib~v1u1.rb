#!/usr/local/bin/ruby

#file_info

def get_fs_path()
	# 01 =============
	# 02 =============
	cur_dir_l = Dir.pwd.split(File::SEPARATOR)

	#debug
	p cur_dir_l
#	cur_dir_l = os.getcwd().split(os.sep)
	# 03 =============
	ind1 = cur_dir_l.index("www")
#	ind1 = os.getcwd().split(os.sep).index("www")
#	ind1 = cur_dir_l.index("ws_ubuntu_1")
	
	#debug
#	p ind1
#	# 04 =============
	ind2 = cur_dir_l[1..-1].length
#	ind2 = len(cur_dir_l[1:])
	# 05 =============
	return File.join(
				File.join([".."] * (ind2 - ind1)), \
				"html", \
				cur_dir_l[-1])
#	return os.sep.join((
#				os.sep.join([".."] * (ind2 - ind1)), \
#				"html", \
#				cur_dir_l[-1]))

end#get_fs_path()

def get_url_path(fname)
	return File.join(File::SEPARATOR, File.basename(Dir.pwd), fname)
#	return "".join(["%s"]*4) % (os.sep, os.path.basename(os.getcwd()), os.sep, fname)
end#def get_url_path(fname)

def get_time_label()
	return Time.new.strftime("%y%m%d_%H%M%S")
end#def get_time_label()

if $0 == __FILE__ then
	print "Content-Type: text/html\n"
	print "\n"

end#if $0 == __FILE__ then
