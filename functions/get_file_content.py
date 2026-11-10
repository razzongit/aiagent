import os

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Read file's content in a specified directory relative to the working directory, providing max 10000 characters of the file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file path to read files content from",
                },

            },
        "required": ["file_path"]
        },
    },
}
def get_file_content(working_directory, file_path):
    try:
        wd = os.path.abspath(working_directory)
        ffp = os.path.join(wd, file_path)
        valid_path = os.path.commonpath([wd, ffp]) == wd
        if not valid_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(ffp):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        MAX_CHARS = 10000

        with open(ffp, "r") as f:
            contents = f.read(MAX_CHARS)

            if f.read(1):
                contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return contents
    except Exception as e:
        return f'Error: {e}'
