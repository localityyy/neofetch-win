@echo off
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo neofetch-win installer requires admin privileges.
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

set SCRIPTS_PATH=C:\Scripts
set disk=C:\
mkdir "%SCRIPTS_PATH%"
if not exist "%SCRIPTS_PATH%\neofetch.bat" (
    echo @echo off > "%SCRIPTS_PATH%\neofetch.bat"
    echo py "%SCRIPTS_PATH%\neofetch.py" >> "%SCRIPTS_PATH%\neofetch.bat"
    echo neofetch.bat was successfully created.
) else (
    echo neofetch.bat already exists. 
)


echo %PATH% > "%disk%\path_backup.txt"
echo backup was successfully created.


echo adding path...
for /f "tokens=*" %%A in ('reg query "HKCU\Environment" /v Path') do (
    set "cpath=%%A"
)
set "cpath=%cpath:*Path    REG_EXPAND_SZ    =%"

echo %cpath% | find /i "%SCRIPTS_PATH%" >nul
if %errorlevel%==0 (
    echo path already exists, you dont need to run this.
) else (
    set "npath=%cpath%;%SCRIPTS_PATH%"
    reg add "HKCU\Environment" /v Path /t REG_EXPAND_SZ /d "%npath%" /f
    echo path was successfully added.
    echo now move neofetch.py to %SCRIPTS_PATH% folder
    echo then 
)

pause
