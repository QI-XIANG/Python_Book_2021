#! python3
# copy file with end with .jpg to a new folder
import shutil,os

def copySfile(StartPath):
    Path = os.path.abspath(StartPath)
    for folder,subfolders,filenames in os.walk(Path):
        
        for filename in filenames:
            if str(filename).endswith('.jpg'):
                filePath = os.path.join(folder,filename)
                os.chdir('C:\\Users\\QiXiang\\Desktop\\newFolder')
                if os.path.exists(filename): # do not copy the file with same name
                    continue
                shutil.copy(filePath,'C:\\Users\\QiXiang\\Desktop\\newFolder')

copySfile('C:\\Users\\QiXiang\\Desktop')# assign beginning path
