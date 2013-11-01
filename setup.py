
from cx_Freeze import setup, Executable

base = "Console"

setup(
    name = "finda",
    version = "0.0",
    author='James Abel',
    author_email='j@abel.co',
    url='www.abel.co',
    license='LICENSE',
    description = "finder program",
    long_description="searches 1 or more paths for 1 or more strings",
    py_modules=['*'],
    platforms=['windows'],
    executables = [Executable("finda.py", base=base)]
)