"""
run

This module contains the primary function for Huffman Encoding. It assumes 
valid I/O. While running, it logs performance metrics. All results are written
to the output file.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from typing import TextIO
from lab3.huffman_tree import HuffmanTree
from lab3.huffman_encoding import HuffmanEncoding
from support.performance import Performance
from support.output_formatters import format_huffman_tree


def run(frequency_table: TextIO, input_file: TextIO, output_file: TextIO,
        encode=False, decode=False) -> None:
    """
    Wrapper function for encoding or decoding a string using Huffman Encoding
    and a user-provided frequency table.

    Args:
        frequency_table (TextIO): file containing frequencies per character
        input_file (TextIO): text file with strings to encode/decode
        output_file (TextIO): text file where results are written
    """
    performance = Performance()
    with open(input_file, 'r', encoding="utf-8") as file, \
            open(output_file, 'w', encoding="utf-8") as out:
        out.write("-------Huffman Tree in Preorder-------\n")

        performance.start()
        huffman_tree = HuffmanTree(frequency_table)
        performance.stop()
        out.write(format_huffman_tree(huffman_tree, 5) + '\n')
        out.write(f"Runtime: {performance.get_runtime()}ns")

        huffman_encoding = HuffmanEncoding(huffman_tree)

    print('OK')
