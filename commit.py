import os
import sys
import shutil
os.system("git add .")
os.system(f"git commit -m \"{sys.argv[1]}\"")
os.system("git push")
shutil.copy(os.getcwd() + "/engine.py", os.getcwd() + "/lichess-bot")