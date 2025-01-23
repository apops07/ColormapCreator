"""
Created on Wed Jan 15 11:22:50 2025

@author: apops07
"""

import numpy as np
import os

# Program that generates a color palette from an input image

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ").strip()
    n_colors = int(input("Enter the number of colors to extract: "))

    if not os.path.exists(image_path):
        print("The specified file does not exist. Check if path is correct.")
    else:
        output_img = generate_palette_image(image_path, n_colors)
        output_path = ".\output_palette.png"
        output_img.save(output_path)
        print(f"Palette image saved as {output_path}")

