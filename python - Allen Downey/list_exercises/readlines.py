def read_file_content(filename):
    with open(filename) as file_object:
        lines = file_object.readlines()
    return lines