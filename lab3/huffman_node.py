"""
huffman_tree

This module contains a class for building a Huffman tree node. It includes
functionality for field setters and getters, as well as comparisons. This 
implementation allows for method chaining.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from typing import Optional


class HuffmanNode:
    """
    Binary tree node object specifically designed for Huffman Trees
    """

    def __init__(self, characters: str, frequency: int):
        self._chars = characters
        self._freq = frequency
        self._right = None
        self._left = None

    def get_right(self) -> Optional['HuffmanNode']:
        """
        Getter method for retrieving right child node.

        Returns:
            'Node': right child of current Node instance
        """
        return self._right

    def get_left(self) -> Optional['HuffmanNode']:
        """
        Getter method for retrieving left child node.

        Returns:
            'Node': left child of current Node instance
        """
        return self._left

    def set_right(self, new_right: 'HuffmanNode') -> 'HuffmanNode':
        """
        Setter method for pointer to current Node instance's right child
        node.

        Args:
            new_right ('HuffmanNode'): new right child node

        Returns:
            'HuffmanNode': current Node instance
        """
        self._right = new_right
        return self

    def set_left(self, new_left: 'HuffmanNode') -> 'HuffmanNode':
        """
        Setter method for pointer to current Node instance's left child
        node.

        Args:
            new_right ('HuffmanNode'): new left child node

        Returns:
            'HuffmanNode': current Node instance
        """
        self._left = new_left
        return self
