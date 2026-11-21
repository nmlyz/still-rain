# Field at Dusk

A small program that writes a short piece of text to a file.

## What it does

Running `main.py` writes a single short text to `entry.txt` inside the
output directory. The output directory is taken from the `MAKEFUN_OUTPUT`
environment variable when it is set, and defaults to `/output` otherwise.

Before writing, the program checks that the text is between 1 and 280
characters long, is not only whitespace, and does not end with a newline.
The file is written atomically (via a temporary file in the same directory,
followed by a rename) with mode `0644`, so repeated runs produce
byte-identical output.

## Usage

```sh
python3 main.py
```

Requires Python 3.13. No network access is needed.
