####################################`
# <Basics>
# => 1. File: rutil.rb
# => 2. Author: Iwabuchi Ken
# => 3. Date: 20120212_071729
# Aim:
#  1.
# <Usage>
#  1. Run the program
# <Source>
# => 1. to_s  => http://yiaowang.web.fc2.com/programing/ruby_base/syntax_variable.html
# => 2. ARGV  => http://www2.atwiki.jp/kmo2/pages/16.html
# => 3. 例外処理  => http://www.namaraii.com/rubytips/?%CE%E3%B3%B0
# => 4. mkdir => http://www.namaraii.com/rubytips/?%A5%C7%A5%A3%A5%EC%A5%AF%A5%C8%A5%EA#l1
# => 5. heredocument => http://www.rubylife.jp/ini/string/index4.html
# => 6. Dir.pwd => http://www.ruby-forum.com/topic/128143
# => 7. if statement => http://doc.ruby-lang.org/ja/1.9.3/doc/spec=2fcontrol.html#if
####################################

def do_something
  puts "do_something"
  puts "Hi."
  puts __FILE__  
end#def do_something

############################
# => get_time_string
# <return>
# 1.
############################
def get_time_string
  # get a time object ###
  t = Time.now
  ### create: month string  ###
  month = (t.month.to_s.length == 1) ? 
            "0" + t.month.to_s : t.month.to_s
  ### create: day string  ###
  day = (t.day.to_s.length == 1) ? 
            "0" + t.day.to_s : t.day.to_s
  hour = (t.hour.to_s.length == 1) ? 
            "0" + t.hour.to_s : t.hour.to_s
  min = (t.min.to_s.length == 1) ? 
            "0" + t.min.to_s : t.min.to_s
  sec = (t.sec.to_s.length == 1) ? 
            "0" + t.sec.to_s : t.sec.to_s
  ### integrate all the data  ###
  string = t.year.to_s + month + day +
           "_" + hour + min + sec
  
  ### return value  ###
  return string
  
end#get_time_string

############################
# => create_folders
# <return>
# 1. -1 => Can't create folders
# 2. 1  => Created
############################
def create_folders
  ### variables ###
  stor_dir_path = "STOR_" + File.basename(__FILE__)
  
  ### create dirs ###
  begin
    ### dir: log  ###
    Dir::mkdir("log")
    puts "Dir created: " + "log"
    
    ### dir: log  ###
    #Dir::mkdir("STOR_" + dir_suffix)
    Dir::mkdir(stor_dir_path)
    puts "Dir created: " + stor_dir_path
    
    ### return  ###
    return 1
  rescue
    puts "Can't create folders"
    return -1
  end
end#def create_folders

def show_usage
  puts <<"EOS"
  <Usage>
  rutil.py md
    => Create dirs: log, STOR_XXX
  <Options>
    
EOS
end#def show_usage

def handle_options
  if ARGV[0] == "md"
    create_folders
  elsif ARGV[0] == "t"
    print get_time_string
  end#if ARGV[0] == "md"

end#def handle_options

if $0 == __FILE__
  if ARGV.length < 1
    show_usage
  else
    handle_options
  end
#  puts "ARGV.length=", ARGV.length
#  puts "ARGV.length=" + ARGV.length.to_s
#  puts "main."
#  puts File.basename(__FILE__)
#  puts File.dirname(__FILE__)
#  puts "Dir.pwd=" + Dir.pwd
  ### create folders  ###
  #create_folders
#  Dir::mkdir("log")
#  #Dir::mkdir("STOR_" + Dir.pwd)
#  Dir::mkdir("STOR_" + File.basename(Dir.pwd))
  
end#if $0 == __FILE__
