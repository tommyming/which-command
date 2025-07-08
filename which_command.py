import os

command_input = input()

request_libraries = command_input.split(sep=" ")
# the first string(which) is not needed.
del request_libraries[0]

path_variable = os.environ.get('PATH')
path_directories = path_variable.split(os.pathsep)

result = ""

for library in request_libraries:
    for directory in path_directories:
        library_path = os.path.join(directory, library)
        if os.path.exists(library_path):
            if (not os.path.isfile(library_path)) or (not os.path.isdir(library_path)) or (not os.access(library_path, os.X_OK)):
                result += library_path
                result += "\n"
    if not result:
        result += f"{library} not found."

print(result)