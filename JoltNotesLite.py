import customtkinter as CTk
import os
import json
from appdirs import user_data_dir
import tkinter.font as tkFont
import tkinter as tk
from customtkinter import CTkFont
import webbrowser

window = CTk.CTk()
window.title("JoltNotes Lite - macOS(Intel)")


def bring_to_front_non_topmost():
    window.attributes('-topmost', True)
    window.lift()
    window.attributes('-topmost', False)

window.resizable(False, False)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 400
window_height = 450
settings_frame_width = 400
settings_frame_height = 200

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

toolbar = CTk.CTkFrame(window, height=25)
toolbar.pack(fill="x", side="top")

textbox = CTk.CTkTextbox(window, wrap='word', fg_color='#171717')
textbox.pack(fill='both', expand=True)

textbox.insert("0.0", "Hello")
text = textbox.get("0.0", "end")
textbox.delete("0.0", "end") 
current_font = CTkFont(family="Helvetica", size=12)

app_name = "JoltNotes Lite"
app_author = "Mineman130"
data_dir = user_data_dir(app_name, app_author)
os.makedirs(data_dir, exist_ok=True)
filepath = os.path.join(data_dir, "notes.json")
settings_path = os.path.join(data_dir, "settings.json")  # New file for settings

save_timer = None
debounce_delay = 300  # milliseconds
show_settings = False

button_underlined_font = CTk.CTkFont(family="Helvetica", size=13, underline=True)

def save_note_debounced(event=None):
    global save_timer
    if save_timer:
        window.after_cancel(save_timer)
    save_timer = window.after(debounce_delay, save_note)

def save_note():
    """Save both text and formatting information to a JSON file"""
    try:
        # Access the underlying Tkinter text widget
        tk_text = textbox._textbox
        
        # Get the text content
        content = tk_text.get("0.0", "end")
        
        # Create a structure to store formatting
        formatted_data = {
            "content": content,
            "formatting": []
        }
        
        # Get all tag names
        all_tags = tk_text.tag_names()
        format_tags = [tag for tag in all_tags if tag.startswith("format_")]
        
        # For each format tag, store its range and properties
        for tag in format_tags:
            # Find the ranges this tag applies to
            tag_ranges = tk_text.tag_ranges(tag)
            
            # Convert ranges to string format
            ranges = []
            for i in range(0, len(tag_ranges), 2):
                start = str(tag_ranges[i])
                end = str(tag_ranges[i+1])
                ranges.append((start, end))
            
            # Determine the format type from the tag name
            format_type = None
            if tag.startswith("format_bold_"):
                format_type = "bold"
            elif tag.startswith("format_italic_"):
                format_type = "italic"
            elif tag.startswith("format_underline_"):
                format_type = "underline"
            elif tag.startswith("format_overstrike_"):
                format_type = "overstrike"
            elif tag.startswith("format_heading_"):
                format_type = "heading"
            elif tag.startswith("format_heading2_"):
                format_type = "heading2"
            elif tag.startswith("format_heading3_"):
                format_type = "heading3"
            
            # Store the format information
            if format_type and ranges:
                formatted_data["formatting"].append({
                    "type": format_type,
                    "ranges": ranges
                })
        
        # Save to JSON file
        with open(filepath, 'w') as file:
            json.dump(formatted_data, file, indent=2)
        
        print(f"Notes with formatting saved to: {filepath}")
    except Exception as e:
        print(f"Error saving note: {e}")

# Settings frame setup
settings_frame = CTk.CTkFrame(window)
settings_frame.pack_forget()
show_settings = False

theme_label = CTk.CTkLabel(settings_frame, text="Themes", text_color='white')
theme_label.pack()

# Default theme
DEFAULT_THEME = "JoltNotes"

