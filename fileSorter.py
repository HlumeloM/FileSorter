import os  
# provides functions to interact with the operating system

import shutil
# offers high-level operations on files, such as copying and moving.

# Prompts the user to enter a path
# Uses os.listdir() to get a list of all files and directories in the specified path
path = input("Enter Path: ")
files = os.listdir(path)

# Begins a loop where file iterates over each item (file or directory)
# in the files list obtained from os.listdir(path).
# Uses os.path.splitext(file) to split file into filename and extension.
#Removes the dot from the extension using extension[1:], storing just the extension
for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    # Skip directories(folders) and hidden files
    if extension == '':
        continue

    # Create the directory if it does not exist
    destination_dir = os.path.join(path, extension)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Move the file to the new directory
    shutil.move(os.path.join(path, file), os.path.join(destination_dir, file))

print("Files have been sorted.")

#Add a method that regularly checks if there are new files in downloads and automaticaly sorts them
# into their respective folders 