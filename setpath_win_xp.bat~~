@echo off
REM ************************************
REM * <Basics>
REM * 	1. File: setpath_win_xp.bat
REM * 	2. Date: 20120225_093943
REM * 	3. Author: Iwabuchi Ken
REM * <Aim>
REM * 	1.
REM * <Usage>
REM * 	1.
REM * <Variables>
REM * 	1.
REM * <File history>
REM *	1.
REM ************************************
REM echo off

REM ************************************
REM * No argument => show usage
REM ************************************
rem if "%1"=="" (
rem 	echo ^<Usage^>
rem 	echo   setpath_win_xp
rem 	goto end
rem )

REM ************************************
REM * Set variables
REM ************************************
set GIT_HOME_BIN=C:\WORKS\PROGRAMS\Git\bin
set NBP_HOME=C:\WORKS\WORKSPACES\G_nbp_new
set PYTHON_HOME=C:\WORKS\PROGRAMS\Python266
set PYTHONPATH=C:\WORKS\PROGRAMS\Python266
set JAVA_HOME=C:\WORKS\PROGRAMS\Java
set JAVA_HOME_BIN=%JAVA_HOME%\jdk1.6.0_25\bin
set MINGW_HOME_BIN=C:\WORKS\PROGRAMS\MinGW\bin;

REM set PATH_TO_ALL=%GIT_HOME_BIN%;%NBP_HOME%;%PYTHON_HOME%;%JAVA_HOME%;%JAVA_HOME_BIN%;%MINGW_HOME_BIN%

REM ************************************
REM * Set paths
REM ************************************
echo set path=%%path%%;%GIT_HOME_BIN%
set path=%path%;%GIT_HOME_BIN%

echo set path=%%path%%;%NBP_HOME%
set path=%path%;%NBP_HOME%

echo set path=%%path%%;%PYTHON_HOME%
set path=%path%;%PYTHON_HOME%

echo set path=%%path%%;%JAVA_HOME%
set path=%path%;%JAVA_HOME%

echo set path=%%path%%;%JAVA_HOME_BIN%
set path=%path%;%JAVA_HOME_BIN%

echo set path=%%path%%;%MINGW_HOME_BIN%
set path=%path%;%MINGW_HOME_BIN%

echo set path=%%path%%;%PYTHONPATH%
set path=%path%;%PYTHONPATH%

rem set path=%path%;%NBP_HOME%

:end
REM ============ EOF ===================