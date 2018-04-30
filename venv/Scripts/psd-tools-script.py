#!C:\Users\wongandx\PycharmProjects\PSD_Text_extractor\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'psd-tools2==1.7.6','console_scripts','psd-tools'
__requires__ = 'psd-tools2==1.7.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('psd-tools2==1.7.6', 'console_scripts', 'psd-tools')()
    )
