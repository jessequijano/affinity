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
    my_file.write("# Reference for Icons")
    my_file.write("\n")
    for (root, dirs, files) in walk(PATH):
        for f in files:
            if "green.png" in f:
                my_file.write(f"\n## {f}\n")
                my_file.write(f"\n![{f}]({root}/{f})\n")

    if __name__ == "__main__":
        main()
