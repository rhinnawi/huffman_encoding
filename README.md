# Prefix to Postfix

Huffman Encoding Tree. Resolves ties by giving single letter groups precedence (left child node) over multiple letter groups, then alphabetically.

## Running Prefix to Postfix

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m prefix_to_postfix -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m prefix_to_postfix <some_input_file> <some_output_file>`
   - Example: `python -m prefix_to_postfix resources/input.txt resources/output.txt`
   - Optional - run the program as a module with errors outputted to stderr:
     `python -m prefix_to_postfix <some_input_file> <some_output_file> --debug`

- Optional - run the program as a module using multiple optional arguments:
  `python -m prefix_to_postfix <some_input_file> <some_output_file> --debug --iterative`

Output will be written to the specified output file after processing the input file.

### Prefix to Postfix Usage:

```commandline
usage: python -m prefix_to_postfix [-h] in_file out_file [--debug] [--iterative]

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname

optional arguments:
  --debug     Toggles debug mode to log errors to stderr
  --iterative Toggles iterative implementation for prefix to postfix conversion. Default is recursive.
  -h, --help  show this help message and exit
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

- [PrefixToPostfix/](.): The parent or "root" folder containing all of these files
  - [README.md](README.md):
    The guide you're reading.
  - [prefix_to_postfix](prefix_to_postfix):
    This is the _package_.
    - [`__init__.py`](prefix_to_postfix/__init__.py)
      This contains the functionality that is automatically run when importing the package
    - [`__main__.py`](prefix_to_postfix/__main__.py)
      This file is the entrypoint to the Prefix to Postfix package when run as a program
    - `*.py`
      These are Python scripts that do the actual work
  - [support](support):
    This is a separate package for supporting modules not directly involved in prefix to postfix conversions.
    - [`__init__.py`](support/__init__.py)
      This contains the functionality that is automatically run when importing the package
    - `*.py`
      These are the supporting Python modules
  - [Resources](resources)
    - `*_input.txt`
      These are the input files for testing code
    - `*_output.txt`
      These are the output files for metrics and data from input files with same name

### Python Version

3.10.x

### IDE / Editor

Visual Studio Code (WSL: Ubuntu)
