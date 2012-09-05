@echo off
REM ************************************
REM * <Basics>
REM * 	1. File: jc.bat
REM * 	2. Date: 20120209_155548
REM * 	3. Author: Iwabuchi Ken
REM * <Aim>
REM * 	1. Execute java source file
REM * <Usage>
REM * 	1. Arguments can be used up to 6
REM * 	2. command: j <class file name>
REM * <Variables>
REM * 	1. arg1
REM * 	2. trunk
REM * <File history>
REM *	1. Created: 20120209_155548
REM ************************************
REM echo off

REM ---------------------------
REM * Set file name from the command line
REM * arguments
REM ---------------------------
set arg1=%1

REM ---------------------------
REM * Set the extensoin
REM ---------------------------
set ext=.java

REM ---------------------------
REM * Get the trunk from the file name
REM * 1. Number of tokens => 2
REM * 2. delimiters => '.'

REM ---------------------------

for /f "tokens=1,2 delims=." %%a in ("%arg1%") do (
	set trunk=%%a
)

REM ---------------------------
REM * Execute 'javac' command
REM * 1. Arguments can be used up to 6
REM ---------------------------
echo Execute: javac %trunk%%ext% %2 %3 %4 %5 %6
javac %trunk%%ext% %2 %3 %4 %5 %6

REM ============ EOF ===================