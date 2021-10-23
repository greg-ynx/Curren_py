class Exceptions(Exception):
    pass


class NoneValueException(Exceptions):
    """Raised when there is no value in lineEdits"""


class ActionCanceled(Exceptions):
    """Raised when an action is canceled"""
