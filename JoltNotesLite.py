import customtkinter as CTk
import os
from appdirs import user_data_dir

window = CTk.CTk()
window.title("JoltNotes Lite - macOS(Intel)")

def bring_to_front_non_topmost():
    window.attributes('-topmost', True)
    window.lift()
    window.attributes('-topmost', False)

window.resizable(False, False)

window.configure(fg_color='#3C3D37')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 400
window_height = 450

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

#toolbar = CTk.CTkFrame(window, height=25)
#toolbar.pack(fill="x", side="top")

textbox = CTk.CTkTextbox(window, wrap='word', fg_color='#171717')
textbox.pack(fill='both', expand=True)

textbox.insert("0.0", "Hello")
text = textbox.get("0.0", "end")
textbox.delete("0.0", "end") 

app_name = "JoltNotes Lite"
app_author = "Mineman130"
data_dir = user_data_dir(app_name, app_author)
os.makedirs(data_dir, exist_ok=True)
filepath = os.path.join(data_dir, "notes.txt")

save_timer = None
debounce_delay = 1000  # milliseconds

def save_note_debounced(event=None):
    global save_timer
    if save_timer:
        window.after_cancel(save_timer)
    save_timer = window.after(debounce_delay, save_note)

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

def open_settings(event):
    new_window = CTk.CTkToplevel()
    new_window.title("Settings")
    new_window.geometry("300x200")

setting_button = CTk.CTkButton(toolbar, text='settings', command=open_settings)
setting_button.pack()

#load_button = CTk.CTkButton(window, text='**Load**', command=load_note, bg_color='#171717')
#load_button.place(relx=0.05, rely=0.9)

textbox.bind("<KeyRelease>", save_note_debounced)

load_note()

window.after(100, bring_to_front_non_topmost)

window.mainloop()