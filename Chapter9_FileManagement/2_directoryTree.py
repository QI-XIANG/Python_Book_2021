# Simple Application for os module

# visit the directory tree with os module
# os.walk(start) -> return foldername,subfolders,filenames
import os
for foldername,subfolders,filenames in os.walk('C:\Windows\System32'):
    print('The current folder is '+foldername)

    for subfolder in subfolders:
        print("SUBFOLDER OF "+foldername+": "+subfolder)

    for filename in filenames:
        print("FILE INSIDE "+foldername+": "+filename)
 