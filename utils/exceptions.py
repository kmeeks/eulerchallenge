class BaseError(Exception):
    """Base class for exceptions in this module."""
    pass


class MissingInputError(BaseError):
    """Exception raised for missing input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self):
        self.message = 'Missing solution name input'
