#!/usr/bin/env python

"""
Script used to create reference.md
"""

from os import walk

PATH = "svg/"


def main():

    """
    All the action
    """


with open("reference.md", "w") as my_file:
    my_file.write("# Reference for Icons\n")
    my_file.write("\n")
    my_file.write("|Name|Icon|Name|Icon|Name|Icon|\n")
    my_file.write("|:-------------:|:----------|:-----------:|:-----------|:-----------:|:-----------|\n")
    for (root, dirs, files) in walk(PATH):
        count = 0
        for f in files:
            if ".png" in f:
                count += 1
                if count == 1:
                    my_file.write(f"|{f}|![{f}]({root}/{f})|")
                if count == 2:
                    my_file.write(f"{f}|![{f}]({root}/{f})|")
                if count == 3:
                    my_file.write(f"{f}|![{f}]({root}/{f})|\n")
                    count = 0
    my_file.write("|\n")

if __name__ == "__main__":
    main()
