import sys
import traceback
from types import ModuleType
import logging

def error_message_detail(error: Exception, error_detail: ModuleType) -> str:
    """
    Generate detailed error message including filename, line number, and function name.
    
    :param error: The exception raised or error message
    :param error_detail: Module instance (sys) used to retrieve traceback information
    :return: Formatted error message string
    """
    _, _, exc_tb = error_detail.exc_info()
    
    # Extract traceback information
    file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "unknown"
    line_number = exc_tb.tb_lineno if exc_tb else 0
    function_name = exc_tb.tb_frame.f_code.co_name if exc_tb else "unknown"
    
    # Handle exception or string as the error parameter
    error_message = (
        f"Error: {error}\n"
        f"Location: file '{file_name}', line {line_number}, in {function_name}\n"
        f"Full traceback: {traceback.format_exc()}"
    )
    
    return error_message

class CustomException(Exception):
    def __init__(self, error: Exception, error_detail: ModuleType):
        """
        Initialize the custom exception with detailed error information
        
        :param error: The caught exception or error description
        :param error_detail: Module instance (sys) to extract traceback details
        """
        self.error_message = error_message_detail(error, error_detail)
        super().__init__(self.error_message)
        
    def __str__(self):
        return f"CustomException: {self.error_message}"