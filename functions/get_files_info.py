import os

def get_files_info(working_directory, directory=None):

    print(f"\ndirectroy: {directory}| working_directory: {working_directory}")

    #check if directory is outside working directory
    working_abs_path = os.path.abspath(working_directory)
    target_abs_path = os.path.abspath(os.path.join(working_directory, directory))

    #check is directory
    if not os.path.isdir(target_abs_path):
        return f'Error: "{target_abs_path}" is not a directory'
    
    #check if target directory is within working directory
    if os.path.commonpath([working_abs_path, target_abs_path]) != working_abs_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    #build and return contents of directory
    contents = os.listdir(target_abs_path)

    file_size_list = []
    for content in contents:
            try:
                full_path = os.path.join(target_abs_path, content)
                size = os.path.getsize(full_path)
                is_dir = os.path.isdir(full_path)
            
            except FileNotFoundError:
                return f'Error: File "{content}" does not exist in directory "{target_abs_path}"'
            
            except PermissionError:
                return f'Error: Permission denied for file "{content}" in directory "{target_abs_path}"'
            
            except Exception as e:
                return f'Error: An unexpected error occurred while accessing file "{content}": {str(e)}'

            file_size_list.append(f"\n- {content}: file_size={size} bytes, is_dir={is_dir}")
        
    string=  "".join(file_size_list)
    print(f"\nstring: {string}")
    return string 


def get_file_content(working_directory, file_path):
     
     #check if directory is outside working directory
    working_abs_path = os.path.abspath(working_directory)
    target_abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    #check is directory
    try:
        if not os.path.isfile(target_abs_path):
            f'Error: File not found or is not a regular file: "{file_path}"'

    except FileNotFoundError:
        return f'Error: File "{file_path}" does not exist in directory "{working_directory}"'
    
    except PermissionError:
        return f'Error: Permission denied for file "{file_path}" in directory "{working_directory}"'
    
    except Exception as e:
        return f'Error: An unexpected error occurred while accessing file "{file_path}": {str(e)}'
    
    #check if target directory is within working directory
    try:
        if os.path.commonpath([working_abs_path, target_abs_path]) != working_abs_path:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        
    except Exception as e:
        return f'Error: An unexpected error occurred while checking file path "{file_path}": {str(e)}'
    
    except ValueError:
        return f'Error: Invalid file path "{file_path}"'
    
    except Exception as e:
        return f'Error: An unexpected error occurred while checking file path "{file_path}": {str(e)}'
    
    with open(target_abs_path, 'r') as file:
        content = file.read(10000)
        rest = file.read(1)

        if rest:
            content += f'[...File "{file_path}" truncated at 10000 characters]'

    return content

def write_file(working_directory, file_path, content):

     #check if directory is outside working directory
    working_abs_path = os.path.abspath(working_directory)
    target_abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    #check is directory
    try:
        if os.path.dirname(target_abs_path):
            os.makedirs(os.path.dirname(target_abs_path), exist_ok=True)

        if not os.path.isfile(target_abs_path):
            with open(target_abs_path, "w") as file:
                pass

    except FileNotFoundError:
        return f'Error: File "{file_path}" does not exist in directory "{working_directory}"'
    
    except PermissionError:
        return f'Error: Permission denied for file "{file_path}" in directory "{working_directory}"'
    
    except Exception as e:
        return f'Error: An unexpected error occurred while accessing file "{file_path}": {str(e)}'
    
    #check if target directory is within working directory
    try:
        if os.path.commonpath([working_abs_path, target_abs_path]) != working_abs_path:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        
    except Exception as e:
        return f'Error: An unexpected error occurred while checking file path "{file_path}": {str(e)}'
    
    except ValueError:
        return f'Error: Invalid file path "{file_path}"'
    
    except Exception as e:
        return f'Error: An unexpected error occurred while checking file path "{file_path}": {str(e)}'
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'