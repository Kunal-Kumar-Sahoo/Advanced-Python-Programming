"""
Aim: Logging with Exception Handling
"""
import logging

# Configure logging by changing level=logging.__  e.g.logging.ERROR
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s [%(levelname)s]')
# logger = logging.getLogger()
# file_handler = logging.FileHandler('program2.log')
# logger.addHandler(file_handler)


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logging.error("Division by zero error")
        # logger.error("Division by zero error")
    else:
        # logger.info(f"The result is: {result}")
        logging.info(f"The result is: {result}")

# Perform division
divide(10, 2)
divide(10, 0)