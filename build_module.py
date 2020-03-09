import os, sys

sys.path.append(os.curdir)

os.chdir('./processes')

from processes.init import process_init

process_init()