import PySimpleGUI as sg
from enums.Move_type import Move_type
import styles
from Utils import format_directory, to_raw_string, verify_if_directory_exists, organizer_main, get_files_extensions_from_checkbox

WINDOW_SIZE: tuple = (470, 425)
FILE_EXTENSIONS: list = [
    ".mp3", ".jpg", ".jpeg", ".m4a", ".png", ".mp4", ".ogg", ".avi"
]

frame_input_folders: list = [
    [sg.Text("Input path",
             background_color=styles.text_background, text_color=styles.text_default_color)],
    [sg.Input(key="browser0", tooltip="Folder path"), sg.FolderBrowse(
        button_text="Search folder", button_color="#4285F4")],
    [sg.Text("Output path",
             background_color=styles.text_background, text_color=styles.text_default_color)],
    [sg.Input(key="browser1", tooltip="Folder path"), sg.FolderBrowse(
        button_text="Search folder", button_color="#4285F4")],
]

radios: list = [
    [sg.Radio(text="Copy", key="rd_copy", group_id="rd_1", default=True, background_color=styles.window_background_color), sg.Radio(
        text="Move", key="rd_move", group_id="rd_1", default=False, background_color=styles.window_background_color)]
]

checkboxes: list = [
    [sg.Checkbox(text=".mp3", key=".mp3", background_color=styles.window_background_color, default=True),
     sg.Checkbox(text=".jpg", key=".jpg", background_color=styles.window_background_color, default=True)],
    [sg.Checkbox(text=".jpeg", key=".jpeg", background_color=styles.window_background_color, default=True),
     sg.Checkbox(text=".m4a", key=".m4a", background_color=styles.window_background_color, default=True)],
    [sg.Checkbox(text=".png", key=".png", background_color=styles.window_background_color, default=True),
     sg.Checkbox(text=".mp4", key=".mp4", background_color=styles.window_background_color, default=True)],
    [sg.Checkbox(text=".ogg", key=".ogg", background_color=styles.window_background_color, default=True),
     sg.Checkbox(text=".avi", key=".avi", background_color=styles.window_background_color, default=True)]
]

layout: list = [
    [sg.Frame(title="Folders path", font=styles.frame_font_default,
              layout=frame_input_folders, background_color=styles.window_background_color, size=(WINDOW_SIZE[0], 150))],
    [sg.Frame(title="Stock options", font=styles.frame_font_default, layout=[[sg.Column(layout=radios, element_justification="center", background_color=styles.window_background_color, justification="center")]],
              background_color=styles.window_background_color, size=(WINDOW_SIZE[0], 60))],
    [sg.Frame(title="File extensions",  font=styles.frame_font_default, layout=[[sg.Column(checkboxes, justification="center", element_justification="center",
                                                                                           background_color=styles.window_background_color)]], background_color=styles.window_background_color, size=(WINDOW_SIZE[0], 150))],
    [sg.Column([[sg.Button('Organizar', button_color="#1A73E8")]], justification="center",
               element_justification="center", background_color=styles.window_background_color)]
]

window = sg.Window(
    'OrdenMiler',
    layout=layout,
    resizable=False,
    background_color=styles.window_background_color,
    size=WINDOW_SIZE,
)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if event == "Organizar":
        dir_0: str = format_directory(to_raw_string(values['browser0']))
        dir_1: str = format_directory(to_raw_string(values['browser1']))
        if (not verify_if_directory_exists(dir_0) or not verify_if_directory_exists(dir_1)):
            sg.popup_ok(
                "O caminho especificado não existe",
                title="Erro",
                background_color=styles.popup_background_color,
                text_color=styles.text_default_color,
                button_color=styles.popup_button_color
            )
        else:
            move_type: Move_type = Move_type.MOVE if values['rd_move'] else Move_type.COPY
            files_extensions: list = get_files_extensions_from_checkbox(
                checkboxes=values, files_extensions=FILE_EXTENSIONS)

            log: str = organizer_main(
                dir=dir_0, dir_to_save=dir_1, move_type=move_type, files_extensions=files_extensions)

            if log:
                sg.PopupScrolled(
                    log,
                    title="log"
                )
            else:
                sg.popup_ok(
                    "Nenhum arquivo foi movido",
                    title="Warning",
                    background_color=styles.popup_background_color,
                    text_color=styles.text_default_color,
                    button_color=styles.popup_button_color
                )

window.close()
