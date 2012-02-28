@echo off
REM ************************************
REM * <Basics>
REM * 	1. File: bmake.bat
REM * 	2. Date: 20120214_093936
REM * 	3. Author: Iwabuchi Ken
REM * <Aim>
REM * 	1. Execute Borland make
REM * <Usage>
REM * 	<Syntax>
REM * 		bmake calc1_bcc.exe
REM * 			=> make calc1_bcc.exe
REM * <Variables>
REM * 	1. arg1	=> make target
REM * <File history>
REM *	1. Created:
REM ************************************

REM ---------------------------
REM * show help if %1==""
REM ---------------------------
if "%1"=="" (
	echo *USAGE*
	echo bmake calc1_bcc.exe
	goto end
) 

REM ---------------------------
REM * initialize variables
REM ---------------------------
set arg1=

REM ---------------------------
REM * Set target from the command line
REM ---------------------------
set arg1=%1

REM ---------------------------
REM * Execute 'bcc32' command
REM * 1. Arguments can be used up to 6
REM ---------------------------
echo Execute: C:\borland\bcc55\Bin\make %arg1%
C:\borland\bcc55\Bin\make %arg1%

REM ---------------------------
REM * free variables
REM ---------------------------
set arg1=

:end

REM ============ EOF ===================