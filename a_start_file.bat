@ECHO OFF
REM ************************************
REM *
REM *	Set vars
REM *
REM ************************************

REM *********************
REM *	1. Git
REM *	2. nbp_new
REM *	3. Python
REM *	4. Java
REM *	5. Sakura
REM *	
REM *********************
ECHO Setting a var: SAKURA_HOME=C:\WORKS\PROGRAMS\sakura
SET SAKURA_HOME=C:\WORKS\PROGRAMS\sakura

ECHO Setting a var: JAVA_HOME=C:\WORKS\PROGRAMS\Java
SET JAVA_HOME=C:\WORKS\PROGRAMS\Java

ECHO Setting a var: GIT_CMD=C:\WORKS\PROGRAMS\msysgit\cmd
SET GIT_CMD=C:\WORKS\PROGRAMS\msysgit\cmd

ECHO Setting a var: NBP_NEW=C:\WORKS\WS\G_nbp_new
SET NBP_NEW=C:\WORKS\WS\G_nbp_new

ECHO Setting a var: PYTHON_HOME=C:\WORKS\PROGRAMS\Python27
SET PYTHON_HOME=C:\WORKS\PROGRAMS\Python27


REM ************************************
REM *
REM *	Set path
REM *
REM ************************************

REM *********************
REM *	1. Git
REM *	2. nbp_new
REM *	3. Python
REM *	4. Java
REM *	5. Sakura
REM *	
REM *********************
ECHO Modifying path: %%PATH%%;%SAKURA_HOME%;
PATH=%PATH%;%SAKURA_HOME%;

ECHO Modifying path: %%PATH%%;%JAVA_HOME%;
PATH=%PATH%;%JAVA_HOME%;

ECHO Modifying path: %%PATH%%;%GIT_CMD%;
PATH=%PATH%;%GIT_CMD%;

ECHO Modifying path: %%PATH%%;%NBP_NEW%;
PATH=%PATH%;%NBP_NEW%;

ECHO Modifying path: %%PATH%%;%PYTHON_HOME%;
PATH=%PATH%;%PYTHON_HOME%;

