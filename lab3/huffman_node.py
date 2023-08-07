"""
huffman_tree

This module contains a class for building a Huffman tree node. It includes
functionality for field setters and getters, as well as comparisons. 
Comparisons give precedence to frequency, and then character length, and 
then lexicographical ordering. This implementation allows for method chaining.

Author: Rani Hinnawi
Date: 2023-08-08
"""
import re
from typing import Optional


class HuffmanNode:
    """
    Class representing a node in a Huffman (binary) tree
    """

    def __init__(self) -> 'HuffmanNode':
        self._chars: Optional[str] = None
        self._freq: Optional[int] = None
        self._code = ""
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
        if self._freq != other.get_frequency():
            return self._freq < other.get_frequency()
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
        if self._freq != other.get_frequency():
            return self._freq > other.get_frequency()
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
        return self._freq == other.get_frequency() and \
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
        if len(self._chars) == 1 and len(other.get_characters()) != 1:
            return 1  # This node takes precedence
        elif len(self._chars) != 1 and len(other.get_characters()) == 1:
            return -1  # The other node takes precedence
        else:
            # Compare lexicographically for all other cases
            # Shortened version of if-else statements returning -1, 0, or 1
            return int(self._chars < other.get_characters())

    def get_code(self) -> str:
        """
        Getter method for retrieving current node's Huffman Code, a binary
        number indicating its position along the binary Huffman Tree.

        Returns:
            str: current node instance's binary Huffman code
        """
        return self._code

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
            HuffmanNode: right child of current Node instance
        """
        return self._right

    def get_left(self) -> Optional['HuffmanNode']:
        """
        Getter method for retrieving left child node.

        Returns:
            HuffmanNode: left child of current Node instance
        """
        return self._left

    def set_code(self, new_code: str) -> 'HuffmanNode':
        """
        Setter method for updating current node's Huffman Code, a binary
        number indicating its position along the binary Huffman Tree.

        Args:
            new_code (str): string in the form of a binary number

        Returns:
            HuffmanNode: current node instance

        Raises:
            ValueError: new string is not a valid binary number
        """
        if (not isinstance(new_code, str)) or \
                (re.match("^[01]*$", new_code) is None):
            raise ValueError("Must be a valid binary number string")

        self._code = new_code
        return self

    def set_frequency(self, new_frequency: int) -> 'HuffmanNode':
        """
        Setter method for updating frequency attribute, which stores the number
        of occurrences this current node instance's characters occur in a
        frequency table

        Args:
            new_frequency (int): number of occurrences of current instance's 
                characters stored in a frequency table

        Returns:
            HuffmanNode: current node instance

        Raises:
            ValueError: when non-integer is passed in
        """
        if not isinstance(new_frequency, int):
            raise ValueError("Frequency must be an integer")

        self._freq = new_frequency
        return self

    def set_characters(self, new_characters: str) -> 'HuffmanNode':
        """
        Setter method for updating characters for current node

        Args:
            new_characters: current instance's characters stored

        Returns:
            HuffmanNode: current node instance

        Raises:
            ValueError: when non-string is passed in
        """
        if not isinstance(new_characters, str):
            raise ValueError("Characters must be an string type")

        self._chars = new_characters
        return self

    def set_right(self, new_right: 'HuffmanNode') -> 'HuffmanNode':
        """
        Setter method for pointer to current Node instance's right child
        node.

        Args:
            new_right (HuffmanNode): new right child node

        Returns:
            HuffmanNode: current Node instance

        Raises:
            TypeError: when new_right is not a HuffmanNode
        """
        if not isinstance(new_right, HuffmanNode):
            raise TypeError("New node must be a HuffmanNode")

        self._right = new_right
        return self

    def set_left(self, new_left: 'HuffmanNode') -> 'HuffmanNode':
        """
        Setter method for pointer to current Node instance's left child
        node.

        Args:
            new_right (HuffmanNode): new left child node

        Returns:
            HuffmanNode: current Node instance

        Raises:
            TypeError: when new_right is not a HuffmanNode
        """
        if not isinstance(new_left, HuffmanNode):
            raise TypeError("New node must be a HuffmanNode")

        self._left = new_left
        return self

    def is_leaf(self) -> bool:
        """
        Indicates whether the current HuffmanNode instance is a leaf node.

        Returns:
            bool: True if it has no child nodes, otherwise false
        """
        return (self._left is None) and (self._right is None)
