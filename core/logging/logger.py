import logging

class Logger:
    def __init__(self, context: str):
        self._logger = logging.getLogger(context)

    def log(self, message: str):
        self._logger.info(message)

    def warn(self, message: str):
        self._logger.warning(message)

    def error(self, message: str, exc: Exception | None = None):
        if exc:
            self._logger.error(message, exc_info=exc)
        else:
            self._logger.error(message)
