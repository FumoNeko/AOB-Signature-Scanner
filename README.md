# AOB-Signature-Scanner
A simple script designed for Array of Byte signature scanning. Compares two AOB signatures and creates signature with marked unknowns, but works with any strings of equal length.

Written in Python 3.10.

# Usage
The script prompts you for everything, run it in IDLE or your favorite shell. There are no command arguments.

There is no quit option, use CTRL+C or abort the script externally.

# Known Bugs
If you enter linebreak characters into the IDLE Terminal it will accept two inputs. Not sure if it's because python doesn't flush `input()` stdin or if it's because the terminal emulator interprets a linebreak and a prompt to move forward in the script. I'm not going to fix this, copy paste then remove the linebreaks if you have them.
