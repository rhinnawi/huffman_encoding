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
# from lab3.huffman_encoding import HuffmanEncoding
# from lab3.huffman_node import HuffmanNode


def run(frequency_table: TextIO):
    """
    Wrapper function for encoding or decoding a string using Huffman Encoding
    and a user-provided frequency table.
    """
    huffman_tree = HuffmanTree(frequency_table)
    print(huffman_tree, '\n')

    # huffman_encoding = HuffmanEncoding(huffman_tree)
    # print(huffman_encoding, '\n')
    print("has memo:", huffman_tree.has_memo())

    huffman_tree = HuffmanTree(frequency_table, True)
    print(huffman_tree, '\n')

    # huffman_encoding = HuffmanEncoding(huffman_tree)
    print(huffman_tree.has_memo())
    print(huffman_tree.print_codes(), '\n')
    print(list(map(str, huffman_tree.get_memo())))

    print('OK')
