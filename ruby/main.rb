#!/usr/local/bin/ruby

#file_info

def get_time_label()
	return Time.new.strftime("%y%m%d_%H%M%S")
end#def get_time_label()

def do_job()
	# do something
end#def do_job()

if $0 == __FILE__ then
	print "Content-Type: text/html\n"
	print "\n"

	do_job()

end#if $0 == __FILE__ then
