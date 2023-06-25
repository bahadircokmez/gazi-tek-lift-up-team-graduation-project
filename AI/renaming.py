import os

# Path to the folder containing the images
folder_path = "C:/Users/HP/OneDrive/Masaüstü/Dataset"

# Get a list of all the files in the folder
files = os.listdir(folder_path)

# Filter out any files that are not images (you can change the list of file extensions as needed)
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]

# Rename the image files with numbers starting from 1
for i, f in enumerate(image_files):
    file_extension = os.path.splitext(f)[1]
    new_file_name = str(i+1) + file_extension
    os.rename(os.path.join(folder_path, f), os.path.join(folder_path, new_file_name))