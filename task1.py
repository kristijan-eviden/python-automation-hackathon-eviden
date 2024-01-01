import os

""" TASK 1 (15 points):
    In this task you are supposed to write code which will help you automate deleting files from your system!
    In order to achieve that you should research python library 'os' which enables us to directly control our system.
    Look up functions: os.path.isfile, os.remove, os.listdir, os.path.join and file.endswith.
    Don't forget to make your code check for exceptions!"""

""" SUBTASK 1 (5 points): Delete BlackDoodleGroupProjectPresentation.pptx file from subtask1 folder. """

file_path = "C:/Programming/new-year-new-me/file_to_be_deleted/subtask1/Cantus Punishments.pdf"

print(file_path)

if os.path.isfile(file_path):
    #os.remove(file_path)
    print("File has been removed successfully!")
else:
        print("This file does NOT exist!")

""" SUBTASK 2 (5 points): Delete all files from subtask2 folder. """

# List all files in the folder
folder_path = "C:/Programming/new-year-new-me/file_to_be_deleted/subtask2"
files = os.listdir(folder_path)
        
# Iterate over each file and delete
for file in files:
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Deleted: {file_path}")

print(f"All files in {folder_path} have been deleted.")

""" SUBTASK 3 (5 points): Delete all .pdf files from subtask3 folder. """
# List all files in the folder
folder_path2 = "C:/Programming/new-year-new-me/file_to_be_deleted/subtask3"
files = os.listdir(folder_path2)
        
# Iterate over each file and delete if it has a .pdf extension
for file in files:
    file_path = os.path.join(folder_path2, file)
    if os.path.isfile(file_path) and file.endswith('.pdf'):
        os.remove(file_path)
        print(f"Deleted: {file_path}")

print(f"All .pdf files in {folder_path2} have been deleted.")