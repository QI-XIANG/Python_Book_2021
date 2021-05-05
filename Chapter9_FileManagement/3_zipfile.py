# Simple Application for zipfile module

import zipfile,os

# read from zipfile
os.chdir("..")
exampleFile = zipfile.ZipFile('bacon.zip')
print(exampleFile.namelist())# exampleFile.namelist() -> list all files and folders in the zipfile

# getInfo(filename)
sampleInfo = exampleFile.getinfo('bacon.txt') # return information of the zipfile (ex. file_size, compress_size) 
print("Zipfile's compress size: "+str(sampleInfo.compress_size))
print("Zipfile's original size: "+str(sampleInfo.file_size))
exampleFile.close()

# extract zipfile
# extractall() -> extract all files in the zipfile, extract(filename) -> only extract ordered file 
exampleFile = zipfile.ZipFile('bacon.zip')
exampleFile.extractall() # you can also assign directory like extractall(directory) -> if the folder under the directory doesn't exist, python will auto establish
exampleFile.extractall('C:\\Users\\QiXiang\\Desktop\\2021_Spring')# extract zipfile to assigned directory

exampleFile.extract('bacon.txt') # extract specific file in the zipfile
exampleFile.extract('bacon.txt','C:\\Users\\QiXiang\\Desktop\\2021_Spring')# you can also assign the directory

exampleFile.close()# close zipfile

# establish and add to zipfile
newZip = zipfile.ZipFile('new.zip','w') # first parameter -> zipfile name, 'w' -> write in zipfile (overwrite orignial content), 'a' -> append content (don't overwrite)
newZip.write('bacon.txt',compress_type=zipfile.ZIP_DEFLATED) # write(filename,algorithm for compressing file)
newZip.close()
 




