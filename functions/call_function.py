import os

def call_function(function_call_part, verbose=False):
  try:
      if verbose:
          print(f"Calling function: {function_call_part.name}({function_call_part.args})")
      else:
          print(f" - Calling function: {function_call_part.name}")

      if function_call_part.name == "get_files_info":

  except Exception as e:
      return f"Error: {str(e)}"