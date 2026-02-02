import logging
from datetime import datetime

class ColoredFormatter(logging.Formatter):
    COLORS = {
        "INFO": "\033[92m",     # Verde
        "WARNING": "\033[93m",  # Amarillo
        "ERROR": "\033[91m",    # Rojo
        "RESET": "\033[0m",
    }

    def format(self, record):
        levelname = record.levelname
        color = self.COLORS.get(levelname, self.COLORS["RESET"])
        reset = self.COLORS["RESET"]

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = record.getMessage()

        return (
            f"{color}"
            f"[{timestamp}] "
            f"[{levelname}] "
            f"{record.name}: "
            f"{message}"
            f"{reset}"
        )
