import os
import subprocess
from sys import stdout

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Execute python files with optional arguments in a specified file path relative to the working directory, execute python files using subprocess.run",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file path to read files content from",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "optional argument for running the python file",
                },
            },
        },
        "required": ["file_path"],
    },
}
def run_python_file(working_directory, file_path, args=None):
    try:
        wd = os.path.abspath(working_directory)
        ffp = os.path.normpath(os.path.join(wd, file_path))
        valid_path = os.path.commonpath([wd, ffp]) == wd
        if not valid_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(ffp):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", ffp]
        if args:
            command.extend(args)
        result = subprocess.run(
                command,  # Replace with your long-running command
                cwd=wd,
                capture_output=True,
                text=True,
                timeout=30
            )
        result_str = ''
        if result.returncode != 0:
            result_str += f'Process exited with code {result.returncode}'
        if not result.stdout and not result.stderr:
            result_str += 'No output produced'
        result_str += f'STDOUT: {result.stdout}, STDERR: {result.stderr}'
        return result_str
    except Exception as e:
        return f'Error: executing Python file: {e}'
