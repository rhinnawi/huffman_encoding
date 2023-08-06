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


def run(frequency_table: TextIO):
    """
    Wrapper function for encoding or decoding a string using Huffman Encoding
    and a user-provided frequency table.
    """
    huffman_tree = HuffmanTree(frequency_table)
    print(huffman_tree)
    print('OK')
