# Simple Application for shutil module
# hint: if you want to test the following code, please just test one block at once
#=============================================================================================================================================================================
import shutil,os

os.chdir("..")# change to the directory that the copied file exists

# hint: the destination path needed to have been created

# copy file to specific directory (folder)
# shutil.copy(source,destination)
shutil.copy('bacon.txt','C:\\Users\\QiXiang\\Desktop\\2021_Spring')# if the bacon.text exists in the destination directory, an error will happen
shutil.copy('bacon.txt','C:\\Users\\QiXiang\\Desktop\\2021_Spring\\bacon2.txt')# copy file to ordered directory and rename the file

#=============================================================================================================================================================================#
# move file to specific directory (folder)
# shutil.move(source,destination)
shutil.move('bacon.txt','C:\\Users\\QiXiang\\Desktop\\2021_Spring')# hint: you can't move the file with same name to the current directory, error will happen if you doing so
shutil.move('bacon.txt','C:\\Users\\QiXiang\\Desktop\\2021_Spring\\bacon3.txt')# move and rename the file

#=============================================================================================================================================================================#
# permanently delete file and folder
# we should check again before we delete the file and folder
# os.unlink(filename)
import os
for filename in os.listdir():
    if filename.endswith('txt'):
        #os.unlink('.txt')
        print(filename)

#=============================================================================================================================================================================#
# delete file and folder but recyclable
# send2trash module -> pip install send2trash (type under command line)
import send2trash
baconfile3 = open('bacon.txt','a')
baconfile3.write('Bacon is not a vegetable.')
baconfile3.close()
send2trash.send2trash('bacon.txt')

#=============================================================================================================================================================================#



