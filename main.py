import os
import shutil

_here = os.path.dirname(os.path.abspath(__file__))
_src = os.path.join(_here, "assets", "entry.png")
_dst = os.path.join(os.getcwd(), "entry.png")
shutil.copyfile(_src, _dst)
print("entry.png written to", _dst)
