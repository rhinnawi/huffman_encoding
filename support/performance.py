"""
performance

This module holds a class that tracks metrics and performance. It allows for
maintaining a timer for runtime, storing size of a process (user's discretion),
and tracking previous successes' and errors' sizes and runtimes. Methods that 
would otherwise return None instead return current instance to allow for method
chaining.

Author: Rani Hinnawi
Date: 2023-07-25
"""
from sys import stderr
from time import time_ns
from typing import Dict, List


class Performance:
    """
    Class for logging space and time performance based stored size and runtime.
    """

    def __init__(self) -> None:
        """
        Creates instance of Performance class that saves start time, stop time,
        and size of input. It also logs previous runs. Times are all in ns
        """
        self._size = 0
        self._start_time = time_ns()
        self._stop_time = time_ns()

        # Log previous successes and failures. Track number of each
        self._successes: Dict[int, List[int]] = {}
        self._errors: Dict[int, List[int]] = {}

        self._num_successes = 0
        self._num_errors = 0

    def __str__(self):
        """
        Returns a string representation of the Performance class
        """
        return f"Size: {self._size}, Runtime: {self.get_runtime()}ns"

    def set_size(self, size: int) -> 'Performance':
        """
        Setter method for size attribute

        Args:
            size (int): user-defined size of a process. Must be >= 0

        Returns:
            "Performance": Current instance of Performance class with updated
                size attribute
        """
        if (size < 0):
            print("Invalid size. Must be >= 0. Automatically setting to 0.",
                  file=stderr)

        self._size = max(size, 0)
        return self

    def get_size(self) -> int:
        """
        Getter method for size attribute

        Returns:
            int: Stored size of current instance of Performance class
        """
        return self._size

    def start(self) -> 'Performance':
        """
        Setter method for start time. Essentially starts a timer in nanoseconds

        Returns: 
            "Performance": Current instance of Performance class with updated 
                _start_time attribute
        """
        self._start_time = time_ns()
        return self

    def stop(self) -> 'Performance':
        """
        Setter method for stop time. Essentially ends a timer in nanoseconds

        Returns: 
            "Performance": Current instance of Performance class with updated 
                _stop_time attribute
        """
        self._stop_time = time_ns()
        return self

    def get_runtime(self) -> int:
        """
        Returns runtime based off stored start and stop times. If start is
        stored after stop time, returns 0

        Returns:
            int: Difference between currently stored start and stop times or 0
        """
        return max(self._stop_time - self._start_time, 0)

    def log_success(self) -> 'Performance':
        """
        Method for logging the current metrics stored as a success

        Returns:
            "Performance": Current instance of Performance class with newly 
                logged success run
        """
        new_log = self.get_runtime()

        # Add as a key-value pair {size: runtime}
        if (self._size in self._successes):
            self._successes[self._size].append(new_log)
        else:
            self._successes[self._size] = [new_log]

        # Update number of success
        self._num_successes += 1

        return self

    def log_error(self) -> 'Performance':
        """
        Method for logging the current metrics stored as an error

        Returns:
            "Performance": Current instance of Performance class with newly
                logged failed run
        """
        new_log = self.get_runtime()

        # Add as a key-value pair {size: runtime}
        if (self._size in self._errors):
            self._errors[self._size].append(new_log)
        else:
            self._errors[self._size] = [new_log]

        # Update number of errors
        self._num_errors += 1

        return self

    def get_successes(self) -> Dict[int, List[int]]:
        """
        Getter method for retrieving logged successes. They are formatted as
        key-value pairs, with keys being the sizes and values being a list of
        runtimes (ns) for successful runs given that size

        Returns:
            dict: Key-value pairs of all successful runs
        """
        return self._successes

    def get_errors(self) -> Dict[int, List[int]]:
        """
        Getter method for retrieving logged failures. They are formatted as
        key-value pairs, with keys being the sizes and values being a list of
        runtimes (ns) for failed runs given that size

        Returns:
            dict: Key-value pairs of all failed runs that returned errors
        """
        return self._errors

    def get_num_successes(self) -> int:
        """
        Getter method that returns the total number of successful runs logge

        Returns:
            int: Number of successful runs logged
        """
        return self._num_successes

    def get_num_errors(self) -> int:
        """
        Getter method that returns the total number of failed runs logged

        Returns:
            int: Number of errors logged
        """
        return self._num_errors
