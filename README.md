# Huffman Encoding

Contains a primary package and a support one for the Huffman Encoding and
Decoding processes. Given a frequency table as a text file, with each line
being a 'character - frequency' key-value pair. The table is then converted
into a Huffman Tree that can be used to decode or encode lines of binary or
regular strings based on user preference.

Precedence for characters that have the same frequency is generally open to
interpretation. In this repository, the Huffman Encoding Tree resolves ties by
giving single letter groups precedence (left child node) over multiple letter
groups, then alphabetically. Characters must be alphabetic, but cases are not
enforced (they default to lowercase).

## Running Huffman Encoding

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m hencoding -h`. This will print the help
   message.
4. Run the program as a module (with real inputs):
   `python -m hencoding <some_input_file> <some_output_file> --encode/--decode`
   - Example: `python -m hencoding resources/input.txt resources/output.txt --encode`
   - Optional - run the program as a module with errors outputted to stderr:
     `python -m hencoding <some_input_file> <some_output_file> --decode --debug`
   - Optional - run the program as a module using multiple optional arguments:
     `python -m hencoding <some_input_file> <some_output_file> --encode --memo`
   - Optional - run the program as a module using optional file:
     `python -m hencoding <some_input_file> <some_output_file> --encode --frequency_table <some_frequency_table_file>`

Output will be written to the specified output file after processing the input
file.

### Huffman Encoding Usage:

```commandline
usage: python -m hencoding [-h] in_file out_file [--frequency_table] frequency_table
        [--debug] [--memoize] [--encode] [--decode]

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname

optional arguments:
  --debug             Toggles debug mode to log errors to stderr
  --frequency_table   Followed by custom frequency table file pathname
  --memoize           Toggles on memoization for encoding
  --encode            Indicates to encode input file strings
  --decode            Indicates to decode input file strings
  -h, --help          show this help message and exit

  NOTE: Either [--encode] or [--decode] must be toggled, not neither nor both
  at once. The option [--memo] may be run with both but will not affect
  decoding process.
```

Usage statements reference

| Symbol        | Meaning                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------ |
| [var]         | variable var is optional.                                                                                          |
| var           | variable var is required. All positional arguments are required.                                                   |
| -v, --version | This refers to a flag. One dash + one letter OR two dashes and a whole word. Some flags take one or more arguments |
| +             | This argument consumes 1 or more values                                                                            |
| \*            | This argument consumes 0 or more values                                                                            |

### Project Layout

- [Huffman_Encoding/](.): The parent or "root" folder containing all of these
  files
  - [README.md](README.md):
    The guide you're reading.
  - [hencoding](hencoding):
    This is the _package_.
    - [`__init__.py`](hencoding/__init__.py)
      This contains the functionality that is automatically run when importing
      the package
    - [`__main__.py`](hencoding/__main__.py)
      This file is the entrypoint to the hencoding package when run as a program
    - `*.py`
      These are Python scripts that do the actual work
  - [support](support):
    This is a separate package for supporting modules not directly involved in
    encoding / decoding.
    - [`__init__.py`](support/__init__.py)
      This contains the functionality that is automatically run when importing
      the package
    - `*.py`
      These are the supporting Python modules
  - [Resources](resources)
    - `*.txt`
      These are the input files for testing code
    - `*_output.txt`
      These are the output files for metrics and data from input files with
      same name

### Python Version

3.10.x

### IDE / Editor

Visual Studio Code (WSL: Ubuntu)
