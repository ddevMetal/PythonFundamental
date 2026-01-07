# Log to File and Console
#------------------------------------
import logging

# Formatting
log_format = """***[%(levelname)s]***
Time: %(asctime)s
Msg: %(message)s
File: %(filename)s Line: %(lineno)d
---------------------------
"""

formatter  = logging.Formatter(log_format)

# Handler 1 - FileHandler
file_handler = logging.FileHandler('ef_app2.log')
file_handler.setFormatter(formatter)

# Handler 2 - StreamHandler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)


# Configure logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)  

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")               


# Recap
#------------------------------------
#Logger -> The main objectst that holds configuration and create loggin messages
#Handler -> Where the log messages go (file, console, etc)
#Formatter -> The layout of the log messages
# Filter* -> Applies filtering on the logs that can pass through