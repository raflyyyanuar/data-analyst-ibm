import os

def rename_files_and_folders(directory):
    # Traverse the directory
    for root, dirs, files in os.walk(directory, topdown=False):
        # Rename directories
        for dir_name in dirs:
            new_dir_name = rename_string(dir_name)
            os.rename(os.path.join(root, dir_name), os.path.join(root, new_dir_name))

        # Rename files
        for file_name in files:
            new_file_name = rename_string(file_name)
            os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))

def rename_string(name):
    # Remove dot after number, replace spaces with dashes, and convert to lowercase
    name = name.replace('.', '', 1) if name[0].isdigit() and name[1] == '.' else name
    name = name.replace(' ', '-').lower()
    return name

# Example usage:
directory = "/home/raflyyyanuar/repos/data-analyst-udemy/1-introduction-to-data-analytics/"
rename_files_and_folders(directory)
