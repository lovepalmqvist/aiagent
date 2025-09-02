import os

def get_files_info(working_directory, directory="."):
    try:
        working_directory = os.path.abspath(working_directory)
        directory = os.path.abspath(os.path.join(working_directory, directory))

        if not os.path.isdir(directory):
            return (f'Error: "{directory}" is not a directory')

        if not os.path.commonpath([working_directory, directory]) == working_directory:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

        lines = []
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)
            lines.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(lines)

    except Exception as e:
        return (f'Error: {str(e)}')
