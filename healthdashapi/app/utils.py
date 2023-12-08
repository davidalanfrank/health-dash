import os

def get_file_type(filepath):
    if os.path.isfile(filepath):
        file_extension = os.path.splitext(filepath)[1]
        file_type = file_extension[1:].upper()
        return file_type
    else:
        return "Invalid file path"
    
def set_working_dir():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    current_file_path = os.chdir(current_directory)
    print("current_directory")
    print(current_file_path)