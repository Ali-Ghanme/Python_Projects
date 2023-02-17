@echo off
@REM :loop
@REM set jump=1
@REM :heyman
@REM set /A "x+=%jump%"
@REM if %x%==4 (set /A "jump=1")
@REM timeout 6
@REM echo %x%
@REM if %x% LSS 10 goto heyman
@REM goto :loop

@REM "C:\Python310\python.exe" "D:\File\Project_Zero\AutoMation_Project\main.py" %jump%
@REM set VAR_1=this
@REM set VAR_2=that

@REM python your_script.py %1 %VAR_1% %VAR_2%


@ECHO OFF
SET /P NAME=Enter name:
SET /P GENDER= Enter age:
SET /P AGE= Enter gender:
python D:\File\Project_Zero\AutoMation_Project\main.py %NAME% %GENDER% %AGE%
PAUSE