# Theme change functions
def color_change_JoltNotes():
    toolbar.configure(fg_color='#262626')
    window.configure(fg_color='#171717')
    textbox.configure(fg_color='#171717', text_color='white')
    theme_label.configure(text_color='white')
    bold_button.configure(text_color='white')
    bold_button.configure(hover_color='#48b5ff')
    italic_button.configure(text_color='white')
    italic_button.configure(hover_color='#48b5ff')
    underline_button.configure(text_color='white')
    underline_button.configure(hover_color='#48b5ff')
    heading_button.configure(text_color='white')
    heading_button.configure(hover_color='#48b5ff')
    heading2_button.configure(text_color='white')
    heading2_button.configure(hover_color='#48b5ff')
    heading3_button.configure(text_color='white')
    heading3_button.configure(hover_color='#48b5ff')
    strickethrough_button.configure(text_color='white')
    strickethrough_button.configure(hover_color='#48b5ff')
    menu_button.configure(text_color='white')
    menu_button.configure(hover_color='#48b5ff')
    settings_menu_button.configure(text_color='white')
    settings_menu_button.configure(hover_color='#48b5ff')
    website_button.configure(text_color='white')
    save_theme("JoltNotes")

def color_change_dark():
    toolbar.configure(fg_color='#171717')
    window.configure(fg_color='#171717')
    textbox.configure(fg_color='#171717', text_color='white')
    theme_label.configure(text_color='white')
    bold_button.configure(text_color='white')
    bold_button.configure(hover_color='#48b5ff')
    italic_button.configure(text_color='white')
    italic_button.configure(hover_color='#48b5ff')
    underline_button.configure(text_color='white')
    underline_button.configure(hover_color='#48b5ff')
    heading_button.configure(text_color='white')
    heading_button.configure(hover_color='#48b5ff')
    heading2_button.configure(text_color='white')
    heading2_button.configure(hover_color='#48b5ff')
    heading3_button.configure(text_color='white')
    heading3_button.configure(hover_color='#48b5ff')
    strickethrough_button.configure(text_color='white')
    strickethrough_button.configure(hover_color='#48b5ff')
    menu_button.configure(text_color='white')
    menu_button.configure(hover_color='#48b5ff')
    settings_menu_button.configure(text_color='white')
    settings_menu_button.configure(hover_color='#48b5ff')
    website_button.configure(text_color='white')
    save_theme("dark")

def color_change_super_dark():
    toolbar.configure(fg_color='black')
    window.configure(fg_color='black')
    textbox.configure(fg_color='black', text_color='white')
    theme_label.configure(text_color='white')
    bold_button.configure(text_color='white')
    bold_button.configure(hover_color='#48b5ff')
    italic_button.configure(text_color='white')
    italic_button.configure(hover_color='#48b5ff')
    underline_button.configure(text_color='white')
    underline_button.configure(hover_color='#48b5ff')
    heading_button.configure(text_color='white')
    heading_button.configure(hover_color='#48b5ff')
    heading2_button.configure(text_color='white')
    heading2_button.configure(hover_color='#48b5ff')
    heading3_button.configure(text_color='white')
    heading3_button.configure(hover_color='#48b5ff')
    strickethrough_button.configure(text_color='white')
    strickethrough_button.configure(hover_color='#48b5ff')
    menu_button.configure(text_color='white')
    menu_button.configure(hover_color='#48b5ff')
    settings_menu_button.configure(text_color='white')
    settings_menu_button.configure(hover_color='#48b5ff')
    website_button.configure(text_color='white')
    save_theme("super_dark")

def color_change_white():
    toolbar.configure(fg_color='#F1F1F1')
    window.configure(fg_color='#F1F1F1')
    textbox.configure(fg_color='white', text_color='black')
    theme_label.configure(text_color='white')
    bold_button.configure(text_color='black')
    bold_button.configure(hover_color='#48b5ff')
    italic_button.configure(text_color='black')
    italic_button.configure(hover_color='#48b5ff')
    underline_button.configure(text_color='black')
    underline_button.configure(hover_color='#48b5ff')
    heading_button.configure(text_color='black')
    heading_button.configure(hover_color='#48b5ff')
    heading2_button.configure(text_color='black')
    heading2_button.configure(hover_color='#48b5ff')
    heading3_button.configure(text_color='black')
    heading3_button.configure(hover_color='#48b5ff')
    strickethrough_button.configure(text_color='black')
    strickethrough_button.configure(hover_color='#48b5ff')
    menu_button.configure(text_color='black')
    menu_button.configure(hover_color='#48b5ff')
    settings_menu_button.configure(text_color='black')
    settings_menu_button.configure(hover_color='#48b5ff')
    website_button.configure(text_color='white')
    save_theme("white")

