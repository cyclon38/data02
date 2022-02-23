@echo off						&: 배치 파일 시작하기
title Task_kill_v.1						&: 창 타이틀 넣기
setlocal

@chcp 65001 1> NUL 2> NUL

echo.

@ECHO -----------------------------------------------------------------------------
@ECHO Task_kill_v.1 LIST
@ECHO -----------------------------------------------------------------------------

ECHO.

tasklist /FI "IMAGENAME eq Calculator*"
tasklist /FI "IMAGENAME eq YourPhone*"
tasklist /FI "IMAGENAME eq LockApp*"
tasklist /FI "IMAGENAME eq igfxEM*"
REM tasklist /FI "IMAGENAME eq scheduler*"
echo.

taskkill /F /IM Calculator.exe
taskkill /F /IM YourPhone.exe
taskkill /F /IM LockApp.exe
taskkill /F /IM igfxEM.exe
REM taskkill /F /IM scheduler.exe /T

pause