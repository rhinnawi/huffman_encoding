"""
huffman_encoding

This module contains a class for Huffman Encoding. It includes
functionality for data encoding and decoding, as well as storing values from
a frequency table. This implementation allows for method chaining.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from typing import TextIO
from lab3.huffman_node import HuffmanNode
from support.heap import Heap


class HuffmanEncoding:
    """
    Class for building a Huffman Tree, which stores characters and their
    frequencies nodes in a binary tree structure.
    """

    def __init__(self, frequency_table: TextIO) -> 'HuffmanEncoding':
        self._huffman_tree = self._build_tree(frequency_table)

    def _build_tree(self, frequency_table_file: TextIO) -> 'HuffmanNode':
        """
        Encodes characters and their frequencies as HuffmanNodes in a binary
        tree structure, or Huffman Tree.

        Args:
            frequency_table_file (TextIO): File containing key-value pairs of
                characters and their frequencies

        Returns:
            'HuffmanNode': root of new Huffman Tree

        TODO: complete implementation, including error checking
        """
        priority_queue = Heap()
        with open(frequency_table_file, 'r', encoding="utf-8") as freq_table:
            for line in freq_table:
                character, _, frequency = line.strip().split()
                new_node = HuffmanNode().set_characters(
                    character).set_frequency(frequency)

                priority_queue.heap_push(new_node)

        return priority_queue.heap_pop()
