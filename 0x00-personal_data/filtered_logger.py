#!/usr/bin/env python3
"""
Module for filtering log data
"""

import logging
import re
from typing import List
import mysql.connector
from os import environ


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
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ Returns a logging.Logger object """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(handler)
    logger.propagate = False
    return logger


PII_FIELDS: List[str] = ("name", "email", "phone", "ssn", "password")


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a connector to a database
    """
    username = environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password = environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    db_name = environ.get('PERSONAL_DATA_DB_NAME')
    host = environ.get('PERSONAL_DATA_DB_HOST')

    conn = mysql.connector.connection.MySQLConnection(user=username,
                                                      password=password,
                                                      host=host,
                                                      database=db_name)
    return conn
