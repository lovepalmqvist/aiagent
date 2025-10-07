import os
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):
  try:
      if verbose:
          print(f"Calling function: {function_call_part.name}({function_call_part.args})")
      else:
          print(f" - Calling function: {function_call_part.name}")

      available_functions = {
            "get_files_info": get_files_info,
            "get_file_content": get_file_content,
            "run_python_file": run_python_file,
            "write_file": write_file
        }

      if function_call_part.name not in available_functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

      # Extract arguments from the model output
      args = dict(function_call_part.args)

      # Inject working_directory manually
      args["working_directory"] = "./calculator"
      function_name = function_call_part.name
      function_result = available_functions[function_name](**args)

      return types.Content(
          role="tool",
          parts=[
              types.Part.from_function_response(
                  name=function_name,
                  response={"result": function_result},
              )
          ],
      )

  except Exception as e:
      return types.Content(
          role="tool",
          parts=[
              types.Part.from_function_response(
                  name=function_call_part.name,
                  response={"error": f"Error: executing Python function: {e}"},
              )
          ],
      )