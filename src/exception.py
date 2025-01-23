import sys
from logger import logging
import traceback

def error_message_detail(error):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    
    tb_details = traceback.extract_tb(exc_traceback)
    
    if tb_details:
        last_tb = tb_details[-1]
        file_name = last_tb.filename
        line_number = last_tb.lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"
    
    type_name = exc_type.__name__ if exc_type else "Unknown"
    
    error_message = (
        f"Error Details:\n"
        f"File: {file_name}\n"
        f"Line: {line_number}\n"
        f"Type: {type_name}\n"
        f"Error: {str(error)}"
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error=None):
        if error is None:
            error = sys.exc_info()[1]
        
        super().__init__(error_message)
        self.error_message = error_message_detail(error)
    
    def __str__(self):
        return self.error_message