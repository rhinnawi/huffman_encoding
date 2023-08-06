"""
heap

This module contains a Heap class that implements the heap ADT, including
several optional methods. The underlying data structure is a Python List. As a 
stylistic choice, methods that would otherwise return None will instead return
self, allowing for method chaining. 

Author: Rani Hinnawi
Date: 2023-08-08
"""
from typing import List, TypeVar, Optional

# Set up generic type for stack to remain type-agnostic
T = TypeVar('T')


class Heap:
    """
    This class holds items of any type in a generic Max Heap data structure.
    Items must be of the same type and allow for >, <, !=, and == comparisons.
    All uses of the term 'heap' specifically reference a max heap.
    """

    def __init__(self):
        """
        Instantiate an empty heap
        """
        self.heap: List[Optional[T]] = []

    def __str__(self) -> str:
        """
        Return a basic string representation of the heap
        """
        return f"Heap[{', '.join(map(str, self.heap))}]"

    def heap_push(self, item: T) -> 'Heap':
        """
        Adds new item to the heap. Maintains heap properties with insertion.

        Args:
            item (T): new item being added to heap

        Returns: 
            'Heap': current instance of the heap
        """
        self.heap.append(item)
        self._percolate_up(self.size() - 1)
        return self

    def heapify(self) -> 'Heap':
        """
        Enforces max heap properties. The top item must carry the max value,
        and each node must be larger than its child nodes.

        Returns:
            'Heap': current instance of the heap
        """
        for i in range(self.size() // 2, -1, -1):
            self._percolate_down(i)

        return self

    def is_empty(self) -> bool:
        """
        Method indicating if current heap instance holds any items.

        Returns:
            bool: True if empty. False if contains >= 1 item(s)
        """
        return self.size() == 0

    def get_root(self) -> T:
        """
        Getter method for max value, placed at the root of the heap.

        Returns:
            T: max value in heap

        Raises:
            IndexError: if heap is empty
        """
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self) -> int:
        """
        Method that returns the number of items on the current heap instance.

        Returns:
            int: number of items on the heap
        """
        return len(self.heap)

    def heap_pop(self):
        """
        Removes and replaces the item on the heap with the largest value,
        placed at the root. Maintains max heap properties.

        Returns:
            T: max value in heap

        Raises:
            IndexError: if heap is empty
        """
        if self.is_empty():
            raise IndexError("Heap is empty")

        root = self.heap[0]
        last_element = self.heap.pop()

        if not self.is_empty():
            # Default case: >= 1 element(s) remain on the heap
            self.heap[0] = last_element
            self._percolate_down(0)
        return root

    def _percolate_up(self, index: int) -> 'Heap':
        """
        Helper method for moving an item up the heap to a correct position
        such that it is larger than its child nodes.

        Args:
            index (int): position of item in the underlying List, self.heap

        Returns:
            'Heap': current instance of the heap
        """
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            # Swap
            self.heap[index], self.heap[parent_index] = \
                self.heap[parent_index], self.heap[index]

            # Update indices to reflect item's new position and new parent
            index = parent_index
            parent_index = (index - 1) // 2

        return self

    def _percolate_down(self, index: int) -> 'Heap':
        """
        Helper method for moving an item down the heap to a correct position
        such that it is larger than its child nodes.

        Args:
            index (int): position of item in the underlying List, self.heap

        Returns:
            'Heap': current instance of the heap
        """
        child_index = 2 * index + 1
        value = self.heap[index]
        heap_size = self.size()

        while child_index < heap_size:
            # Find the max among the node and all the node's children
            min_value = value
            min_index = -1

            for i in range(2):
                child = child_index + i
                if child < heap_size and self.heap[child] < min_value:
                    min_value = self.heap[child]
                    min_index = child

            if min_value == value:
                return self
            else:
                # Case: current item is smaller than at least one child. Swap
                # and continue percolating down heap
                self.heap[index], self.heap[min_index] = \
                    self.heap[min_index], self.heap[index]
                index = min_index
                child_index = 2 * index + 1

        return self
