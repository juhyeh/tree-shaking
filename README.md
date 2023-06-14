## Tree-shaking Coding Challenge

You are given a file that contains an entire program in Python. You need to write a program that does some cleanup.

1. Write a func that identifies all of the uncalled funcs in the program.
2. Write a func that can remove all of the uncalled funcs in the program.
   ** Hint: Regex is useful for complex text matching. regex101.com is also useful for testing regex
   ** There should be a function called main() that is the entry, and that one should never be considered uncalled.

### Solution

The solution to this challenge is written in `tree-shaking.py`.
The `main.py` file is an example file you can test the tree-shaking functions with.
The main.py will be updated once the script in tree-shaking.py is ran with it.

### To run the script

1. Clone this repo
2. In your terminal, `cd` into the repo and run `python tree-shaking.py`
3. If you would like to test this script with other python files, add the file into this directory and update the file_path variable in tree-shaking.py.
