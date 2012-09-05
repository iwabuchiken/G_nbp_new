CC = g++

cgi_test.exe: do_cgi.cpp
	$(CC) -o $@ $^
#	g++ -o $@ $^

cp0102.exe: cp0102.cpp
	$(CC) -o $@ $^

all: cgi_test.exe cp0102.exe

clean:
	rm *.exe

clean_win:
	del *.exe