def color_change_earth():
    toolbar.configure(fg_color='#a0aec0')
    window.configure(fg_color='#f5f5f5')
    textbox.configure(fg_color='#f5f5f5', text_color='#4a5568')
    theme_label.configure(text_color='white')
    bold_button.configure(text_color='#4a5568')
    bold_button.configure(hover_color='white')
    italic_button.configure(text_color='#4a5568')
    italic_button.configure(hover_color='white')
    underline_button.configure(text_color='#4a5568')
    underline_button.configure(hover_color='white')
    heading_button.configure(text_color='#4a5568')
    heading_button.configure(hover_color='white')
    heading2_button.configure(text_color='#4a5568')
    heading2_button.configure(hover_color='white')
    heading3_button.configure(text_color='#4a5568')
    heading3_button.configure(hover_color='white')
    strickethrough_button.configure(text_color='#4a5568')
    strickethrough_button.configure(hover_color='white')
    menu_button.configure(text_color='#4a5568')
    menu_button.configure(hover_color='white')
    settings_menu_button.configure(text_color='#4a5568')
    settings_menu_button.configure(hover_color='white')
    website_button.configure(text_color='white')
    save_theme("mutedearth")

def color_change_orange():
    toolbar.configure(fg_color='#282828')
    window.configure(fg_color='#282828')
    textbox.configure(fg_color='#282828', text_color='#FFB000')
    theme_label.configure(text_color='#FFB000')
    bold_button.configure(text_color='#FFB000')
    bold_button.configure(hover_color='#bd8200')
    italic_button.configure(text_color='#FFB000')
    italic_button.configure(hover_color='#bd8200')
    underline_button.configure(text_color='#FFB000')
    underline_button.configure(hover_color='#bd8200')
    heading_button.configure(text_color='#FFB000')
    heading_button.configure(hover_color='#bd8200')
    heading2_button.configure(text_color='#FFB000')
    heading2_button.configure(hover_color='#bd8200')
    heading3_button.configure(text_color='#FFB000')
    heading3_button.configure(hover_color='#bd8200')
    strickethrough_button.configure(text_color='#FFB000')
    strickethrough_button.configure(hover_color='#bd8200')
    menu_button.configure(text_color='#FFB000')
    menu_button.configure(hover_color='#bd8200')
    settings_menu_button.configure(text_color='#FFB000')
    settings_menu_button.configure(hover_color='#bd8200')
    website_button.configure(text_color='#FFB000')
    save_theme("orange")

def color_change_green():
    toolbar.configure(fg_color='#282828')
    window.configure(fg_color='#282828')
    textbox.configure(fg_color='#282828', text_color='#00FF66')
    theme_label.configure(text_color='#00FF66')
    bold_button.configure(text_color='#00FF66')
    bold_button.configure(hover_color='#00b849')
    italic_button.configure(text_color='#00FF66')
    italic_button.configure(hover_color='#00b849')
    underline_button.configure(text_color='#00FF66')
    underline_button.configure(hover_color='#00b849')
    heading_button.configure(text_color='#00FF66')
    heading_button.configure(hover_color='#00b849')
    heading2_button.configure(text_color='#00FF66')
    heading2_button.configure(hover_color='#00b849')
    heading3_button.configure(text_color='#00FF66')
    heading3_button.configure(hover_color='#00b849')
    strickethrough_button.configure(text_color='#00FF66')
    strickethrough_button.configure(hover_color='#00b849')
    menu_button.configure(text_color='#00FF66')
    menu_button.configure(hover_color='#00b849')
    settings_menu_button.configure(text_color='#00FF66')
    settings_menu_button.configure(hover_color='#00b849')
    website_button.configure(text_color='#00FF66')
    save_theme("green")

