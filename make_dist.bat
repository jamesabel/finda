rmdir /s /q build
rmdir /s /q dist
venv\scripts\python.exe setup.py py2exe
REM venv\scripts\python.exe setup.py sdist
REM venv\scripts\python.exe setup.py bdist_msi