# Read and Write File in Python
# Step.1 call open() -> return file object
# Step.2 call file object's read() write() 
# Step.3 call file object's close() -> close file

File = open("../RomeoAndJuliet.txt")

# Read file -> read() readlines()
'''
print(File.read())
print(File.read(30)) # you can also assign the length
print(File.readlines()) # each string splits with "\n"
print(File.readlines(30)) # you can also assign the length
'''
File.close()

# Write file -> open(path,'w') -> write(content) -> close()

baconFile = open('../bacon.txt','w') # rewrite content
baconFile.write('Hello World!\n')
baconFile.close()
baconFile = open('../bacon.txt','a') # do not rewrite content, append content after the old one
baconFile.write('Hello World!\n')
baconFile.close()
baconFile = open('../bacon.txt') # default 'r'
content = baconFile.read() # return content in txt file
baconFile.close()
print(content) 
