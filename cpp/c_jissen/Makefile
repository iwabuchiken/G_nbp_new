TRUNK	=
EXE		= .exe
OBJ		= .obj
SRC		= .c
CC		= cl
COMPILER	= 
CFLAG	= 
FILES	= mylib1
MACRO	=
#INCLUDE_PATH	=  C:\workspaces\ws_ubuntu_1\G20111104_083701_C_learn_01\C_jissen_work\Chp_07_work\exc_7-6
#INCLUDE_STD	= "c:\Program Files\Microsoft Visual Studio 10.0\VC\INCLUDE;C:\Program Files\Microsoft SDKs\Windows\v7.0A\include;"

#all:$(TRUNK)_$(CC)$(EXE)
#all:$(TRUNK)$(EXE)
all: $(TRUNK)_$(COMPILER)$(EXE)

#$(TRUNK)_$(COMPILER)$(EXE): $(TRUNK)_$(COMPILER)$(OBJ) $(FILES)$(OBJ)
$(TRUNK)_$(COMPILER)$(EXE): $(TRUNK)$(OBJ) $(FILES)$(OBJ)
	$(CC) /Fe$(TRUNK)_$(COMPILER)$(EXE) \
			$(TRUNK)$(OBJ) $(FILES)$(OBJ)
