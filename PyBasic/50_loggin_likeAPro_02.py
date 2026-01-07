# Logging Basics"
#   - Logging into a file
#---------------------------------------------------
import logging


# Log to a file without console
# Setuup Logger
# log_format = '%(asctime)s - %(levelname)s - %(message)s'
log_format = """***[%(levelname)s]***
Time" %(asctime)s
Msg: %(message)s
File: %(filename)s Line: %(lineno)ds
------------------------------------------------------"""
logging.basicConfig(level=logging.DEBUG, 
                    filename='ef_app.log',
                    format=log_format)







# log messages
logging.debug('This is a debug message2')
logging.info('This is an info message2')
logging.warning('This is a warning message2')


print('Where are our log messages?')


