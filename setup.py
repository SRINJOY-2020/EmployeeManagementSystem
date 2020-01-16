import sys
from cx_Freeze import setup, Executable
import os.path
import Pmw
import MySQLdb
import sqlparse
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","Pmw","sqlparse",'MySQLdb'],'include_files':['tcl86t.dll','tk86t.dll','libmysql.dll','libeay32.dll','ssleay32.dll','diatmlogo.ico','diatm-home-1024x444.jpg']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Employee",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("EmployeeManagementSystem.py", base=base)])