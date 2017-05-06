REM py2exe is apparently still only at Python 3.4
c:\Python34\python.exe -m venv --clear venv
venv\Scripts\pip3 install -U pip
venv\Scripts\pip3 install -U setuptools
venv\Scripts\pip3 install -r requirements.txt
