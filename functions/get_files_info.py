import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"

            
def get_file_content(working_directory, file_path):
     #check if directory is outside working directory
    working_abs_path = os.path.abspath(working_directory)
    target_abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    #check is directory
    try:
        if not os.path.isfile(target_abs_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
    except Exception as e:
        return f'Error: An unexpected error occurred while accessing file "{file_path}": {str(e)}'
    
    #check if target directory is within working directory
    try:
        if os.path.commonpath([working_abs_path, target_abs_path]) != working_abs_path:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    except Exception as e:
        return f'Error: An unexpected error occurred while checking file path "{file_path}": {str(e)}'
    
    with open(target_abs_path, 'r') as file:
        content = file.read(10)
        rest = file.read(1)

        if rest:
            content += f'[...File "{file_path}" truncated at 10000 characters]'
        print(f"\ncontent: {content}")
    
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
        },required=["file_path"],
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