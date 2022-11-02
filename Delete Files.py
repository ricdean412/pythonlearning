import os
# import shutil #need to delete files

# path = "delete.txt"
path = "folder"

try:
    os.remove(path) #delete a file
    os.rmdir(path)  # delete an empty directory(folder)
    # shutil.rmtree(path) #dangerous function as it will delete all in folder.
except FileNotFoundError:
    print("The file you're looking for is not found.")
except PermissionError:
    print("You don't have permission to delete this.")
except OSError:
    print("The folder is not empty.")
else:
    print(path+ " was deleted.")
