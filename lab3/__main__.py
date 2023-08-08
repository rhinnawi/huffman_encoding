"""
__main__

This is the entry point for the huffman_encoding package. It runs when explicity 
called and not by default when the package is imported. It can be called by the
command: 
python -m lab3 input_file output_file [--encode/decode] [...optional arguments]

The primary functionality lies in the package modules, and not directly in the
main module here.

Author: Rani Hinnawi
Date: 2023-08-08
"""
from sys import stderr
from pathlib import Path
import argparse
from support.is_valid_io import is_valid_io
from lab3.run import run

DEFAULT_FREQUENCY_TABLE_PATH = "lab3/DefaultFreqTable.txt"

# Set up command line argument parsing
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input_file", type=str, help="Input file pathname")
arg_parser.add_argument("output_file", type=str, help="Output file pathname")
arg_parser.add_argument("--frequency_table", type=str,
                        help="(Optional) Frequency table file pathname")
arg_parser.add_argument("--memoize", action="store_true",
                        help="Toggles on memoization for encoding")
arg_parser.add_argument("--debug", action="store_true",
                        help="Toggles debug mode to log errors to stderr")

# Either --encode or --decode may be passed in. Not both nor neither
group = arg_parser.add_mutually_exclusive_group(required=True)
group.add_argument("--encode", action="store_true",
                   help="Indicates to encode input file strings")
group.add_argument("--decode", action="store_true",
                   help="Indicates to decode input file strings")
args = arg_parser.parse_args()

# Convert file names into paths
in_file = Path(args.input_file)
out_file = Path(args.output_file)
freq_table = Path(args.frequency_table) if args.frequency_table else Path(
    DEFAULT_FREQUENCY_TABLE_PATH)

# Validate file paths then run main program
try:
    is_valid_io(in_file, out_file, freq_table)
    run(freq_table, in_file, out_file, encode=args.encode,
        memo=args.memoize, decode=args.decode, debug=args.debug)
except FileNotFoundError as fnfe:
    error_message = fnfe.args[0]
    if args.debug:
        print(error_message, file=stderr)
