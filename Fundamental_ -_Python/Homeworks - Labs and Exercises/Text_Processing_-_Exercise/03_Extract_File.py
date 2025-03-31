path_of_file = input().split("\\")
file_name = path_of_file[-1].split(".")
print(f"File name: {file_name[0]}")
print(f"File extension: {file_name[-1]}")
