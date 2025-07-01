import os

def get_files_info(working_directory, directory=None):

    print(f"\ndirectroy: {directory}| working_directory: {working_directory}")

    #check if directory is outside working directory
    working_abs_path = os.path.abspath(working_directory)
    target_abs_path = os.path.abspath(os.path.join(working_directory, directory))
    print(f"\nworking_abs_path: {working_abs_path}")
    print(f"\ntarget_abs_path: {target_abs_path}")

    #check is directory
    if not os.path.isdir(target_abs_path):
        print(f'\nError: "{target_abs_path}" is not a directory')
        return f'\nError: "{target_abs_path}" is not a directory'
    
    

    if os.path.commonpath([working_abs_path, target_abs_path]) != working_abs_path:
        f'Error: Cannot list "{target_abs_path}" as it is outside the permitted working directory'

    #build and return contents of directory
    try:
        contents = os.listdir(target_abs_path)
    
    except PermissionError:
        return f'Error: Permission denied for directory "{target_abs_path}"'
    
    except Exception as e:
        return f'Error: An unexpected error occurred: {str(e)}'

    file_size_list = []
    for content in contents:
        try:
            size = os.path.getsize(content)
            is_dir = os.path.isdir(content)
        
        except PermissionError:
            return f'Error: Permission denied for file "{content}" in directory "{target_abs_path}"'
        
        except Exception as e:
            return f'Error: An unexpected error occurred while accessing file "{content}": {str(e)}'

        file_size_list.append(f"\n- {content}: file_size={size} bytes, is_dir={is_dir}")
    string=  "".join(file_size_list)
    print(f"string: {string}")
