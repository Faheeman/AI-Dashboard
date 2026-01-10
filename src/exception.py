import sys
import traceback

class CustomException(Exception):
    def __init__(self, error: Exception):
        self.error_message = "".join(
            traceback.format_exception(
                etype=type(error),
                value=error,
                tb=error.__traceback__
            )
        )
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message
