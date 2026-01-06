# Logging Basics
#-----------------------------
import logging

# Setuup Logger
logging.basicConfig(level=logging.ERROR)

# Log Messages
# logging.debug("This is a debug message")                # 10
# logging.info("This is an info message")                 # 20
# logging.warning("This is a warning message")            # 30
# logging.error("This is an error message")               # 40
# logging.exception("This is an exception message")       # 40    <- Includes Except Traceback
# logging.critical("This is a critical message")          # 50

# simple example
a,b = 10, 0

logging.debug(f'Executing: {a}/{b}')
try:
    c = a/b
    logging.info(f'Result: {c}')
except:
    logging.error('Somehing went wrong...')
    
print('Hello World!')