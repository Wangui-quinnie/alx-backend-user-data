#!/usr/bin/env python3
"""
Module for filtering log data
"""

import re


def filter_datum(
    fields: list,
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Replaces specified fields in a log message with redaction string.

    Args:
        fields (list): List of strings representing fields to obfuscate.
        redaction (str): String representing how the field will be obfuscated.
        message (str): String representing the log line.
        separator (str): String representing the character separating fields
        in the log line.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    return re.sub(
        rf'(;|^)(' + '|'.join(fields) + r')=[^;]*',
        rf'\1{redaction}',
        message
    )
