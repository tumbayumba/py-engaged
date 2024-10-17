


class ApplicationException(Exception):

    def __init__(self, message):
        self.base_message = "Caught an exception: "
        self.message = "Caught an exception: " + " " + message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"