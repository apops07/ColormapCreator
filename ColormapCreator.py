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

    kmeans = KMeans(n_clusters = n_colors, random_state = 42)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_.astype(int)
    return colors

def pastelColors(color):
    pastel = (np.array(color) + 255) // 2
    return tuple(pastel.astype(int))

def saveToFile(colors, pastel_colors, output_path):
    with open(output_path, "w") as file:
        file.write(f"{'Regular Colormap':20}{'Pastel Colormap':20}\n")
        for regular, pastel in zip(colors, pastel_colors):
            regular_hex = '#{:02x}{:02x}{:02x}'.format(*regular)
            pastel_hex = '#{:02x}{:02x}{:02x}'.format(*pastel)
            file.write(f"{regular_hex:20}{pastel_hex:20}\n")


def ColormapCreator(image_path, n_colors):

    colors = extract_colors(image_path, n_colors)
    pastel_colors = [pastelColors(color) for color in colors]

    img = Image.open(image_path)
    img_width, img_height = img.size

    # New image size (image + ColorPalette)
    swatch_height = 50
    padding = 10
    total_height = img_height + (swatch_height + padding) * 2 + padding

    output_img = Image.new('RGB', (img_width, total_height), 'white')
    output_img.paste(img, (0,0))

    draw = ImageDraw.Draw(output_img)

    try:
        font = ImageFont.truetype("arial.ttf", 14)
    except IOError:
        font = ImageFont.load_default()
    
    # Draw the regular color palette

    for i, color in enumerate(colors):
        x0 = i * (img_width // n_colors)
        x1 = (i + 1) * (img_width // n_colors)
        y0 = img_height + padding 
        y1 = y0 + swatch_height

        draw.rectangle([x0+2, y0, x1, y1], fill=tuple(color))
        hex_code = '#{:02x}{:02x}{:02x}'.format(*color)
        draw.text((x0 + 5, y0 + 5), hex_code, fill = 'black', font = font)
    
    # Draw the pastel color palette
    for i, pastel_color in enumerate(pastel_colors):
        x0 = i * (img_width // n_colors)
        x1 = (i + 1) * (img_width // n_colors)
        y0 = img_height + padding + swatch_height + padding
        y1 = y0 + swatch_height

        draw.rectangle([x0+2, y0, x1, y1], fill=tuple(pastel_color))
        hex_code = '#{:02x}{:02x}{:02x}'.format(*pastel_color)
        draw.text((x0 + 5, y0 + 5), hex_code, fill="black", font=font)
    
    return output_img, colors, pastel_colors

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ").strip()
    n_colors = int(input("Enter the number of colors to extract: "))

    if not os.path.exists(image_path):
        print("The specified file does not exist. Check if path is correct.")
    else:
        output_img, colors, pastel_colors = ColormapCreator(image_path, n_colors)
        output_path = "output_palette.png"
        output_img.save(output_path)
        print(f"Palette image saved as {output_path}")

        text_output_path = "output_colors.txt"
        saveToFile(colors, pastel_colors, text_output_path)
        print(f"Color data saved as {text_output_path}")
