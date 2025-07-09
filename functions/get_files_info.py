import os
from google.genai import types

def get_files_info(working_directory, directory=None):

    print(f"\ndirectory: {directory}| working_directory: {working_directory}")

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
            return f'Error: File not found or is not a regular file: "{file_path}"'

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
                file.write(content)

    except FileNotFoundError:
        return f'Error: File "{file_path}" does not exist in directory "{working_directory}"'
    
    except PermissionError:
        return f'Error: Permission denied for file "{file_path}" in directory "{working_directory}"'
    
    except Exception as e:
        return f'Error: An unexpected error occurred while accessing file "{file_path}": {str(e)}'
    


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="reads the content of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="relative path for the file to read",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="runs the python file and returns the output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="relative path for to the python file to run",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="content to write into the file",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file with the provided content, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="relative path for the file to write",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",)
        },
    ),
)

available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )