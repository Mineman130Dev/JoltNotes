import customtkinter as CTk
import os
from appdirs import user_data_dir

window = CTk.CTk()
window.title("JoltNotes Lite v1.0")
window.attributes("-topmost", True)
window.resizable(False, False)

window.configure(fg_color='#3C3D37')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 400
window_height = 450

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

forget_label = CTk.CTkLabel(window, text="JoltNotes Lite", font=("Arial", 16, "bold"), text_color="white")
forget_label.place(relx=0.5, rely=0.025, anchor="center")

version_label = CTk.CTkLabel(window, text="MacOS - Intel", font=("Arial", 16, "bold"), text_color="white")
version_label.place(relx=0.5, rely=0.07, anchor="center")

textbox = CTk.CTkTextbox(window, width=390, height=400, wrap='word', fg_color='#171717')
textbox.place(rely=0.093, relx=0.013)

textbox.insert("0.0", "Hello")
text = textbox.get("0.0", "end")
textbox.delete("0.0", "end") 

app_name = "Jolt Notes Lite"
app_author = "Mineman130"
data_dir = user_data_dir(app_name, app_author)
os.makedirs(data_dir, exist_ok=True)
filepath = os.path.join(data_dir, "notes.txt")

def save_note():
    text_to_save = textbox.get("0.0", "end")
    try:
        with open(filepath, 'w') as file:
            file.write(text_to_save)
        print(f"Notes saved to: {filepath}")
    except Exception as e:
        print(f"Error saving note: {e}")

def load_note():
    try:
        with open(filepath, "r") as file:
            loaded_text = file.read()
            textbox.delete('0.0', 'end')
            textbox.insert('0.0', loaded_text)
        print(f'Note Loaded from: {filepath}')
    except FileNotFoundError:
        print('No Files Found.')
    except Exception as e:
        print(f'Error Loading Note: {e}')

save_button = CTk.CTkButton(window, text='Save', command=save_note, bg_color='#171717')
save_button.place(relx=0.6, rely=0.9)

load_button = CTk.CTkButton(window, text='Load', command=load_note, bg_color='#171717')
load_button.place(relx=0.05, rely=0.9)

load_note()

window.mainloop()