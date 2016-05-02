from cx_Freeze import setup, Executable
import sys

build_exe_options = {"packages": ["os"], "includes": [""], "excludes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = 'zillow_scrape',
    version = '1',
    description = '.',
    executables=[Executable('zillow_scrape.py', base=base)],
    options={"build_exe":build_exe_options},
)
