# get all png path in this directory and store it in variable called files
import os
from glob import glob
import shutil

files = []
start_dir = os.getcwd()
pattern   = "*.png"
dst_dir=os.getcwd()

for dir,_,_ in os.walk(start_dir):
    files.extend(glob(os.path.join(dir,pattern))) 

# copy the file to the destination directory dst_dir
for file in files:
    shutil.copy(file, dst_dir)