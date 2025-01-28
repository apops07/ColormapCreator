"""
Created on Wed Jan 15 11:22:50 2025

@author: apops07
"""

import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont
from sklearn.cluster import KMeans

# Program that generates a color palette from an input image

#Color extraction using K-Means clustering
def extract_colors(image_path, n_colors):
    img = Image.open(image_path).convert('RGB')
    img_data = np.array(img)

    pixels = img_data.reshape(-1,3)

    kmeans = KMeans(n_clusters = n_colors, random_state = 17)
    kmeans.fit(pixels)

def pastelColors(color):
    pastel = (np.array(color)+255//2)
    return tuple(pastel)

def saveToFile(colors, pastel_colors, output_path):
    with open(output_path, "w") as file:
        file.write(f"{'Regular Colormap':<20}{'Pastel Colormap':<20}\n")
        for regular, pastel in zip(colors, pastel_colors):
            regular_hex = '#{:02x}{:02x}{:02x}'.format(*regular)
            pastel_hex = '#{:02x}{:02x}{:02x}'.format(*pastel)
            file.write(f"{regular_hex:<20}{pastel_hex:<20}\n")


def ColormapCreator(image_path, n_colors):
    colors = extract_colors(image_path, n_colors)
    pastel = [pastelColors(color) for color in colors]


if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ").strip()
    n_colors = int(input("Enter the number of colors to extract: "))

    if not os.path.exists(image_path):
        print("The specified file does not exist. Check if path is correct.")
    else:
        output_img = ColormapCreator(image_path, n_colors)
        output_path = ".\output_palette.png"
        output_img.save(output_path)
        print(f"Palette image saved as {output_path}")

