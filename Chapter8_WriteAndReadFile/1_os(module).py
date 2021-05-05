# Simple Application for os module
import os 
print(os.path.join('user','bin','spam'))#form a directory

myFiles = ['accounts.txt','details.csv','invite.docx']
for fileName in myFiles:
    print(os.path.join("C:\\Users\\asweigart",fileName))

# get current working directory
print(os.getcwd())

# change current working directory
os.chdir('C:\\Windows\\System32') #if the directory doesn't exist, error happens
print(os.getcwd())

# create new folder
# os.makedirs(path) the folder between the path will be created automatically

# os.path module
# handle absolute path and relative path
print(os.path.abspath('.'))
print(os.path.relpath('C:\\Windows\\System32',os.getcwd()))# os.path.relpath(start directory,end directory)
print(os.path.isabs('.'))# check whether the path is an absolute path

# os.path.basename() os.path.dirname()
# C:\Windows\System32\calc.exe ==> dirname -> C:\Windows\System32 , basename -> calc.exe 
path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.dirname(path))
print(os.path.basename(path))

# split directory -> dirname + basename
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(calcFilePath))# ('C:\\Windows\\System32', 'calc.exe')

print(calcFilePath.split(os.path.sep)) # ['C:', 'Windows', 'System32', 'calc.exe']

# get file size and content in folder
print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
os.listdir('C:\\Windows\\System32') #list all file under the directory -> type:list
total_size = 0 # bit
for filename in os.listdir():
    total_size += os.path.getsize(filename)
print(total_size)

# check whether the path is exist/file/dir
# os.path.isdir() os.path.exists() os.path.isfile() -> return True or False
print(os.path.isdir('C:\\Windows\\System32')) 
print(os.path.exists('C:\\Windows\\System3')) 
print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))