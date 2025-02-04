import os

def count_files_and_folders(path):
    # Variables to store the count of files and folders
    num_files = 0
    num_folders = 0
    
    # Directories to completely ignore
    excluded_dirs = {'.git', '__pycache__', '.history', '.idea', 'node_modules'}

    # Dictionary to store the folder tree structure
    tree = {}

    # Recursive function to traverse through directories and files
    def traverse_directory(directory, tree_structure):
        nonlocal num_files, num_folders
        
        try:
            # Increase the folder count (only if it's not the root)
            if directory != path:
                num_folders += 1  

            # Create the tree structure for the folder
            tree_structure['name'] = os.path.basename(directory)
            tree_structure['subfolders'] = {}
            tree_structure['files'] = []

            # Loop through files and subdirectories in the current directory
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                
                if os.path.isdir(item_path):
                    # If it's a folder and not in the excluded list, traverse it
                    if item not in excluded_dirs:
                        tree_structure['subfolders'][item] = {}
                        traverse_directory(item_path, tree_structure['subfolders'][item])
                else:
                    # If it's a file, add it to the list of files
                    tree_structure['files'].append(item)
                    num_files += 1
        except PermissionError:
            print(f"Permission denied to folder: {directory}")
            return

    # Start traversing from the main folder
    traverse_directory(path, tree)

    # Return the tree structure, file count, and folder count
    return tree, num_files, num_folders

def print_tree(tree, indent=0):
    """Function to print the folder tree in a readable format"""
    print(" " * indent + tree['name'] + "/")
    for file in tree['files']:
        print(" " * (indent + 2) + file)
    for folder in tree['subfolders'].values():
        print_tree(folder, indent + 2)

# The main directory you want to scan
path = os.getcwd()  # Get the current directory

# Call the function
tree, num_files, num_folders = count_files_and_folders(path)

# Print the results
print(f"Number of folders (excluding ignored dirs): {num_folders}")
print(f"Number of files (excluding ignored dirs): {num_files}")
print("\nProject tree structure:")
print_tree(tree)

