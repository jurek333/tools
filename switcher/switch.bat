@echo off
:: A simple environment switcher by Gynvael Coldwind (assume MIT license).
:: Make sure that you use the full path to the Python executable here, as well
:: as the full path to the switch-worker.py and switch-worker-output.bat.
d:\Python27\python.exe C:\Users\Maciej\tools\switch-worker.py %*
call C:\Users\Maciej\tools\switch-worker-output.bat
