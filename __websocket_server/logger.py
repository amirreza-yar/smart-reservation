import time
import colorama
from colorama import Fore

colorama.init(autoreset=True)  # Initialize colorama for cross-platform support

# Custom logger function
def log(message, level="INFO", source="General", function=""):
    # Get current timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Define log levels and their corresponding colors
    log_levels = {
        "INFO": Fore.GREEN,
        "DEBUG": Fore.BLUE,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED
    }

    # Get the appropriate color for the log level, default to white for unknown levels
    color = log_levels.get(level, Fore.WHITE)

    # Format the log message with time, level, source, and function name
    formatted_message = f"[{timestamp}] [{level}] [{source}] [{function}]: {message}"

    # Print the colorized log message
    print(color + formatted_message)

# # Example usage
# custom_logger("Connection established", level="INFO", source="WebSocketServer", function="handler")
# custom_logger("Image received and saved", level="DEBUG", source="ImageProcessor", function="save_image")
# custom_logger("Client disconnected unexpectedly", level="ERROR", source="WebSocketServer", function="handler")
# custom_logger("Unable to load image", level="WARNING", source="ImageProcessor", function="load_image")
