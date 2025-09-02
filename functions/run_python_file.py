import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not os.path.commonpath([working_directory, abs_file_path]) == working_directory:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(abs_file_path):
            return f'Error: File "{os.path.basename(file_path)}" not found.'

        if not abs_file_path.endswith('.py'):
            return f'Error: "{os.path.basename(file_path)}" is not a Python file.'

        result = subprocess.run(['python', abs_file_path] + args, capture_output=True, text=True, cwd=working_directory, timeout=30)

        output_parts = []
        if result.stdout.strip():
            output_parts.append(f"STDOUT:\n{result.stdout.strip()}")
        if result.stderr.strip():
            output_parts.append(f"STDERR:\n{result.stderr.strip()}")
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        if not output_parts:
            return "No output produced."

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"