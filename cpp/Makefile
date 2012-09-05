#file_info

CC = gcc
CXX = g++
EXECEXT = .exe
SRCEXT_C = .c
SRCEXT_CXX = .cpp
OBJEXT = .o
HEADEXT = .h
MAINFILE = main

T1 = $(MAINFILE)$(EXECEXT)
IN1 = $(MAINFILE)$(SRCEXT_C)
IN2 = $(MAINFILE)$(SRCEXT_CXX)
OBJ1 = $(MAINFILE)$(OBJEXT)
H1 = $(MAINFILE)$(HEADEXT)
CMPOPT = -o
#IOPT = -I./include

$(T1): $(OBJ1)
	$(CC) $(IOPT) $(CMPOPT) $@ $^

.PHONY: all
all: $(T1)

.PHONY: clean
clean:
	rm *.exe
clean_all:
	rm *.o
	rm *.exe

clean_all_win:
	del *.o
	del *.exe

clean_o:
	rm *.o

.PHONY: clean_win
clean_win:
	del *.exe

.PHONY: clean_win_o
clean_win_o:
	del *.o

.PHONY: show
show:
	echo \<clean clean_all clean_all_win clean_o clean_win clean_win_o\>\<all $(T1)\>
