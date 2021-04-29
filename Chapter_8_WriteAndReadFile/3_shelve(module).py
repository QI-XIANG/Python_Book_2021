# Simple Application for shelve module
# By this module, you can store python variable into the binary shelf file and reuse it

import shelve
shelffile = shelve.open('mydata')
cats = ['Zophie','Pooka','Simon']
shelffile['cats'] = cats # write shelf file as dictionary of python 
shelffile.close()

shelffile = shelve.open('mydata')
type(shelffile)
print(shelffile['cats']) # read variable content from 'cats'

# shelf also has keys() , values() 
# -> return data like list (but it is not real list, you need to change the data type to list)
print(list(shelffile.keys())) # return keys in shelf file
print(list(shelffile.values())) # return values in shelf file
shelffile.close()

# extra information
# Simple Application for pprint module
import pprint
cats = [{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py','w') # not use shelf file to store variable but use python file and pprint module
fileObj.write('cats = '+pprint.pformat(cats)+"\n")
fileObj.close()