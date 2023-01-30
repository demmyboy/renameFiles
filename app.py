import os

# The path to the folder containing the files
folder_path = r'C:\Users\demol\Downloads\PythonProjects\renameFiles\images'

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    # Ignore hidden files and directories
    if filename.startswith("."):
        continue
    # Get the full path of the file
    file_path = os.path.join(folder_path, filename)
    # Check if the file is a regular file (not a directory)
    if os.path.isfile(file_path):
        # Remove the word "old_" from the beginning of the name
        new_filename = filename.replace("resized_", "")
        # Get the full path of the new file name
        new_file_path = os.path.join(folder_path, new_filename)
        # Rename the file
        os.rename(file_path, new_file_path)
