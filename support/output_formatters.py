"""
output_formatters

This module contains helper functions called to format strings intended to be
outputted to a text file.

Author: Rani Hinnawi
Date: 2023-08-08
"""


def break_string(expression: str, chars_per_line: int) -> str:
    """
    Helper function for outputting a long string within user-defined length
    restrictions.

    Args:
        expression (str): string being broken into multiple lines
        chars_per_line (str): max length of substring per line

    Returns:
        str: formatted string
    """
    if len(expression) <= chars_per_line:
        return expression

    # Begin on new line with indentation
    lines = ["\t\t"]

    # Break up into lines of length chars_per_line and return
    for i in range(0, len(expression), chars_per_line):
        lines.append(expression[i:i + chars_per_line])

    return "\n\t\t".join(lines)


def format_encoded_results(line_number: int, expression: str, result: str,
                           metrics: str, error=False, chars_per_line=80) \
        -> str:
    """
    Function that formats the inputted expression and the output given from the
    encoding process.

    Args:
        line_number (int): number for labelling lines in the output
        expression (str): original expression being encoded
        result (str): encoded binary expression OR error message
        metrics (str): string representation of Performance values (size, runtime)
        error (bool): indicator of whether result is an error message

    Returns:
        str: conditionally formatted results
    """
    # Format header line with original expression
    prefix = f"{line_number}. Original: "
    expression = break_string(expression, chars_per_line - len(prefix))
    write = [prefix + expression]

    # Format and append result with error  handling
    prefix = "\tError - " if error else "\tEncoded: "
    result = break_string(result, chars_per_line - len(prefix))
    write.append(prefix + result)

    # Add metrics and return
    write.append(f"{metrics}\n")

    return '\n'.join(write)


def format_decoded_results(line_number: int, expression: str, result: str,
                           metrics: str, error=False, chars_per_line=80) \
        -> str:
    """
    Function that formats the inputted expression and the output given from the
    decoding process.

    Args:
        line_number (int): number for labelling lines in the output
        expression (str): original expression being decoded
        result (str): decoded expression OR error message
        metrics (str): string representation of Performance values (size, runtime)
        error (bool): indicator of whether result is an error message

    Returns:
        str: conditionally formatted results
    """
    # Format header line with original expression
    prefix = f"{line_number}. Binary: "
    expression = break_string(expression, chars_per_line - len(prefix))
    write = [prefix + expression]

    # Format and append result with error  handling
    prefix = "\tError - " if error else "\tDecoded: "
    result = break_string(result, chars_per_line - len(prefix))
    write.append(prefix + result)

    # Add metrics and return
    write.append(f"{metrics}\n")

    return '\n'.join(write)
