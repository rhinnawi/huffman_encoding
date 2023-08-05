"""
is_valid_io

This module contains the function that checks for validating the user-provided
input and output file paths. Python typing initially assumes that arguments
are TextIO types, so the function body validates that the paths exist. The
input file must already exist as output depends on its values. Output files
may be newly written, and so only the parent directory must already exist.

Author: Rani Hinnawi
Date: 2023-07-25
"""
from typing import TextIO, List


def is_valid_io(*files: List[TextIO]) -> bool:
    """
    Function that validates that the input and the path to the output exist

    Args:
        *files (List[TextIO]): list of possible file paths

    Returns:
        bool: True if all file paths are valid

    Raises:
        FileNotFoundError: If any file passed in does not exist
    """
    error_message = "ERROR: the files below do not exist\n"
    error = False

    for file in files:
        # Validate path
        if not file.exists():
            error_message += f"- {file.name}\n"
            error = True

    # Raise error if either file is invalid. Otherwise, return True
    if error:
        raise FileNotFoundError(error_message)

    return True
