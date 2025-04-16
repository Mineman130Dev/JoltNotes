import customtkinter as CTk
import os

window = CTk.CTk()
window.title("JoltNotes: Lite")
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

textbox = CTk.CTkTextbox(window, width=390, height=400, wrap='word')
textbox.pack()

textbox.insert("0.0", "Hello")
text = textbox.get("0.0", "end")
textbox.delete("0.0", "end") 

def save_note():
    filepath = 'notes.txt'
    text_to_save = textbox.get("0.0", "end")
    try:
        with open(filepath, 'w') as file:
            file.write(text_to_save)
        print("Notes saved!")
    except Exception as e:
        print(f"Error saving note: {e}")

def load_note():
    filepath = 'notes.txt'
    try:
        with open(filepath, "r") as file:
            loaded_text = file.read()
            textbox.delete('0.0', 'end')
            textbox.insert('0.0', loaded_text)
        print('Note Loaded!')
    except FileNotFoundError:
        print('No Files Found.')
    except Exception as e:
        print(f'Error Loading Note: {e}')

def enter_event():
    print('pressed')

save_button = CTk.CTkButton(window, text='Save', command=save_note)
save_button.place(relx=0.6, rely=0.9)

load_button = CTk.CTkButton(window, text='Load', command=load_note)
load_button.place(relx=0.05, rely=0.9)

load_note()

window.mainloop()