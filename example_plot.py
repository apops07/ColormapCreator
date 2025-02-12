import matplotlib.pyplot as plt
from use_colormap import load_palette

# Load color palette (choose "regular" or "pastel")
my_palette = load_palette("output_colors.txt", mode="Regular Colormap")

# Example usage in a plot
colors = list(my_palette.values())  # Extract hex values

plt.bar(["A", "B", "C", "D"], [10, 15, 7, 12], color=colors)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart with Custom Colors")
plt.show()
