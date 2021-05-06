#! python3
# Simple Application of logging module

#==================================================================================================================================================#
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s') # get detail information of LogRecord

logging.debug('Start of program') # call basicConfig() to print message and the message will follow the format above

def factorial(n):
    logging.debug('Start of factorial(%s)' %(n))# set part of %(message)s
    total = 1
    for i in range(n+1): # range should start from 1
        total *= i
        logging.debug('i is '+str(i)+', total is '+str(total))# set part of %(message)s
    logging.debug('End of factorial(%s)' %(n))# set part of %(message)s
    return total

print(factorial(5))
logging.debug('End of program')# set part of %(message)s

#==============================================================================================================================================================#
# hint: do not use print() to debug, because you need to delete these messages manually
# hint: logging.disable(logging.CRITICAL) -> disable the logging -> more convenient than  print()

# logging 
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s') , if you set level=logging.DEBUG, you will see other higher level
# 1.DEBUG -> logging.debug() low level
# 2.INFO -> logging.info() # if you set level=logging.INFO, you will not see other lower level
# 3.WARNING -> logging.warning()
# 4.ERROR -> logging.error()
# 5.CRITICAL -> logging.critical() high level

logging.basicConfig(level=logging.ERROR,format='%(asctime)s - %(levelnme)s - %(message)s')
logging.debug('Some Debug Details')
logging.info('Some Info Details')
logging.warning('Some Warning Details')
logging.error('Some Error Details')
logging.critical('Some Critical Details')

#===================================================================================================================================================#
# Disable logging
logging.disable(logging.ERROR) # disable lower level from logging.ERROR (included)
logging.debug('Some Debug Details')
logging.info('Some Info Details')
logging.warning('Some Warning Details')
logging.error('Some Error Details')
logging.critical('Some Critical Details')

#==================================================================================================================================================#
# write logging message to file

logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some Debug Details')
logging.info('Some Info Details')
logging.warning('Some Warning Details')
logging.error('Some Error Details')
logging.critical('Some Critical Details')



