import shutil
from shutil import copy
import os
import shutil
from os import walk
from os.path import join
import time

#Locat the current working directory to the given path
os.chdir('given path')
or_mypath = "given path"#original folder path
tg_mypath = "given path"#target folder path

#Move files
def move(tf1):
   f1=join(or_mypath,tf1)
   f2=join(tg_mypath,tf1)
   try:
      shutil.copyfile(f1,f2)
      print('File [',tf1,'] is moved successfully')
      
      delete(f1)
      
   except OSError as e:
       print(e)

#Delete files after moving
def delete(df1):
    try:
        os.remove(df1)
    except OSError as e:
        print(e)
    else:
        print("File is deleted successfully")




#Loop all paths
for root, dirs, files in walk(or_mypath):
  for f in files:
    fullpath = join(root, f)
    #print(fullpath)

#Check if empty
if not files:
    print("Empty")
else:
    print("Files Not Empty")

    for i in files:
        print('moving')
        move(i)

