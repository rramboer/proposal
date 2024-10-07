import os

# Directory containing the images
img_dir = "img/"

# Get a sorted list of all the image files in the directory
photos = sorted([f for f in os.listdir(img_dir) if f.endswith('.jpg')], key=lambda x: int(x.split('.')[0]))

# Renaming each photo sequentially starting from 1
for i, photo in enumerate(photos, start=1):
    old_path = os.path.join(img_dir, photo)
    new_name = f"{i}.jpg"
    new_path = os.path.join(img_dir, new_name)

    # Rename the file
    os.rename(old_path, new_path)

print(f"Renamed {len(photos)} photos successfully.")
