import os,shutil
d=os.path.dirname(os.path.abspath(__file__))
shutil.copyfile(os.path.join(d,'assets','entry.png'), os.path.join(os.getcwd(),'entry.png'))
