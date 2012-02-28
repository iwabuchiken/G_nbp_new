@echo off
REM ************************************
REM * <Basics>
REM * 	1. File: ru.bat
REM * 	2. Date: 20120222_072611
REM * 	3. Author: Iwabuchi Ken
REM * <Aim>
REM * 	1. Execute rutil.rb
REM * <Usage>
REM * 	1. Arguments can be used up to 6
REM * 	2. command: ru <ruby file name>
REM * <Variables>
REM * 	1.
REM * <File history>
REM *	1. Created: 
REM *
REM ************************************
REM echo off

REM ************************************
REM * No argument => show usage
REM ************************************
if "%1"=="" (
	echo ^<Usage^>
	echo   ru t
	echo   =^> rtuil.py t
	goto end
)

REM ***************************************
REM * Execute 'rutil.rb' command
REM * 1. Arguments can be used up to 6
REM ***************************************
echo Execute: rutil.rb %1 %2 %3 %4 %5 %6
rutil.rb %1 %2 %3 %4 %5 %6

REM ************************************
REM * :end
REM ************************************
:end

REM ============ EOF ===================