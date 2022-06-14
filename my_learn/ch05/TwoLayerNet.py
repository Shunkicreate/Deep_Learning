import sys, os
from os.path import dirname, abspath
parent_dir = dirname(dirname(abspath(__file__))) # 追加
if parent_dir not in sys.path: # 追加
    sys.path.append(parent_dir) # 追加