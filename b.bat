@echo off
REM ************************************
REM * <Basics>
REM * 	1. File: b.bat
REM * 	2. Date: 20120212_141418
REM * 	3. Author: Iwabuchi Ken
REM * <Aim>
REM * 	1. Execute "bcc32" command
REM * <Usage>
REM * 	<Syntax>
REM * 		b sub1.c
REM * 			=> sub1_bcc.exe
REM * <Variables>
REM * 	1. trunk
REM * 	2. file_name
REM * <File history>
REM *	1. Created: 20120212_141418
REM ************************************

REM ---------------------------
REM * show help if %1==""
REM ---------------------------
if "%1"=="" (
	echo *USAGE*
	echo b ^<file name^> ^<options^>
	echo ^(Example^)
	echo b transfer_time.c -DD
	echo    =^> bcc32 -DD -etransfer_time_bcc.exe transfer_time.c
	goto end	
) 

REM ---------------------------
REM * initialize variables
REM ---------------------------
set trunk=
set file_name=

REM ---------------------------
REM * Set file name from the command line
REM * arguments
REM ---------------------------
set file_name=%1

REM ---------------------------
REM * Get the trunk from the file name
REM * 1. Number of tokens => 2
REM * 2. delimiters => '.'

REM ---------------------------

for /f "tokens=1,2 delims=." %%a in ("%file_name%") do (
	set trunk=%%a
)

echo file_name=%file_name%
echo trunk=%trunk%

REM ---------------------------
REM * Execute 'bcc32' command
REM * 1. Arguments can be used up to 6
REM ---------------------------
echo Execute: bcc32 %2 -e%trunk%_bcc.exe %file_name%
bcc32 %2 -e%trunk%_bcc.exe %file_name%

REM ---------------------------
REM * free variables
REM ---------------------------
set trunk=
set file_name=

:end

REM ============ EOF ===================