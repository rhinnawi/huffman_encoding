"""
huffman_tree

This module contains a class for Huffman Tree. It includes functionality for
storing values from a frequency table. This implementation allows for method 
chaining.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from sys import setrecursionlimit, stderr
from typing import List, Optional, TextIO
from lab3.huffman_node import HuffmanNode
from support.heap import Heap

# Set recursion limit. Python default: 1000
RECURSION_LIMIT = 750
setrecursionlimit(RECURSION_LIMIT)


class HuffmanTree:
    """
    Class for building a Huffman Tree, which stores characters and their
    frequencies nodes in a binary tree structure.
    """

    def __init__(self, frequency_table: TextIO) -> 'HuffmanTree':
        self._frequency_table = frequency_table
        self._root = self._build_tree()

    def __str__(self) -> str:
        """
        String representation of Huffman Tree using pre-order traversal

        Returns:
            str: pre-order traversal of Huffman Tree nodes in format 
                characters: frequency
        """
        def preorder(root: Optional['HuffmanNode']) -> List[str]:
            rep = []

            # Visit root, then left, then right
            if not root:
                return rep

            rep.append(str(root))

            if root.get_left():
                rep.extend(preorder(root.get_left()))

            if root.get_right():
                rep.extend(preorder(root.get_right()))

            return rep

        return ', '.join(preorder(self._root))

    def _build_priority_queue(self) -> 'Heap':
        """
        Helper method for building the priority queue containing all leaf nodes.

        Returns:
            Heap: priority queue containing HuffmanNode objects within a min
                heap

        Raises:
            ValueError: character key is not a single alphabetical character or
                frequency value is not an integer >= 1
        """
        nodes_pq = Heap()
        with open(self._frequency_table, 'r', encoding="utf-8") as freq_table:
            for line in freq_table:
                # Get character and frequency values
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

                # Build new leaf node for the character and its frequency
                new_node = HuffmanNode().set_characters(
                    character).set_frequency(frequency)

                # Add new node to priority queue
                nodes_pq.heap_push(new_node)

        return nodes_pq

    def _build_tree(self) -> 'HuffmanNode':
        """
        Encodes characters and their frequencies as HuffmanNodes in a binary
        tree structure, or Huffman Tree.

        Returns:
            'HuffmanNode': root of new Huffman Tree

        TODO: complete implementation, including error checking
        """
        # Set up a priority queue with all leaf nodes
        nodes_pq = self._build_priority_queue()

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
