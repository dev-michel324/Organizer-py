import os
import shutil

from enums.Move_type import Move_type

class Organizer:
    def __init__(self, dir: str, dir_to_save: str, move_type: Move_type, files_extensions: list) -> None:
        self._dir: str = dir
        self.dir_to_save: str = dir_to_save
        self.__move_type: Move_type = move_type
        self.__files_extensions: list = files_extensions
        self.files_type: dict = {
            ".mp3": "/audios",
            ".jpg": "/images",
            ".jpeg": "/images",
            ".m4a": "/audios",
            ".png": "/images",
            ".mp4": "/videos",
            ".ogg": "/audios",
            ".avi": "/videos"
        }
        self.__str_log: str = ""
        self.__create_folders()

    def __create_folders(self) -> None:
        if not os.path.exists(self.dir_to_save):
            os.makedirs(self.dir_to_save)
        for i in self.files_type.keys():
            path: str = f"{self.dir_to_save}{self.files_type[i]}"
            if not os.path.exists(path):
                os.makedirs(path)

    def main(self) -> str:
        for root, current_dir, files in os.walk(self._dir):
            for file in files:
                file_ext: str = self.get_file_extension(file)
                if file_ext in self.__files_extensions:
                    if file_ext in self.files_type.keys():
                        folder_to_save: str = self.files_type[file_ext]
                        path_to_save: str = f"{self.dir_to_save}{folder_to_save}/{file}"
                        original_path: str = f"{root}/{file}"
                        if self.__move_type == Move_type.MOVE:
                            os.replace(original_path, path_to_save)
                        elif self.__move_type == Move_type.COPY:
                            shutil.copy(original_path, path_to_save)
                        self.__str_log += f"DE: {original_path} PARA: {path_to_save}\n"
        return self.__str_log

    def get_file_extension(self, file: str):
        return os.path.splitext(file)[-1]