import os
MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    try:
        working_directory = os.path.abspath(working_directory)
        file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not os.path.isfile(file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        if not os.path.commonpath([working_directory, file_path]) == working_directory:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        with open(file_path, 'r') as file:
            content = file.read(MAX_CHARS)
            if len(content) == MAX_CHARS:
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content

    except Exception as e:
        return f'Error: {str(e)}'