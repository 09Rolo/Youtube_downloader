@echo off

:main
cls

cd %cd%
python YoutubeDownload.py

echo.
echo Nyomj meg egy gombot a folytatashoz
pause>nul
:ujravagynem
cls
echo.
echo.
echo Szeretnel meg egy dolgot letolteni?(i/n)
set /p input=">> "

if %input% == i ( goto main) else ( goto leallito )

:leallito
cls
echo.
echo A kilepeshez nyomj meg egy gombot
pause>nul
start %cd%