def color_change_pink():
    toolbar.configure(fg_color='#FFC1DA')
    window.configure(fg_color='#FFC1DA')
    textbox.configure(fg_color='#FFC1DA', text_color='black')
    theme_label.configure(text_color='white')
    bold_button.configure(text_color='black')
    bold_button.configure(hover_color='white')
    italic_button.configure(text_color='black')
    italic_button.configure(hover_color='white')
    underline_button.configure(text_color='black')
    underline_button.configure(hover_color='white')
    heading_button.configure(text_color='black')
    heading_button.configure(hover_color='white')
    heading2_button.configure(text_color='black')
    heading2_button.configure(hover_color='white')
    heading3_button.configure(text_color='black')
    heading3_button.configure(hover_color='white')
    strickethrough_button.configure(text_color='black')
    strickethrough_button.configure(hover_color='white')
    menu_button.configure(text_color='black')
    menu_button.configure(hover_color='white')
    settings_menu_button.configure(text_color='black')
    settings_menu_button.configure(hover_color='white')
    website_button.configure(text_color='white')
    save_theme("pink")

# Theme button
theme_buttons = [
    ("JoltNotes", color_change_JoltNotes, 'white'),
    ("Dark", color_change_dark, 'white'),
    ("Super Dark", color_change_super_dark, 'white'),
    ("Arctic White", color_change_white, 'white'),
    ("Mutted Earth", color_change_earth, 'white'),
    ("Terminal Amber", color_change_orange, 'white'),
    ("Terminal Green", color_change_green, 'white'),
    ("Pretty Pink", color_change_pink, 'white'),
]

for text, command, text_color in theme_buttons:
    button = CTk.CTkButton(
        settings_frame,
        text=text,
        command=command,
        fg_color='transparent',
        hover_color="#48b5ff",
        width=30,
        text_color=text_color
    )
    button.pack()

def load_note():
    """Load text and formatting from the JSON file"""
    try:
        # Check if the file exists
        if not os.path.exists(filepath):
            # If we're migrating from the old .txt format, try loading that
            old_filepath = os.path.join(data_dir, "notes.txt")
            if os.path.exists(old_filepath):
                with open(old_filepath, "r") as file:
                    loaded_text = file.read()
                    textbox.delete('0.0', 'end')
                    textbox.insert('0.0', loaded_text)
                print(f'Migrated from old note format: {old_filepath}')
            return
        
        # Load the JSON data
        with open(filepath, "r") as file:
            data = json.load(file)
        
        # Clear the current text and insert the content
        textbox.delete('0.0', 'end')
        textbox.insert('0.0', data.get("content", ""))
        
        # Access the underlying Tkinter text widget
        tk_text = textbox._textbox
        
        # Apply formatting
        for format_item in data.get("formatting", []):
            format_type = format_item.get("type")
            ranges = format_item.get("ranges", [])
            
            for start, end in ranges:
                # Create a unique tag name
                tag_name = f"format_{format_type}_{start.replace('.', '_')}_{end.replace('.', '_')}"
                
                # Configure the tag based on format type
                if format_type == "bold":
                    tk_text.tag_configure(tag_name, font=tkFont.Font(family="Helvetica", weight="bold"))
                elif format_type == "italic":
                    tk_text.tag_configure(tag_name, font=tkFont.Font(family="Helvetica", slant="italic"))
                elif format_type == "underline":
                    tk_text.tag_configure(tag_name, underline=True)
                elif format_type == "overstrike":
                    tk_text.tag_configure(tag_name, overstrike=True)
                elif format_type == "heading":
                    tk_text.tag_configure(tag_name, font=tkFont.Font(family="Helvetica", size=25, weight="bold"))
                elif format_type == "heading2":
                    tk_text.tag_configure(tag_name, font=tkFont.Font(family="Helvetica", size=20, weight="bold"))
                elif format_type == "heading3":
                    tk_text.tag_configure(tag_name, font=tkFont.Font(family="Helvetica", size=15, weight="bold"))
                
                # Apply the tag
                tk_text.tag_add(tag_name, start, end)
        
        print(f'Note loaded with formatting from: {filepath}')
    except json.JSONDecodeError:
        print("Error decoding JSON file. The file might be corrupted.")
    except Exception as e:
        print(f'Error loading note: {e}')

