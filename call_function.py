from google.genai import types
from functions.get_files_info import *
from functions.run_python import run_python_file

MAX_iters = 5
# calling the function
def call_function(function_calls, verbose=False):
    print(f"\n call_function called\n")

    #check to see if user is runing a verbose mode
    if verbose:
        print(f"\nCalling function name = {function_calls.name} args = ({function_calls.args})")
    else:
        print(f"\n -> Calling function name:  = {function_calls.name}")
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }
    function_name = function_calls.name
    # function not found
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    args = dict(function_calls.args)
    args["working_directory"] = "./calculator"
    function_result= function_map[function_name](**args)

    # Create the type content to return
    type_content = types.Content(
        role = "tool",
        parts=[
            types.Part.from_function_response(
                name = function_name,
                response = {"result": function_result},
            )
        ],
    )
    return type_content