"""
run

This module contains the primary function for Huffman Encoding. It assumes 
valid I/O. While running, it logs performance metrics. All results are written
to the output file.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from sys import stderr
from typing import TextIO, List, Tuple
from lab3.huffman_tree import HuffmanTree
from lab3.huffman_encoding import HuffmanEncoding
from lab3.huffman_node import HuffmanNode
from support.performance import Performance
from support.output_formatters import format_encoded_results, \
    format_decoded_results, write_to_output
from support.output_tree_formatters import format_huffman_tree, \
    format_huffman_tree_binary_codes
from support.format_performance_report import format_performance_report


def run(frequency_table: TextIO, input_file: TextIO, output_file: TextIO,
        memo=False, encode=False, decode=False, debug=False) -> None:
    """
    Wrapper function for encoding or decoding a string using Huffman Encoding
    and a user-provided frequency table.

    Args:
        frequency_table (TextIO): file containing frequencies per character
        input_file (TextIO): text file with strings to encode/decode
        output_file (TextIO): text file where results are written
        memo (bool): True if memoizing HuffmanTree nodes, otherwise False
        encode (bool): True if input file strings will be encoded
        decode (bool): True if input file strings will be decoded
        debug (bool): True if debug mode is toggled on, otherwise False

    Raises:
        ValueError: if both decode and encode are False
    """
    # Set up Performance object and output strings used by runner functions
    performance = Performance()
    out = []
    NODES_PER_LINE = 4

    def run_tree_setup() -> Tuple['HuffmanTree', List[str], bool]:
        """
        Helper function for running the Huffman Tree setup and measuring its
        performance. 

        Returns:
            HuffmanTree: Huffman Tree instance built using frequency_table
            bool: True if HuffmanTree instantiation raised a ValueError, otherwise
                False
        """
        out.append("-------Huffman Tree in Preorder-------\n")

        # Get number of character - frequency pairs. Set up error handling
        frequency_table_size = 0
        error = False
        huffman_tree = None
        nonlocal NODES_PER_LINE

        with open(frequency_table, 'r', encoding="utf-8") as ft:
            frequency_table_size = len(ft.readlines())

        # Start runtime timer for a HuffmanTree with frequency_table_size nodes
        performance.set_size(frequency_table_size)
        performance.start()

        try:
            huffman_tree = HuffmanTree(frequency_table, memo=memo)
        except ValueError as ve:
            # All possible errors are ValueErrrors. Save to output
            error_message = ve.args[0]
            error = True

            if debug:
                print(error_message, file=stderr)
        finally:
            performance.stop()

            if error:
                out.append(error_message)
            else:
                out.append(format_huffman_tree(
                    huffman_tree, nodes_per_line=NODES_PER_LINE) + '\n')

            out.append(f"Size (number of frequencies): {frequency_table_size}")
            out.append(f"Runtime: {performance.get_runtime_micro_sec()}μs")

        return huffman_tree, error

    if encode == decode:
        # Error case: decode OR encode can be True, but not both or neither
        raise ValueError("Either encode or decode must be True")

    # Build Huffman Tree. Don't attempt encoding / decoding if error raised
    huffman_tree, error = run_tree_setup()

    if error:
        write_to_output(output_file, out)
        return

    # print(huffman_tree.print_codes())

    huffman_encoding = HuffmanEncoding(huffman_tree)
    with open(input_file, 'r', encoding="utf-8") as file:
        out.append("\n\n-------Conversion Results-------\n")

        # Counting lines for clean formatting
        line_counter = 1
        for line in file:
            expression = line.strip()
            size = len(expression)

            if size == 0:
                # Case: empty line. Ignore.
                continue

            # Set up error handling and performance metrics
            error = False
            result = ""
            performance.set_size(size).start()

            try:
                if encode:
                    result = huffman_encoding.encode(expression)
                elif decode:
                    result = huffman_encoding.decode(expression)
            except ValueError as ve:
                result = ve.args[0]
                error = True

                if debug:
                    error_message = f"Expression: {expression}"
                    error_message += f"\n\tError Message: {result}"
                    print(error_message, file=stderr)
            finally:
                performance.stop()

                if error:
                    performance.log_error(micro_sec=True)
                else:
                    performance.log_success(micro_sec=True)

                if encode:
                    out.append(format_encoded_results(
                        line_counter, expression, result,
                        performance.get_metrics_micro_sec(), error))
                else:
                    out.append(format_decoded_results(
                        line_counter, expression, result,
                        performance.get_metrics_micro_sec(), error))
                line_counter += 1

    # Display conversion values
    out.append("\nConversion values: ")

    if not memo:
        # If not using memoization, codes are not preset
        huffman_tree.set_codes()

    out.append(format_huffman_tree_binary_codes(huffman_tree, NODES_PER_LINE))

    # Output performance report
    out.append(format_performance_report(performance, micro_sec=True))

    # Output results
    write_to_output(output_file, out)

    if debug:
        print('OK', file=stderr)
