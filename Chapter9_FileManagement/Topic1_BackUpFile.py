# Topic 1: backup folder content

#! python3
# Copies an entire folder and its contents into
# a Zipfile whose filename increments

from os.path import basename
import zipfile,os

def backup(folder1):
    # back the entire contents of 'folder' into a zip file
    folder = os.path.abspath(folder1)

    # figure out the filename this code should use based on
    # what files already exists

    number = 1

    while True:
        zipfileName = os.path.basename(folder)+"-"+str(number)+".zip"
        if not os.path.exists(zipfileName):
            break
        number += 1

    # Create the zipfile
    print("Creating... %s" %zipfileName)
    backupZipfile = zipfile.ZipFile(zipfileName,'w')

    # Walk the entire folder tree and compree the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print("Adding files in %s..." %foldername)

        # Add currrent folder to the zip file
        backupZipfile.write(foldername)

        # Add all the files in the folder to the zipfile
        for filename in filenames:
            newbase = os.path.basename(folder)+'_'
            if str(filename).startswith(str(basename)) and str(filename).endswith('.zip'):
                continue # don't backup the zip file
            backupZipfile.write(os.path.join(foldername,filename))
    
    backupZipfile.close()# close the zip file

    print("Done")  

backup('C:\\Users\\QiXiang\\Desktop\\2021_Spring\\Python_Book_Github')
