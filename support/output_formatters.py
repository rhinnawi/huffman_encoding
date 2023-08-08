"""
output_formatters

This module contains helper functions called to format strings intended to be
outputted to a text file.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from sys import setrecursionlimit
from typing import Optional, List, Tuple
from support.performance import Performance
from lab3.huffman_tree import HuffmanTree
from lab3.huffman_node import HuffmanNode

# Set recursion limit. Python default: 1000. Should not need to exceed number
# of letters in Latin (English) alphabet
RECURSION_LIMIT = 52
setrecursionlimit(RECURSION_LIMIT)


def format_huffman_tree(huffman_tree: 'HuffmanTree', nodes_per_line: int) \
        -> str:
    """
    Function that formats the number of Huffman Tree nodes per line for easier
    readability in an output file.

    Args:
        huffman_tree (HuffmanTree): Huffman Tree being printed out
        nodes_per_line (int): max number of Huffman Nodes printed per line

    Returns:
        str: string representation of Huffman Nodes

    Raises:
        ValueError: when nodes_per_line is not a positive integer
    """
    def preorder(root: Optional['HuffmanNode'], nodes_left=nodes_per_line) \
            -> Tuple[List[str], int]:
        """
        Preorder traversal of Huffman Tree and its nodes.

        Args:
            root (HuffmanNode): root of a Huffman tree or subtree OR None

        Returns:
            List[str]: list of Python nodes as key-value pairs in format
                character: frequency
        """
        # Add nodes to 'representation' list
        rep = []

        # Visit root, then left, then right
        if not root:
            return rep, nodes_left

        node_str = str(root)

        # Node is placed on new line when 0 nodes left per line are remaining
        if nodes_left == 0:
            node_str = "\n\t" + node_str
            nodes_left = nodes_per_line
        else:
            nodes_left -= 1

        # Add HuffmanNode string, then visit left and right branches
        rep.append(node_str)

        if root.get_left():
            left, nodes_left = preorder(root.get_left(), nodes_left)
            rep.extend(left)

        if root.get_right():
            right, nodes_left = preorder(
                root.get_right(), nodes_left)
            rep.extend(right)

        # Returns preorder representation list and remaining nodes for
        # possible recursive calls
        return rep, nodes_left

    if nodes_per_line < 1:
        error = "There must be at least 1 node per line"
        raise ValueError(error)

    output, _ = preorder(huffman_tree.get_root())
    return ", ".join(output)


def break_string(expression: str, chars_per_line: int) -> str:
    if len(expression) <= chars_per_line:
        return expression

    # Begin on new line with indentation
    lines = ["\t\t"]
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
                           metrics: str, error=False) -> str:
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
    write = [f"{line_number}. Binary: {expression}"]

    if (error):
        write.append(f"\tERROR - {result}")
    else:
        write.append(f"\tDecoded: {result}\n")

    write.append(f"{metrics}\n")

    return '\n'.join(write)


def format_performance_report(metrics: 'Performance') -> str:
    """
    Function that formats the size and runtime data logged for each success and
    failure into a report. Runtimes are outputted by size in order from 
    smallest to largest.

    Args:
        metrics (Performance): Performance object with logged metrics data

    Returns:
        str: logged successes and failures, formatted to suit a text file

    TODO: Update to have write be a List that is joined by \n
    """
    write = "\n-------Performance Report-------\n"

    # Note total number of successes and successes per size
    write += f"Total number of successes: {metrics.get_num_successes()}\n"

    successes = metrics.get_successes()
    for size in sorted(successes.keys()):
        runtime = sorted(successes[size])
        write += f"{size}: {runtime}\n"

    write += "\n"

    # Note total number of errors and errors per size
    write += f"Total number of errors: {metrics.get_num_errors()}\n"

    errors = metrics.get_errors()
    for size in sorted(errors.keys()):
        runtime = sorted(errors[size])
        write += f"{size}: {runtime}\n"

    write += "\nFormat:\n\tstring_size: [runtime1, ..., runtimeN]"
    write += "\n\tNOTE: Runtimes measured in nanoseconds (ns)\n"
    return write
