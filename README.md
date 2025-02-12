# ColormapCreator

This Python project generates a color palette from an input image using K-Means clustering to extract dominant colors. Additionally, it creates pastel versions of these colors and saves them as an image and a text file. 
Tool dedicated to aesthetic data visualization, tuned to specific projects, companies and clients.

## Features
- Extracts dominant colors from an image using K-Means clustering.
- Generates pastel versions of the extracted colors.
- Saves the color palette as an image with labeled hex codes.
- Stores the hex codes of both normal and pastel colors in a text file.

## Usage
1. Run the script:
   ```bash
   python image_color_palette.py
   ```
2. Enter the path to the image file when prompted.
3. Specify the number of colors to extract.
4. The script will generate:
   - `output_palette.png` containing the original image and the generated color palette.
   - `output_colors.txt` listing the extracted colors and their pastel versions.

## Output Files
- **`output_palette.png`**: An image displaying the original picture and the color palette.
- **`output_colors.txt`**: A text file containing hex codes of the extracted and pastel colors in a tabular format.


## License
This project is open-source and free to use.


