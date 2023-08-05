"""
__main__

This is the entry point for the huffman_encoding package. It runs when explicity 
called and not by default when the package is imported. It can be called by the
command: python -m huffman_encoding input_file output_file [--debug]

The primary functionality lies in the package modules, and not directly in the
main module here.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from sys import stderr
from pathlib import Path
import argparse
from support.is_valid_io import is_valid_io

DEFAULT_FREQUENCY_TABLE_PATH = "./DefaultFreqTable.txt"

# Set up command line argument parsing
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input_file", type=str, help="Input file pathname")
arg_parser.add_argument("output_file", type=str, help="Output file pathname")
arg_parser.add_argument("--frequency_table", type=str,
                        help="(Optional) Frequency table file pathname")
arg_parser.add_argument("--debug", action="store_true",
                        help="Toggles debug mode to log errors to stderr")
args = arg_parser.parse_args()

# Convert file names into paths
in_file = Path(args.input_file)
out_file = Path(args.output_file)
freq_table = Path(args.frequency_table) if args.frequency_table else Path(
    DEFAULT_FREQUENCY_TABLE_PATH)

# Validate file paths then run main program
try:
    is_valid_io(in_file, out_file)
    # run_conversions(in_file, out_file,
    #                 iterative=args.iterative, debug=args.debug)
    print('OK')
except FileNotFoundError as fnfe:
    error_message = fnfe.args[0]
    if (args.debug):
        print(error_message, file=stderr)
