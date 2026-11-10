import os


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
def get_files_info(working_directory, directory="."):
    try:
        wd = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(wd, directory))
        valid_target_dir = os.path.commonpath([wd, target_dir]) == wd
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'"{directory}" is not a directory'
        if valid_target_dir:
            # return f'Success: "{directory}" is within the working directory'
            dir_content = os.listdir(target_dir)
            item_list = []
            for c in dir_content:
                try:
                    name = c
                    c_full_path = os.path.join(target_dir, name)
                    size = os.path.getsize(c_full_path)
                    is_dir = os.path.isdir(c_full_path)
                except Exception as e:
                    return f'Error: {e}'

                item_list.append(f'- {name}: file_size={size} bytes, is_dir={is_dir}')
            return "\n".join(item_list)
    except Exception as e:
        return f'Error: {e}'