def apply_format_to_selection(format_type):
    """Apply formatting to selected text with toggle support and format switching"""
    try:
        # Access the underlying Tkinter text widget
        tk_text = textbox._textbox
        
        # Check if there's a selection
        try:
            start = tk_text.index("sel.first")
            end = tk_text.index("sel.last")
            selected_text = tk_text.get(start, end)
        except:
            print("No text selected")
            return
        
        # Get all existing tags at the selection start
        current_tags = tk_text.tag_names(start)
        
        # Format type prefixes for identification
        format_prefixes = {
            "bold": "format_bold_",
            "italic": "format_italic_",
            "underline": "format_underline_",
            "overstrike": "format_overstrike_",
            "heading": "format_heading_",
            "heading2": "format_heading2_",
            "heading3": "format_heading3_"
        }
        
        # Special handling for heading tags (they're mutually exclusive)
        if format_type in ["heading", "heading2", "heading3"]:
            # Remove any existing heading tags
            for tag in current_tags:
                if tag.startswith("format_heading_") or tag.startswith("format_heading2_") or tag.startswith("format_heading3_"):
                    tk_text.tag_remove(tag, start, end)
        
        # Check if the format is already applied
        format_already_applied = False
        for tag in current_tags:
            if tag.startswith(format_prefixes[format_type]):
                # Format is already applied, so remove it (toggle off)
                tk_text.tag_remove(tag, start, end)
                format_already_applied = True
        
        # If format wasn't already applied or removed, apply it now
        if not format_already_applied:
            # Create a unique tag name for this formatting
            tag_name = f"{format_prefixes[format_type]}{start.replace('.', '_')}_{end.replace('.', '_')}"
            
            # Configure the tag based on format type
            if format_type == "bold":
                    tk_text.tag_configure(tag_name, font=tkFont.Font(family="Helvetica", weight="bold"))
            elif format_type == "italic":
                    tk_text.tag_configure(tag_name, font=tkFont.Font(family="Helvetica", slant="italic"))
            elif format_type == "underline":
                    tk_text.tag_configure(tag_name, underline=True)
            elif format_type == "overstrike":
                    tk_text.tag_configure(tag_name, overstrike=True)
            elif format_type == "heading":
                    tk_text.tag_configure(tag_name, font=tkFont.Font(family="Helvetica", size=25, weight="bold"))
            elif format_type == "heading2":
                    tk_text.tag_configure(tag_name, font=tkFont.Font(family="Helvetica", size=20, weight="bold"))
            elif format_type == "heading3":
                    tk_text.tag_configure(tag_name, font=tkFont.Font(family="Helvetica", size=17, weight="bold"))
            
            # Apply the tag to the selected text
            tk_text.tag_add(tag_name, start, end)
        
    except Exception as e:
        print(f"Formatting error: {e}")

# Button command functions
def bold_text():
    apply_format_to_selection("bold")

def italicize_text():
    apply_format_to_selection("italic")

def underline_text():
    apply_format_to_selection("underline")

def strickethrough_text():
    apply_format_to_selection("overstrike")

def heading_text():
    apply_format_to_selection("heading")

def heading2_text():
    apply_format_to_selection("heading2")

def heading3_text():
    apply_format_to_selection("heading3")

def delete_line(event=None):
    try:
        current_position = textbox.index(tk.INSERT)
        current_line = current_position.split('.')[0]
        print(f"{current_position}")
        line_start = f"{current_line}.0"
        if textbox.compare(f"{current_line}.end", "<", "end"):
            line_end = f"{str(int(current_line)+1)}.0"
        else:
            line_end = f"{current_line}.end"
        textbox.delete(line_start, line_end)
        print("Line Deleted")
    except Exception as e:
        print(f"Error deleting line: {e}")

def toggle_settings():
    global show_settings
    show_settings = not show_settings
    if show_settings:
        textbox.pack_forget()
        settings_frame.pack(pady=20)
    else:
        settings_frame.pack_forget()
        textbox.pack(fill='both', expand=True)

