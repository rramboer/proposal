from PIL import Image
import os

input_folder = "img/"
output_folder = "img_thumbnails/"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

max_dimension = 400

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        with Image.open(input_path) as img:
            # Calculate the thumbnail size while maintaining aspect ratio
            img.thumbnail((max_dimension, max_dimension))

            # Save the image with reduced quality
            img.save(output_path, "JPEG", quality=70)

        print(f"Processed: {file_name}")

print("Thumbnail generation complete!")
