""" created 25/10/2016
author: marcello
version: 0.1
"""

class SeqException(Exception):
    """Base class Exception for sequences modules."""
    pass

class SequenceException(SeqException):
    """Exception raised for errors in building sequencese.

    Fires if the building sequence contains other characters than a t g c in
    DNA, a u c g in DNA, aminoacids in proteins, etc.
    """

    def __init__(self, expression: str, message: str):
        self.expression = expression
        self.message = message



