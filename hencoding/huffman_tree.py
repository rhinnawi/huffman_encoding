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
from hencoding.huffman_node import HuffmanNode
from support.heap import Heap

# Set recursion limit. Python default: 1000. Should not need to exceed number
# of letters in Latin (English) alphabet. +1 for buffer. Limit extended for
# Python built-in functions
RECURSION_LIMIT = 500
setrecursionlimit(RECURSION_LIMIT)


class HuffmanTree:
    """
    Class for building a Huffman Tree, which stores characters and their
    frequencies nodes in a binary tree structure.
    """

    def __init__(self, frequency_table: TextIO, memo=False) -> 'HuffmanTree':
        self._frequency_table = frequency_table

        # Each index corresponds to a letter in the alphabet
        self._memo = \
            [None for _ in range(ord('z') - ord('a') + 1)] if memo else []
        self._root = self._build_tree()

        # Set binary codes for quick retrieval if has memo. Otherwise, find
        # dynamically during encoding process
        if memo:
            self.set_codes()

    def __str__(self) -> str:
        """
        String representation of Huffman Tree using pre-order traversal

        Returns:
            str: pre-order traversal of Huffman Tree nodes in format 
                characters: frequency
        """
        def preorder(root: Optional['HuffmanNode']) -> List[str]:
            """
            Preorder traversal of Huffman Tree and its nodes.

            Args:
                root (HuffmanNode): root of a Huffman tree or subtree OR None

            Returns:
                List[str]: list of Python nodes as key-value pairs in format
                    character: frequency
            """
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

    def _prepare_leaf_nodes(self) -> 'Heap':
        """
        Helper method for building the priority queue containing all leaf 
        nodes. It error checks inputs and builds new nodes to be placed in the
        queue. If memoization is activated for current instance, also places
        references to each leaf node in a memo list index corresponding to its
        character's position in the Latin (English) alphabet. Case insensitive.

        Returns:
            Heap: priority queue containing HuffmanNode objects within a min
                heap

        Raises:
            ValueError: character key is not a single, unique alphabetical
                character or frequency value is not an integer >= 1
        """
        nodes_pq = Heap()
        has_memo = self.has_memo()
        unique_chars = set()
        with open(self._frequency_table, 'r', encoding="utf-8") as freq_table:
            for line in freq_table:
                # Get character and frequency values
                character, _, frequency = line.strip().split()

                # Enforce case insensitivity
                character = character.lower()

                try:
                    frequency = int(frequency)
                except ValueError as ve:
                    # Error case: frequency is not a number
                    print(ve.args[0], file=stderr)

                if frequency < 1:
                    # Error case: cannot have negative frequency
                    error = "INVALID FREQUENCY: must be > 0"
                    raise ValueError(error)

                if character in unique_chars:
                    # Case: repeat characters in file
                    error = f"INVALID CHAR: {character} has already been added"
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

                # Add new node to priority queue. Account for memoization
                nodes_pq.heap_push(new_node)
                if has_memo:
                    index = ord(character) - ord('a')
                    self._memo[index] = new_node

                # Add character to set for error checking
                unique_chars.add(character)

        return nodes_pq

    def _build_tree(self) -> 'HuffmanNode':
        """
        Encodes characters and their frequencies as HuffmanNodes in a binary
        tree structure, or Huffman Tree.

        Returns:
            'HuffmanNode': root of new Huffman Tree
        """
        # Set up a priority queue with all leaf nodes
        nodes_pq = self._prepare_leaf_nodes()

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

    def set_codes(self) -> 'HuffmanTree':
        """
        Method for adding binary codes to Huffman tree nodes.

        Returns:
            HuffmanTree: current HuffmanTree object instance
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

        root = self._root
        preorder(root)

        return self

    def print_codes(self) -> str:
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

            if root.is_leaf():
                rep.append(f"{root.get_characters()}: {root.get_code()}")
                return rep

            if root.get_left():
                rep.extend(preorder(root.get_left()))

            if root.get_right():
                rep.extend(preorder(root.get_right()))

            return rep

        if not self.has_memo():
            # Case: without memoization toggled on, no codes are set to print
            self.set_codes()

        return ', '.join(preorder(self._root))

    def get_root(self) -> 'HuffmanNode':
        """
        Getter method for retrieving the root node of the Huffman Tree

        Returns:
            HuffmanNode: the root node
        """
        return self._root

    def has_memo(self) -> bool:
        """
        Checks if HuffmanTree nodes utilizes memoization. Here, it means nodes
        are referenced in a list with indices corresponding to each letter's
        position in the Latin (English) alphabet. This must have been set with
        HuffmanTree instantiation and cannot be changed.

        Returns:
            bool: True if memoization is used, otherwise False
        """
        return len(self._memo) != 0

    def get_memo(self) -> Optional[List['HuffmanNode']]:
        """
        Getter method for retrieving a list of leaf HuffmanNode objects, where
        each index i corresponds the value ord(char) - ord('a'), ord(char)
        being the unicode value of any character char.

        Returns:
            List[HuffmanNode]: memo list with references to HuffmanNodes in
                current instance of HuffmanTree OR None if this instance does
                not utilize memoization
        """
        return self._memo
