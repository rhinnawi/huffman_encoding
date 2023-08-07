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


class HuffmanEncoding:
    """
    Class for encoding and decoding text based on passed-in Huffman Tree and
    the frequency values per character it contains.
    """

    def __init__(self, huffman_tree: 'HuffmanTree') -> 'HuffmanEncoding':
        self._tree = huffman_tree
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

        def preorder(node: Optional['HuffmanNode'], prefix: str) -> None:
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
        preorder(root, "")

        return self
