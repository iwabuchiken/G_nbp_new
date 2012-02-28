@echo off
REM ************************************
REM * <Basics>
REM * 	1. File: makefile_sub1.bat
REM * 	2. Date: 20120218_060625
REM * 	3. Author: Iwabuchi Ken
REM * 	4. Path: C:\workspaces\ws_ubuntu_1\G20111104_083701_C_learn_01\C_jissen_work\Chp_08_work\sub1.bat
REM * <Aim>
REM * 	1.
REM * <Usage>
REM * <Variables>
REM * 	1. trunk
REM * 	2. FILE_PATH
REM * 	3. LIB_FILE_TRUNK
REM * 	4. MYLIB_INCLUDE
REM * <File history>
REM *	1. 
REM ************************************

REM ************************************
REM * Exit if %1 is empty
REM ************************************
if "%1"=="" (
	echo First argument needed for
	echo  the file to be compiled
	echo ^<Example^>
	echo   1.
	echo  ^>makefile_sub1.bat sub1.c
	echo   2.
	echo  ^>makefile_sub1.bat sub1.c N
	echo    =^> "mylib1.obj" is not included
	goto end
)

REM ************************************
REM * Set the module option
REM * => If the option 'N' is set,
REM * 	then "mylib1.obj" is not co-built in. 
REM ************************************
if not "%2"=="" (
	if "%2"=="N" (
		set MYLIB_INCLUDE=false
	) else (
		set MYLIB_INCLUDE=true
	)
) else (
	set MYLIB_INCLUDE=true
)

REM ************************************
REM * Get the trunk from
REM * 	the first argument
REM ************************************
for /f "tokens=1,2 delims=." %%a in ("%1") do (
	set trunk=%%a
)

echo trunk=%trunk%

REM ************************************
REM * Set other variables
REM ************************************
set FILE_PATH=C:\workspaces\ws_ubuntu_1\G20111104_083701_C_learn_01\C_jissen_work\Chp_07_work\exc_7-6
set LIB_FILE=mylib1.c
for /f "tokens=1,2 delims=." %%a in ("%LIB_FILE%") do (
	set LIB_FILE_TRUNK=%%a
)


REM ************************************
REM * Compile "mylib1.c"
REM ************************************
echo bcc32 -c %FILE_PATH%\%LIB_FILE%
bcc32 -c %FILE_PATH%\%LIB_FILE%

rem echo bcc32 -c C:\workspaces\ws_ubuntu_1\G20111104_083701_C_learn_01\C_jissen_work\Chp_07_work\exc_7-6\mylib1.c -omylib1_bcc.obj
REM echo bcc32 -c -omylib1_bcc.obj C:\workspaces\ws_ubuntu_1\G20111104_083701_C_learn_01\C_jissen_work\Chp_07_work\exc_7-6\mylib1.c
REM bcc32 -c -omylib1.obj C:\workspaces\ws_ubuntu_1\G20111104_083701_C_learn_01\C_jissen_work\Chp_07_work\exc_7-6\mylib1.c
rem bcc32 -c C:\workspaces\ws_ubuntu_1\G20111104_083701_C_learn_01\C_jissen_work\Chp_07_work\exc_7-6\mylib1.c -omylib1_bcc.obj

REM ************************************
REM * Compile and link main file
REM * and the object files
REM ************************************
if "%MYLIB_INCLUDE%"=="true" (
	echo bcc32 -I%FILE_PATH% -e%trunk%_bcc.exe %trunk%.c %LIB_FILE_TRUNK%.obj
	bcc32 -I%FILE_PATH% -e%trunk%_bcc.exe %trunk%.c %LIB_FILE_TRUNK%.obj
) else (
	echo bcc32 -I%FILE_PATH% -e%trunk%_bcc.exe %trunk%.c
	bcc32 -I%FILE_PATH% -e%trunk%_bcc.exe %trunk%.c
)
rem echo nmake all /e trunk=%trunk%
rem nmake all /e trunk=%trunk% COMPILER=cl

REM ************************************
REM * Free variables
REM ************************************
set	trunk=
set	FILE_PATH=
set	LIB_FILE=
set LIB_FILE_TRUNK=

REM ************************************
REM * "end" section
REM ************************************
:end
