from functions.get_files_info import get_files_info

print(f'Result for current directory: \n{get_files_info("calculator", ".")}',
f'Result for current directory: \n{get_files_info("calculator", "pkg")}',
f'Result for current directory: \n{get_files_info("calculator", "/bin")}',
f'Result for current directory: \n{get_files_info("calculator", "../")}'
)
