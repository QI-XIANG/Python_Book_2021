# Simple Application for webbrower module
import webbrowser,sys,pyperclip
'''
webbrowser.open("https://www.youtube.com/") # auto open the link in your browser
'''
# further application with google maps
if len(sys.argv) > 1:
    #Get address from argv
    address = ' '.join(sys.argv[1:])
else:
    #Get address from pyperclip
    address = pyperclip.paste()

webbrowser.open('https://www.google.com.tw/maps/place/'+address)