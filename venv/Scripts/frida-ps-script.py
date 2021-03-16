#!C:\Users\นฺย๙มุ\PycharmProjects\ch4njun3\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'frida-tools==5.1.0','console_scripts','frida-ps'
__requires__ = 'frida-tools==5.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('frida-tools==5.1.0', 'console_scripts', 'frida-ps')()
    )
