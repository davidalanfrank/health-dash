import os



def get_file_type(filepath):
    if os.path.isfile(filepath):
        file_extension = os.path.splitext(filepath)[1]
        file_type = file_extension[1:].upper()
        return file_type
    else:
        return "Invalid file path"