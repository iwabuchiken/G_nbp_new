@echo off
rem echo %1
rem echo %2
mingw32-make %1 %2 %3
rem dir

rem Example: >mmake laplacian2.o "MACRO_OPT=-DL4"
rem Example: >mingw32-make laplacian2.o MACRO_OPT=-DL4