"""
huffman_encoding

This module contains a class for Huffman Tree. It includes functionality for
storing values from a frequency table. This implementation allows for method 
chaining.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from sys import stderr
from typing import List, Optional, TextIO
from lab3.huffman_node import HuffmanNode
from support.heap import Heap


class HuffmanTree:
    """
    Class for building a Huffman Tree, which stores characters and their
    frequencies nodes in a binary tree structure.
    """

    def __init__(self, frequency_table: TextIO) -> 'HuffmanTree':
        self._root = self._build_tree(frequency_table)
        self._nodes_pq: Optional['Heap'] = None

    def __str__(self) -> str:
        """
        String representation of Huffman Tree using pre-order traversal

        Returns:
            str: pre-order traversal of Huffman Tree nodes in format 
                characters: frequency
        """
        def preorder(root: Optional['HuffmanNode']) -> List[str]:
            rep = []

            if not root:
                return rep

            rep.append(f"{root.get_characters()}: {root.get_frequency()}")

            if root.get_left():
                rep.extend(preorder(root.get_left()))

            if root.get_right():
                rep.extend(preorder(root.get_right()))

            return rep

        return ', '.join(preorder(self._root))

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
        # Set up a priority queue with all leaf nodes
        nodes_pq = Heap()
        with open(frequency_table_file, 'r', encoding="utf-8") as freq_table:
            for line in freq_table:
                character, _, frequency = line.strip().split()

                try:
                    frequency = int(frequency)
                except ValueError as ve:
                    # Error case: frequency is not a number
                    print(ve.args[0], file=stderr)

                if frequency < 1:
                    # Error case: cannot have negative frequency
                    error = "INVALID FREQUENCY: must be > 0"
                    raise ValueError(error)

                if len(character) != 1:
                    # Error case: key is not a single character
                    error = "INVALID CHAR: key must be a single character"
                    raise ValueError(error)

                if not character.isalpha():
                    # Error case: character must be alphabetical
                    error = "INVALID CHAR: key must be alphabetical"
                    raise ValueError(error)

                new_node = HuffmanNode().set_characters(
                    character).set_frequency(frequency)

                nodes_pq.heap_push(new_node)

        # Combine nodes into left-right pairs under a new parent
        while nodes_pq.size() > 1:
            # Default case: Huffman tree will have multiple nodes
            right: 'HuffmanNode' = nodes_pq.heap_pop()
            left: 'HuffmanNode' = nodes_pq.heap_pop()

            # Set up new parent node and push back to priority queue
            parent_chars = left.get_characters() + right.get_characters()
            parent_freqs = left.get_frequency() + right.get_frequency()
            parent_node = HuffmanNode()\
                .set_characters(parent_chars)\
                .set_frequency(parent_freqs)\
                .set_left(left)\
                .set_right(right)

            nodes_pq.heap_push(parent_node)

        # Last item is the root of a new binary tree. Return root
        return nodes_pq.heap_pop()
