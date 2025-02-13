def load_palette(file_path, mode="Regular Colormap"):
    """
    Reads a color palette from a text file and returns a dictionary of colors.
    
    :param file_path: Path to the output_colors.txt file
    :param mode: "Regular Colormap" or "Pastel Colormap" to choose the color mode
    :return: Dictionary of colors {color_name: hex_value}
    """
    palette = []

    with open(file_path, "r") as file:
        first_line = True  # Track the first line (headers)
        for line in file:
            line = line.strip()
            if first_line:  # Skip the header row
                first_line = False
                continue
            if line.startswith("#>") or not line: 
                continue

            parts = line.split()  # Use split() without arguments to handle multiple spaces/tabs
            if len(parts) == 2:
                regular, pastel = parts
                if mode == "Regular Colormap":
                    palette.append(regular)
                elif mode == "Pastel Colormap":
                    palette.append(pastel)
                else:
                    raise ValueError("Mode must be 'Regular Colormap' or 'Pastel Colormap'")
                
    return palette