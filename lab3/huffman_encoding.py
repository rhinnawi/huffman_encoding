"""
huffman_encoding

This module contains a class for a Huffman Encoding object. It includes 
functionality for encoding and decoding based on frequencies of characters as
they are stored in a HuffmanTree. This implementation allows for method 
chaining.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from lab3.huffman_tree import HuffmanTree


class HuffmanEncoding:
    """
    Class for encoding and decoding text based on passed-in Huffman Tree and
    the frequency values per character it contains.
    """

    def __init__(self, huffman_tree: 'HuffmanTree') -> 'HuffmanEncoding':
        self._tree = huffman_tree
