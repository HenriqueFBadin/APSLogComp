@echo off
setlocal

REM Verifica se o argumento foi passado
if "%~1"=="" (
    echo Uso: ./tester.bat arquivo.mus
    exit /b 1
)

REM Nome base sem extensão
set "FILE=%~1"
for %%F in ("%FILE%") do set "BASE=%%~nF"

python main_adaptado.py %FILE%
llc -filetype=obj %BASE%.ll -o %BASE%.o
gcc -c personalized_functions.c -o personalized_functions.o
gcc %BASE%.o personalized_functions.o -o %BASE%.exe
%BASE%.exe

pause