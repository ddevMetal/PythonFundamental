# ============================================
# CUSTOM LOGGER - Send Logs to Discord Webhook
# ============================================
# This skeleton demonstrates how to create a custom logging handler
# that sends log messages to external services (Discord in this case)

import logging, requests

# ============================================
# STEP 1: CONFIGURATION - Webhook URL
# ============================================
# Webhook - is a way for apps to communicate using HTTP POST requests
# We send JSON data to this URL, and Discord receives/displays our logs
WEBHOOK_DISCORD = "https://discordapp.com/api/webhooks/1458294981239246999/SRO_dqgOvnkjOu0f0z33zTMndqqgLENFBSnCW9fn-rsqUZdJzEc9FGdBKRXlzYbXCy6K"

# ============================================
# STEP 2: CUSTOM HANDLER - Core Component
# ============================================
# Key: Inherit from logging.Handler and override emit() method
class CustomHandler(logging.Handler):
    """Custom handler that sends log messages to Discord webhook"""
    
    def emit(self, record):
        """
        This method is called automatically whenever a log is generated
        Args:
            record: LogRecord object containing all log information
        """
        # Format the log record using the assigned formatter
        log_entry = self.format(record)
        
        # Send the formatted log to Discord
        try:
            response = requests.post(WEBHOOK_DISCORD, json={"content": log_entry})
            response.raise_for_status()  # Raise exception if request failed
        except requests.exceptions.RequestException as e:
            print(f'Failed to send log to Discord: {e}')

# ============================================
# STEP 3: FORMATTER - Define Log Format
# ============================================
# This controls how the log message looks
log_format="""***[%(levelname)s]***
Time: %(asctime)s
Msg: %(message)s
File: %(filename)s Line: %(lineno)d
-------------------------------------------------"""
formatter = logging.Formatter(log_format)

# ============================================
# STEP 4: INSTANTIATE HANDLER & APPLY FORMATTER
# ============================================
# Create an instance of our custom handler and attach the formatter
custom_handler = CustomHandler()
custom_handler.setFormatter(formatter)  # Links the formatter to the handler

# ============================================
# STEP 5: CONFIGURE LOGGER
# ============================================
# Create a named logger, set its level, and attach our custom handler
logger_ef = logging.getLogger("EF")        # Create/get logger named "EF"
logger_ef.setLevel(logging.DEBUG)          # Set minimum log level
logger_ef.addHandler(custom_handler)       # Attach our custom handler

# ============================================
# STEP 6: USE THE LOGGER - Generate Logs
# ============================================
# Now any log messages will be sent to Discord via our custom handler
logger_ef.debug("This is a debug message")
for i in range(10):
    logger_ef.warning('Attempt {}/10: Something went wrong!')