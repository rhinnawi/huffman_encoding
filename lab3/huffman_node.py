"""
huffman_tree

This module contains a class for building a Huffman tree node. It includes
functionality for field setters and getters, as well as comparisons. 
Comparisons give precedence to frequency, and then character length, and 
then lexicographical ordering. This implementation allows for method chaining.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from typing import Optional


class HuffmanNode:
    """
    Class representing a node in a Huffman (binary) tree
    """

    def __init__(self) -> 'HuffmanNode':
        self._chars: Optional[str] = None
        self._freq: Optional[int] = None
        self._right: Optional['HuffmanNode'] = None
        self._left: Optional['HuffmanNode'] = None

    def __str__(self) -> str:
        """
        Creates a string representation of a Huffman Node

        Returns:
            str: string representing the node as the key-value pair
                'characters: frequency'
        """
        return f'{self._chars}: {self._freq}'

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """
        Less-than comparison for HuffmanNode objects. It is primarily based on
        frequency. Given equal frequencies, character length and then character
        order are taken into account.

        Args:
            other (HuffmanNode): The other HuffmanNode with which to compare

        Returns:
            bool: True if this node is less than the other node.
        """
        if self._freq != other._freq:
            return self._freq < other._freq
        return self._compare_chars(other) < 0

    def __gt__(self, other: 'HuffmanNode') -> bool:
        """
        Greater-than comparison for HuffmanNode objects. It is primarily based
        on frequency. Given equal frequencies, character length and then 
        character order are taken into account.

        Args:
            other (HuffmanNode): The other HuffmanNode with which to compare

        Returns:
            bool: True if this node is greater than the other node.
        """
        if self._freq != other._freq:
            return self._freq > other._freq
        return self._compare_chars(other) > 0

    def __le__(self, other: 'HuffmanNode') -> bool:
        """
        Less-than-or-equal comparison for HuffmanNode objects.

        Args:
            other (HuffmanNode): The other HuffmanNode with which to compare

        Returns:
            bool: True if this node is less than or equal to the other node.
        """
        return not self.__gt__(other)

    def __ge__(self, other: 'HuffmanNode') -> bool:
        """
        Greater-than-or-equal comparison for HuffmanNode objects.

        Args:
            other (HuffmanNode): The other HuffmanNode with which to compare

        Returns:
            bool: True if this node is greater than or equal to the other node.
        """
        return not self.__lt__(other)

    def __eq__(self, other: 'HuffmanNode') -> bool:
        """
        Equality comparison for HuffmanNode objects. Two nodes are equal if
        they have the same frequency and characters string value 

        Args:
            other (HuffmanNode): The other HuffmanNode with which to compare

        Returns:
            bool: True if this node is equal to the other node.
        """
        return self._freq == other._freq and \
            self._chars == other.get_characters()

    def __ne__(self, other: 'HuffmanNode') -> bool:
        """
        Inequality comparison for HuffmanNode objects.

        Args:
            other (HuffmanNode): The other HuffmanNode with which to compare

        Returns:
            bool: True if this node is not equal to the other node.
        """
        return not self.__eq__(other)

    def _compare_chars(self, other: 'HuffmanNode') -> int:
        """
        Helper method for comparing characters alphabetically and by length for
        HuffmanNode objects.

        Args:
            other (HuffmanNode): The other HuffmanNode with which to compare

        Returns:
            int: Negative if this node comes before, positive if after, 0 if
                equal
        """
        if len(self._chars) == len(other.get_characters()):
            # Shortened version of if-else statements returning -1, 0, or 1
            return (self._chars > other.get_characters()) - \
                (self._chars < other.get_characters())

        return len(self._chars) - len(other.get_characters())

    def get_frequency(self) -> int:
        """
        Getter method for retrieving frequency of current node

        Returns:
            int: number of occurrences of current instance's characters stored
                in a frequency table
        """
        return self._freq

    def get_characters(self) -> str:
        """
        Getter method for retrieving characters for current node

        Returns:
            str: current instance's characters stored
        """
        return self._chars

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

    def set_frequency(self, new_frequency: int) -> 'HuffmanNode':
        """
        Setter method for updating frequency attribute, which stores the number
        of occurrences this current node instance's characters occur in a
        frequency table

        Args:
            new_frequency (int): number of occurrences of current instance's 
                characters stored in a frequency table

        Returns:
            'HuffmanNode': current node instance
        """
        self._freq = new_frequency
        return self

    def set_characters(self, new_characters: str) -> 'HuffmanNode':
        """
        Setter method for updating characters for current node

        Args:
            new_characters: current instance's characters stored

        Returns:
            'HuffmanNode': current node instance
        """
        self._chars = new_characters
        return self

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
