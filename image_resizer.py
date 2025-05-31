# How to run this script:
# 1. Make sure you have the Pillow library installed:
#    pip install Pillow
# 2. Run the script from your terminal:
#    python image_resizer.py <path_to_your_image>
#    Example: python image_resizer.py my_photo.jpg
#
# This script will create a new image file in the same directory as the input image,
# with "_resized_WIDTHxHEIGHT" appended to the original filename.

from PIL import Image
import sys
import os

def resize_image(input_image_path, output_resolution=(1024, 768)):
    """
    Resizes an image to the specified resolution.

    Args:
        input_image_path (str): The path to the input image.
        output_resolution (tuple): A tuple (width, height) for the output resolution.
    """
    if not os.path.exists(input_image_path):
        print(f"Error: Input image path '{input_image_path}' not found.")
        return

    try:
        img = Image.open(input_image_path)
        resized_img = img.resize(output_resolution)

        # Construct output filename
        directory, filename = os.path.split(input_image_path)
        name, ext = os.path.splitext(filename)
        output_filename = f"{name}_resized_{output_resolution[0]}x{output_resolution[1]}{ext}"
        output_image_path = os.path.join(directory, output_filename)
        if not directory: # If input was just a filename in the current dir
            output_image_path = output_filename

        resized_img.save(output_image_path)
        print(f"Image resized successfully and saved to '{output_image_path}'")
    except FileNotFoundError:
        print(f"Error: The file '{input_image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python image_resizer.py <input_image_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    # You can add more command-line arguments here to specify output resolution
    # For now, it uses the default 1024x768
    resize_image(input_path)