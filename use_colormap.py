def load_palette(file_path, mode="Regular Colormap"):
    """
    Reads a color palette from a text file and returns a dictionary of colors.
    
    :param file_path: Path to the output_colors.txt file
    :param mode: "Regular Colormap" or "Pastel Colormap" to choose the color mode
    :return: Dictionary of colors {color_name: hex_value}
    """
    palette = {}

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("#") or not line:  # Skip comments and empty lines
                continue

            parts = line.split(",")
            if len(parts) == 3:
                name, regular, pastel = parts
                if mode == "Regular Colormap":
                    palette[name.lower()] = regular
                elif mode == "Pastel Colormap":
                    palette[name.lower()] = pastel
                else:
                    raise ValueError("Mode must be 'Regular Colormap' or 'Pastel Colormap'")
    print(palette)
    return palette