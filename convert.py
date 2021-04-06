!
from os import walk, mkdir
import pyvips

# sudo apt-get install libvips
# pip install pyvips

# shapes = ["circle", "naked", "square"]
# colors = ["blue", "gray", "green", "red"]
PATH = "svg/"

for (root, dirs, files) in walk(PATH):
    for f in files:
        if ".svg" in f:
            try:
                mkdir(path=f"{root}/png/")
            except OSError as error:
                pass
            convert_file = pyvips.Image.thumbnail(f"{root}/{f}", 52, height=52)
            convert_file.write_to_file(f"{root}/png/{f.replace('svg', 'png')}")
