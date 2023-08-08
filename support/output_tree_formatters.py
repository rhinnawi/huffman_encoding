"""
output_tree_formatters

This module contains helper functions called to format strings intended to be
outputted to a text file. These are specifically for formatting Huffman Trees
and nodes.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from sys import setrecursionlimit
from typing import Optional, List, Tuple
from lab3.huffman_tree import HuffmanTree
from lab3.huffman_node import HuffmanNode

# Set recursion limit. Python default: 1000. Should not need to exceed number
# of letters in Latin (English) alphabet. +1 for buffer. Limit extended for
# Python built-in functions
RECURSION_LIMIT = 500
setrecursionlimit(RECURSION_LIMIT)


def format_huffman_tree(huffman_tree: 'HuffmanTree', nodes_per_line: int) \
        -> str:
    """
    Function that formats the number of Huffman Tree nodes per line for easier
    readability in an output file.

    Args:
        huffman_tree (HuffmanTree): Huffman Tree being printed out
        nodes_per_line (int): max number of Huffman Nodes printed per line

    Returns:
        str: string representation of Huffman Nodes

    Raises:
        ValueError: when nodes_per_line is not a positive integer
    """
    def preorder(root: Optional['HuffmanNode'], nodes_left=nodes_per_line) \
            -> Tuple[List[str], int]:
        """
        Preorder traversal of Huffman Tree and its nodes.

        Args:
            root (HuffmanNode): root of a Huffman tree or subtree OR None

        Returns:
            List[str]: list of Python nodes as key-value pairs in format
                character: frequency
        """
        # Add nodes to 'representation' list
        rep = []

        # Visit root, then left, then right
        if not root:
            return rep, nodes_left

        node_str = str(root)

        # Node is placed on new line when 0 nodes left per line are remaining
        if nodes_left == 0:
            node_str = "\n\t" + node_str
            nodes_left = nodes_per_line
        else:
            nodes_left -= 1

        # Add HuffmanNode string, then visit left and right branches
        rep.append(node_str)

        if root.get_left():
            left, nodes_left = preorder(root.get_left(), nodes_left)
            rep.extend(left)

        if root.get_right():
            right, nodes_left = preorder(
                root.get_right(), nodes_left)
            rep.extend(right)

        # Returns preorder representation list and remaining nodes for
        # possible recursive calls
        return rep, nodes_left

    if nodes_per_line < 1:
        error = "There must be at least 1 node per line"
        raise ValueError(error)

    output, _ = preorder(huffman_tree.get_root())
    return ", ".join(output)


def format_huffman_tree_binary_codes(huffman_tree: 'HuffmanTree',
                                     nodes_per_line: int) -> str:
    """
    Function that formats the number of Huffman Tree leaf nodes and their
    respective binary Huffman Codes per line for easier readability in an
    output file. 

    Args:
        huffman_tree (HuffmanTree): Huffman Tree codes being printed out
        nodes_per_line (int): max number of Huffman Nodes printed per line

    Returns:
        str: string representation of Huffman Nodes

    Raises:
        ValueError: when nodes_per_line is not a positive integer
    """
    def preorder(root: Optional['HuffmanNode'], nodes_left=nodes_per_line) \
            -> Tuple[List[str], int]:
        """
        Preorder traversal of Huffman Tree and its nodes. Only outputs leaf
        nodes.

        Args:
            root (HuffmanNode): root of a Huffman tree or subtree OR None

        Returns:
            List[str]: list of Python nodes as key-value pairs in format
                character: Huffman Code
        """
        # Add nodes to 'representation' list
        rep = []

        # Check root, then visit left and right subtrees
        if not root:
            # Case: Node (root) does not exist
            return rep, nodes_left

        if root.is_leaf():
            # Case: root is a leaf. Can add it and its code to output
            # node_str = f"{root.get_characters()}: {root.get_code()}"
            node_str = f"{root} - {root.get_code()}"

            # Node is placed on new line when 0 nodes left per line are remaining
            if nodes_left == 0:
                node_str = "\n\t" + node_str
                nodes_left = nodes_per_line
            else:
                nodes_left -= 1

            rep.append(node_str)
            return rep, nodes_left
        else:
            # Get left subtree leaf nodes
            if root.get_left():
                left, nodes_left = preorder(root.get_left(), nodes_left)
                rep.extend(left)

            # Get right subtree leaf nodes
            if root.get_right():
                right, nodes_left = preorder(
                    root.get_right(), nodes_left)
                rep.extend(right)

            # Returns preorder representation list and remaining nodes for
            # possible recursive calls
            return rep, nodes_left

    if nodes_per_line < 1:
        error = "There must be at least 1 node per line"
        raise ValueError(error)

    output, _ = preorder(huffman_tree.get_root())
    return '\t' + ", ".join(output)
