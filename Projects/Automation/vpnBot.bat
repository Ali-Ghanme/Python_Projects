@echo off
:start
cd \
cd \python%python_ver%\Scripts\
pip install selenium

set count=1
set /p username= Enter The Usernames List Path: 
set /p email= Enter The Email List Path: 

:loop
@REM taskkill /IM psiphon3.exe
@REM taskkill /IM chromedriver.exe

@REM echo "[+] Starting Proxy Services"
@REM cmd.exe /c "start D:\File\Project_Zero\AutoMation_Project\psiphon3.exe"

timeout 6
echo "[+] Starting the Automation process"

:heyman
set /A "x+=%count% "
echo "[*] Starting with user number %x% %input%"
python D:\File\Project_Zero\AutoMation_Project\main.py %1 %username% %2 %email% %3 %x%

echo "[+] Automation don. i will exit now and start with new user <0_0>"
cls
@REM echo "[+] Killing the Vpn"
@REM @REM taskkill /IM psiphon3.exe

goto loop