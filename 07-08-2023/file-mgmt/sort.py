import os
import shutil

def copy_jpg_files_recursive(source_dir, dest_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Recursively search for .jpg files and copy them
    for root, _, files in os.walk(source_dir):
        for filename in files:
            if filename.endswith(".jpg"):
                src_path = os.path.join(root, filename)
                dest_path = os.path.join(dest_dir, filename)
                shutil.copy(src_path, dest_path)
                print(f"Copied {filename} to {dest_path}")

def display_current_and_parent_directory():
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    
    print(f"Current Working Directory: {current_dir}")
    print(f"Parent Working Directory: {parent_dir}")

if __name__ == "__main__":
    source_directory = "."
    destination_directory = "./JPG"

    copy_jpg_files_recursive(source_directory, destination_directory)
    display_current_and_parent_directory()
