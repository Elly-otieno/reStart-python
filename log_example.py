# import logging

# # Set up logging configuration to log into "app.log" file at DEBUG level
# logging.basicConfig(filename="app.log", level=logging.DEBUG, 
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# def divide(a, b):
#     try:
#         result = a / b
#         logging.debug(f"Dividing {a} by {b}. Result: {result}")
#         return result
#     except ZeroDivisionError:
#         logging.error("Attempted to divide by zero.")
#         return "Error: Division by zero is not allowed."
#     except Exception as e:
#         logging.error(f"An unexpected error occurred: {e}")
#         return f"Error: {str(e)}"

# # Example usage
# print(divide(10, 2))  # Should log the result
# print(divide(10, 0))  # Should log the error for division by zero

import logging

# Configure logging to handle all levels and log them to a file
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,  # Capture all messages from DEBUG level and above
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to divide two numbers and log different levels
def divide(a, b):
    try:
        logging.debug(f"Attempting to divide {a} by {b}.")
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError as e:
        logging.error("Division by zero attempted.", exc_info=True)
        return "Cannot divide by zero!"
    except Exception as e:
        logging.critical(f"Unexpected error occurred: {e}", exc_info=True)
        return "An unexpected error occurred."

# Test the function
if __name__ == "__main__":
    # Example test cases
    divide(10, 2)  # This should log DEBUG and INFO
    divide(10, 0)  # This will log an ERROR
    divide("a", 2)  # This will log a CRITICAL
