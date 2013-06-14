def get_time_label(format=0)
    
    if format == 0
      
        return Time.now.strftime("%Y%m%d_%H%M%S")
      
    else
        
        #REF http://stackoverflow.com/questions/7415982/how-do-i-get-the-current-date-time-in-dd-mm-yyyy-hhmm-format answered Sep 14 '11 at 
        return Time.now.strftime("%d/%m/%Y %H:%M:%S")
        
    end
  
end#def get_time_label(format=0)


def show_help
    
    puts "<Usage>"
    
    puts "r [Options]<-t><-t2>"
    
    puts
    
    puts "    -t	Get time label: 20130614_081234"
    puts "    -t2	Get time label: 14/06/2013 08:12:34"
    
end#def show_help

def arg_t(format=0)
    
    puts get_time_label(format)
    
    # puts "Show time"
    
end

def do_something
    
    if ARGV.length < 1
      
        show_help()
        
        exit
    
    # elif ARGV[0] == "-t"
    elsif ARGV[0].chomp == "-t"
        
        arg_t(0)
        
        exit
        
    elsif ARGV[0].chomp == "-t2"
        
        arg_t(1)
        
        exit
        
    else
      
        puts "Unknown option: #{ARGV[0]} ==> ?"
        
        exit
      
    end
    
    # puts ARGV
    p ARGV
    
end

do_something
