"""
huffman_encoding

This module contains a class for a Huffman Encoding object. It includes 
functionality for encoding and decoding based on frequencies of characters as
they are stored in a HuffmanTree. This implementation allows for method 
chaining.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from typing import Optional
from hencoding.huffman_tree import HuffmanTree
from hencoding.huffman_node import HuffmanNode

ALLOWED_PUNCTUATION = {'.', ',', ';', ':', '!', '?', '-',
                       '"', "'", '(', ')', '/', '\\', '_', '@', '&', '*', '~'}


class HuffmanEncoding:
    """
    Class for encoding and decoding text based on passed-in Huffman Tree and
    the frequency values per character it contains.
    """

    def __init__(self, huffman_tree: 'HuffmanTree',
                 allowed_nonalpha_chars=None) -> 'HuffmanEncoding':
        self._tree = huffman_tree
        self._allowed_nonalpha_chars = allowed_nonalpha_chars if \
            allowed_nonalpha_chars is not None else ALLOWED_PUNCTUATION

    def encode(self, expression: str) -> str:
        """
        Method for encoding an expression string using the Huffman Tree

        Args:
            expression (str): the string being encoded

        Returns:
            str: a new binary string made entirely of 1s and 0s
        """
        if self._tree.has_memo():
            return self._encode_with_memo(expression)

        return self._encode_without_memo(expression)

    def _value_error_message(self, char: str) -> str:
        """
        Helper method for standardizing value error message across both encode
        methods.

        Args:
            char (str): invalid character referenced in error message
        """
        error = f"INVALID CHAR: the character '{char}' is not a leaf node in "
        error += "the frequency table, a permitted punctuation symbol, or a "
        error += "whitespace"
        return error

    def _encode_with_memo(self, expression: str) -> str:
        """
        Encodes a given expression using the Huffman Tree. Each character
        should appear as a leaf node, which carries a binary Huffman code
        corresponding to it. Uses memoization to quickly call a reference to
        the node and retrieve pre-calculated code.

        Args:
            expression (str): the string being encoded

        Returns:
            str: a new binary string made entirely of 1s and 0s

        Raises:
            ValueError: when a non-punctuation or non-white space character 
                appears that is not a leaf node in the Huffman Tree (it has no
                corresponding Huffman code)
        """
        encoded = ""
        leaf_nodes = self._tree.get_memo()
        for char in expression:
            # Enforce case insensitivity
            char = char.lower()

            # Get binary encoding for symbol. Add to output string
            if (char in self._allowed_nonalpha_chars) or (char.isspace()):
                # Case: char is a whitespace or permitted punctuation symbol
                continue

            index = ord(char) - ord('a')
            if (index >= len(leaf_nodes)) or (index < 0):
                # Error case: character is not in the Huffman tree
                raise ValueError(self._value_error_message(char))

            node = leaf_nodes[index]
            if node is not None:
                encoded += node.get_code()
            else:
                # Error case: character is not in the Huffman tree
                raise ValueError(self._value_error_message(char))

        return encoded

    def _encode_without_memo(self, expression: str) -> str:
        """
        Encodes a given expression using the Huffman Tree. Each character
        should appear as a leaf node, which carries a binary Huffman code
        corresponding to it. Uses preorder traversal to dynamically calculate
        Huffman code.

        Args:
            expression (str): the string being encoded

        Returns:
            str: a new binary string made entirely of 1s and 0s

        Raises:
            ValueError: when a non-punctuation or non-white space character 
                appears that is not a leaf node in the Huffman Tree (it has no
                corresponding Huffman code)
        """
        def encode_char(node: 'HuffmanNode', target_letter: str, code="") \
                -> Optional[str]:
            """
            Helper function for leveraging preorder traversal to determine a
            character's Huffman code.

            Args:
                node (HuffmanNode): Root of Huffman Tree or subtree
                char (str): character being searched for in Huffman Tree
                code (str): binary Huffman code of parent node

            Returns:
                str: Binary number indicating position of char in the Huffman
                    Tree OR None if not in tree
            """
            if node.is_leaf():
                if node.get_characters() == target_letter:
                    return code
                else:
                    return None
            else:
                # Must be leaf. Search left, then search right for char
                left_code = encode_char(node.get_left(), target_letter,
                                        code + "0")
                if left_code is not None:
                    return left_code

                right_code = encode_char(node.get_right(), target_letter,
                                         code + "1")
                return right_code

        encoded = ""
        for char in expression:
            # Enforce case insensitivity
            char = char.lower()

            # Get binary encoding for symbol. Add to output string
            if (char in self._allowed_nonalpha_chars) or (char.isspace()):
                # Case: char is a whitespace or permitted punctuation symbol
                continue

            letter_code = encode_char(self._tree.get_root(), char)
            if letter_code is not None:
                encoded += letter_code
            else:
                # Error case: character is not in the Huffman tree
                raise ValueError(self._value_error_message(char))

        return encoded

    def decode(self, encoded_string: str) -> str:
        """
        Decompresses a given compressed binary string using the Huffman Tree.

        Args:
            encoded_string (str): the compressed binary string

        Returns:
            str: the decompressed string

        Raises:
            ValueError: if a character (bit) is not a 0 or 1
        """
        # Begin conversion at the root. Set up output and error message
        node = self._tree.get_root()
        result = ""
        error_message = "INVALID BINARY: Leftover bits in the encoded string. "
        error_message += "Cannot be converted."

        # Traverse Huffman Tree. 0 = left, 1 = right. Leaf = letter decoded
        for bit in encoded_string:
            if bit == '0':
                node = node.get_left()
            elif bit == '1':
                node = node.get_right()
            elif bit.isspace():
                # Case: whitespace encountered at end of a potential word
                if node != self._tree.get_root():
                    # Error case: "word" in binary string could not be decoded
                    raise ValueError(error_message)
                continue
            else:
                # Error case: not a binary string
                error = f"INVALID CHAR: {bit} is not a binary bit"
                raise ValueError(error)

            if node.is_leaf():
                # Add letter to decoded message. Restart next bit at the root
                result += node.get_characters()
                node = self._tree.get_root()

        if node != self._tree.get_root():
            # Error case: leftover bits in the encoded_string
            raise ValueError(error_message)

        return result
