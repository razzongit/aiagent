import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "write or overrite files in a specified file path relative to the working directory, writing provided content to the file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file path to read files content from",
                },
                "content": {
                    "type": "string",
                    "description": "content which would be written in the file",
                },

            },
        "required": ["file_path", "content"]
        },
    },
}
def write_file(working_directory, file_path, content):
    try:
        wd = os.path.abspath(working_directory)
        ffp = os.path.join(wd, file_path)
        valid_path = os.path.commonpath([wd, ffp]) == wd
        if not valid_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(ffp):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(ffp), exist_ok=True)
        with open(ffp, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'
