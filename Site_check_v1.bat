@ECHO off

@chcp 65001 1> NUL 2> NUL

echo.

@ECHO -----------------------------------------------------------------------------
@ECHO 누리집 체크 스크립트 v.1
@ECHO -----------------------------------------------------------------------------

ECHO.

@ECHO ○ 빅데이터 캠퍼스 누리집 체크
echo.

set url1="https://bigdata.seoul.go.kr/"
set url2="https://cran.seoul.go.kr/"

:_loop

echo %date% %time%
echo.

REM 빅캠 체크

for  /f  "tokens=1  delims=  "  %%a  IN  ('curl -i -s %url1%  ^|  findstr HTTP/1.1')  do  set  result1=%%a

set result11=%result1:~9,3%
set result12=%result1:~13,9%

@echo Bigdata 결과값 : %result11%,%result12%
echo.

if %result11%==200 (
	echo "정상입니다"
	@echo Campus_webpage,%date%,%time%,%result11%,%result12% >> success.log
) else (
	echo "실패입니다"
	@echo Campus_webpage,%date%,%time%,%result11%,%result12% >> fail.log
)

echo.

REM R-cran 체크

for  /f  "tokens=1  delims=  "  %%a  IN  ('curl -i -s %url2%  ^|  findstr HTTP/1.1')  do  set  result2=%%a

set result21=%result2:~9,3%
set result22=%result1:~13,9%

@echo R-Cran 결과값 : %result21%,%result22%
echo.

if %result21%==200 (
	echo "정상입니다"
	@echo Cran_Site,%date%,%time%,%result21%,%result22% >> success.log
) else (
	echo "실패입니다"
	@echo Cran_Site,%date%,%time%,%result21%,%result22% >> fail.log
)
echo.

timeout 10 > NUL

goto _loop