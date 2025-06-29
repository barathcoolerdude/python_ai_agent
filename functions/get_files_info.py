import os

def get_files_info(working_directory, directory=None):

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    working_dir = working_directory.split("/")
    contents_of_directory = directory.split("/")
    print(f"working_dir: {working_dir}")
    print(f"\ncontents of directory: {contents_of_directory}")
    for i in range(len(working_dir)):
        print(f"\nworking_dir[{i}]: {working_dir[i]}")
        print(f"\ncontents_of_directory[{i}]: {contents_of_directory[i]}")
        if working_dir[i] != contents_of_directory[i]:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    print(f"contents of {directory}:")
    return "True"
    # if "readme.md" in working_dict:
        