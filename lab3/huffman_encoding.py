"""
huffman_encoding

This module contains a class for a Huffman Encoding object. It includes 
functionality for encoding and decoding based on frequencies of characters as
they are stored in a HuffmanTree. This implementation allows for method 
chaining.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from typing import List, Optional
from lab3.huffman_tree import HuffmanTree
from lab3.huffman_node import HuffmanNode

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
        # Set binary codes for quick retrieval if has memo. Otherwise, find
        # dynamically during encoding process
        if self._tree.has_memo():
            self._set_codes()

    def __str__(self) -> str:
        """
        Method for representing Huffman Encoding binary codes for all Huffman 
        tree nodes using preorder traversal. Output is a comma-separated list 
        of each node's characters string and binary Huffman code as a key-value
        pair.

        str: pre-order traversal of Huffman Tree nodes in format 
                characters: code
        """
        def preorder(root: Optional['HuffmanNode']) -> List[str]:
            rep = []

            # Visit root, then left, then right
            if not root:
                return rep

            rep.append(f"{root.get_characters()}: {root.get_code()}")

            if root.get_left():
                rep.extend(preorder(root.get_left()))

            if root.get_right():
                rep.extend(preorder(root.get_right()))

            return rep

        return ', '.join(preorder(self._tree.get_root()))

    def _set_codes(self) -> 'HuffmanEncoding':
        """
        Method for adding binary codes to Huffman tree nodes.

        Returns:
            HuffmanEncoding: current HuffmanEncoding object instance
        """

        def preorder(node: Optional['HuffmanNode'], prefix="") -> None:
            """
            Helper function for preorder traversal of Huffman Tree to update
            each node's binary Huffman code. Each left child has a 0 appended,
            and each right has a 1 appended to its parent node's code (prefix).

            Args:
                node (HuffmanNode): current node being visited
                prefix (str): parent node's Huffman code
            """
            if not node:
                return

            if node.is_leaf():
                node.set_code(prefix)
            else:
                preorder(node.get_left(), prefix + "0")
                preorder(node.get_right(), prefix + "1")

            return

        root = self._tree.get_root()
        preorder(root)

        return self

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
            # Get binary encoding for symbol. Add to output string
            if (char in self._allowed_nonalpha_chars) or (char.isspace()):
                # Case: char is a whitespace or permitted punctuation symbol
                continue

            index = ord(char) - ord('A')
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
