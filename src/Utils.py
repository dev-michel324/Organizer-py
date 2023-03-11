import os
from enums.Move_type import Move_type
from Organizer import Organizer

def organizer_main(dir: str, dir_to_save: str, move_type: Move_type, files_extensions: list) -> str:
    organizer: Organizer = Organizer(dir=dir, dir_to_save=dir_to_save, move_type=move_type, files_extensions=files_extensions)
    log: str = organizer.main()
    return log

def get_files_extensions_from_checkbox(checkboxes: dict, files_extensions: list) -> list:
    selected_checkboxes: list = []
    for file_extension in files_extensions:
        if file_extension in checkboxes.keys():
            if checkboxes[file_extension]:
                selected_checkboxes.append(file_extension)
    return selected_checkboxes

def to_raw_string(string: str) -> str:
    return fr"{string}"

def format_directory(directory: str) -> str :
    return directory.replace("\\", "/")

def verify_if_directory_exists(directory: str) -> bool:
    return os.path.exists(directory)