import os
import subprocess

def run_python_file(working_directory, file_path):
    output = ""
     #check if directory is outside working directory
    working_abs_path = os.path.abspath(working_directory)
    target_abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    # check if file exists
    try:
        if not os.path.isfile(target_abs_path):
            print(f"is working")
            return f'File "{file_path}" not found'

    except PermissionError:
        return f'Error: Permission denied for file "{file_path}" in directory "{working_directory}"'
    
    except Exception as e:
        return f'Error: An unexpected error occurred while accessing file "{file_path}": {str(e)}'
    
    #check if target directory is within working directory
    try:
        if os.path.commonpath([working_abs_path, target_abs_path]) != working_abs_path:
            return f'Cannot execute "{file_path}" as it is outside'
    
    except ValueError:
        return f'Error: Invalid file path "{file_path}"'
    
    except Exception as e:
        return f'Error: An unexpected error occurred while checking file path "{file_path}": {str(e)}'
   
   #check if file is a Python file
    try: 
        if os.path.splitext(file_path)[1].lower() != ".py":
            return f'Error: "{file_path}" is not a Python file.'
    
    except Exception as e:
        f"Error: executing Python file: {e}"
        
    result = subprocess.run(
        ['python', target_abs_path],
        capture_output=True,
        text=True,
        cwd=working_directory
    )

    if result.stdout:
        output += f"STDOUT: {result.stdout}"

    if result.stderr:
        output += f"STDERR: {result.stderr}"

    if result.returncode != 0:
        output += f"\nProcess exited with code {result.returncode}"

    if result.stdout and result.stderr:
        return f"No output produced."
    
    return output
