#!/usr/bin/env python3
"""
Module for filtering log data
"""

import logging
import re
from typing import List


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Returns the log message obfuscated.

    Args:
        fields (List[str]): A list of strings representing all fields to
        obfuscate.
        redaction (str): A string representing by what the field will be
        obfuscated.
        message (str): A string representing the log line.
        separator (str): A string representing by which character is separating
        all fields in the log line (message).

    Returns:
        str: The obfuscated log message.
    """
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format method to filter values in incoming log records
        """
        message = record.msg
        for field in self.fields:
            message = re.sub(
                rf'{field}=.+?{self.SEPARATOR}',
                f'{field}={self.REDACTION} {self.SEPARATOR}',
                message
            )
        record.msg = message
        return super().format(record)
