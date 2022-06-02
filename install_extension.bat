@echo off

call "%~dp0tools\packman\python.bat" %~dp0tools\scripts\install_extension.py i %*
if %errorlevel% neq 0 ( goto Error )

:Success
exit /b 0

:Error
exit /b %errorlevel%