def open_mini():
    global mini_window
    global mini_textbox
    mini_window = CTk.CTkToplevel(window)
    mini_window.title("Mini Jolt")
    mini_textbox = CTk.CTkTextbox(mini_window, wrap='word', fg_color='#171717')
    mini_textbox.pack(fill='both', expand=True)
    mini_window.geometry("200x200")
    mini_window.resizable(False, False)
    mini_window.attributes('-topmost', True)

def open_site():
    webbrowser.open("https://mineman130.dev/themes")

website_button = CTk.CTkButton(settings_frame, text='Themes Information', command=open_site, fg_color='transparent', hover_color="#48b5ff", width=30, font=button_underlined_font)
website_button.pack(side='top', padx=5)

strickethrough_button = CTk.CTkButton(toolbar, text='S', command=strickethrough_text, fg_color='transparent', hover_color="#48b5ff", width=30)
strickethrough_button.pack(side='right', padx=5)

heading3_button = CTk.CTkButton(toolbar, text='H3', command=heading3_text, fg_color='transparent', hover_color="#48b5ff", width=30)
heading3_button.pack(side='right', padx=5)

heading2_button = CTk.CTkButton(toolbar, text='H2', command=heading2_text, fg_color='transparent', hover_color="#48b5ff", width=30)
heading2_button.pack(side='right', padx=5)

heading_button = CTk.CTkButton(toolbar, text='H', command=heading_text, fg_color='transparent', hover_color="#48b5ff", width=30)
heading_button.pack(side='right', padx=5)
    
underline_button = CTk.CTkButton(toolbar, text='U', command=underline_text, fg_color='transparent', hover_color="#48b5ff", width=30)
underline_button.pack(side='right', padx=5)

italic_button = CTk.CTkButton(toolbar, text='I', command=italicize_text, fg_color='transparent', hover_color="#48b5ff", width=30)
italic_button.pack(side='right', padx=5)

bold_button = CTk.CTkButton(toolbar, text='B', command=bold_text, fg_color='transparent', hover_color="#48b5ff", width=30)
bold_button.pack(side='right', padx=5)

menu_button = CTk.CTkButton(toolbar, text='<', command=None, fg_color='transparent', hover_color="#48b5ff", width=30)
menu_button.pack(side='left', padx=5)

settings_menu_button = CTk.CTkButton(toolbar, text='⚙️', command=toggle_settings, fg_color='transparent', hover_color="#48b5ff", width=30)
settings_menu_button.pack(side='left', padx=5)

textbox.bind("<KeyRelease>", save_note_debounced)

textbox.bind('<Command-BackSpace>', delete_line)
textbox.bind('<Control-BackSpace>', delete_line)
window.bind('<Command-s>', lambda event: open_mini()) 

# Function to save the current theme
def save_theme(theme_name):
    try:
        with open(settings_path, "w") as f:
            json.dump({"theme": theme_name}, f)
    except Exception as e:
        print(f"Error saving theme: {e}")

# Function to load the saved theme
def load_theme():
    try:
        if os.path.exists(settings_path):
            with open(settings_path, "r") as f:
                data = json.load(f)
                return data.get("theme", DEFAULT_THEME)
        else:
            return DEFAULT_THEME 
    except Exception as e:
        print(f"Error loading theme: {e}")
        return DEFAULT_THEME

# Apply the theme when the app starts
def apply_saved_theme():
    saved_theme = load_theme()
    if saved_theme == "dark":
        color_change_dark()
    elif saved_theme == "super_dark":
        color_change_super_dark()
    elif saved_theme == "JoltNotes":
        color_change_JoltNotes()
    elif saved_theme == "white":
        color_change_white()
    elif saved_theme == "earth":
        color_change_earth()
    elif saved_theme == "orange":
        color_change_orange()
    elif saved_theme == "green":
        color_change_green()
    elif saved_theme == "pink":
        color_change_pink()
    else:
        color_change_JoltNotes() # set default.

# Call apply_saved_theme when the app starts
apply_saved_theme()

load_note()

window.after(100, bring_to_front_non_topmost)

window.mainloop()