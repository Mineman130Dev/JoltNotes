import customtkinter as CTk
import os
import json
from appdirs import user_data_dir
import tkinter.font as tkFont
import tkinter as tk
from customtkinter import CTkFont
import webbrowser

window = CTk.CTk()
window.title("JoltNotes v0.3.0-alpha.0")

mini_window = None
mini_textbox = None

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

app_name = "JoltNotes"
app_author = "Mineman130"
data_dir = user_data_dir(app_name, app_author)
os.makedirs(data_dir, exist_ok=True)
filepath = os.path.join(data_dir, "notes.json")
settings_path = os.path.join(data_dir, "settings.json")

save_timer = None
debounce_delay = 300  # milliseconds
show_settings = False
show_menu = False

button_underlined_font = CTk.CTkFont(family="Helvetica", size=13, underline=True)

def save_note_debounced(event=None):
    global save_timer
    if save_timer:
        window.after_cancel(save_timer)
    save_timer = window.after(debounce_delay, save_note)

def save_note():
    """Save both text and formatting information to a JSON file"""
    try:
        tk_text = textbox._textbox
        
        content = tk_text.get("0.0", "end")
        
        formatted_data = {
            "content": content,
            "formatting": []
        }
        
        all_tags = tk_text.tag_names()
        format_tags = [tag for tag in all_tags if tag.startswith("format_")]
        
        for tag in format_tags:
            tag_ranges = tk_text.tag_ranges(tag)
            
            ranges = []
            for i in range(0, len(tag_ranges), 2):
                start = str(tag_ranges[i])
                end = str(tag_ranges[i+1])
                ranges.append((start, end))
            
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
            
            if format_type and ranges:
                formatted_data["formatting"].append({
                    "type": format_type,
                    "ranges": ranges
                })
        
        with open(filepath, 'w') as file:
            json.dump(formatted_data, file, indent=2)
        
        print(f"Notes with formatting saved to: {filepath}")
    except Exception as e:
        print(f"Error saving note: {e}")

settings_frame = CTk.CTkFrame(window)
settings_frame.pack_forget()
show_settings = False
show_menu = False

theme_label = CTk.CTkLabel(settings_frame, text="Themes", text_color='white')
theme_label.pack()

DEFAULT_THEME = "JoltNotes"

def color_change_JoltNotes():
    print("Applying JoltNotes theme...")
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
    strickethrough_button.configure(text_color='white')
    strickethrough_button.configure(hover_color='#48b5ff')
    menu_button.configure(text_color='white')
    menu_button.configure(hover_color='#48b5ff')
    settings_menu_button.configure(text_color='white')
    settings_menu_button.configure(hover_color='#48b5ff')
    website_button.configure(text_color='white')
    settings_frame.configure(fg_color='#171717')
    notes_list_main_frame.configure(fg_color='#171717')
    if mini_window != None:
        mini_window.configure(fg_color='#171717')
    if mini_textbox != None:
        mini_textbox.configure(text_color='white')
        mini_textbox.configure(fg_color='#171717')
    save_theme("JoltNotes")

def color_change_silicon():
    print("Applying Apple Silicon theme...")
    toolbar.configure(fg_color='#1a1a1a') 
    window.configure(fg_color='#0d0d0d') 
    textbox.configure(fg_color='#0d0d0d', text_color="#FFFFFF")
    settings_frame.configure(fg_color='#0d0d0d')
    notes_list_main_frame.configure(fg_color='#0d0d0d')

    theme_label.configure(text_color="#FF78FF")
    
    bold_button.configure(text_color='#FF78FF', hover_color="#8C4BC9")
    italic_button.configure(text_color="#FF78FF", hover_color='#8C4BC9')
    underline_button.configure(text_color='#FF78FF', hover_color="#8C4BC9")
    heading_button.configure(text_color='#FF78FF', hover_color='#8C4BC9')
    heading2_button.configure(text_color='#FF78FF', hover_color='#8C4BC9')
    strickethrough_button.configure(text_color='#FF78FF', hover_color='#8C4BC9')

    menu_button.configure(text_color='#FF78FF', hover_color='#8C4BC9') # Magenta text, darker purple hover
    settings_menu_button.configure(text_color='#FF78FF', hover_color='#8C4BC9')
    
    website_button.configure(text_color='#FF78FF', hover_color='#8C4BC9')

    if mini_window != None:
        mini_window.configure(fg_color='#0d0d0d')
    if mini_textbox != None:
        mini_textbox.configure(text_color='#FFFFFF')
        mini_textbox.configure(fg_color='#0d0d0d')
        
    save_theme("silicon")

def color_change_dark():
    print("Applying Dark theme...")
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
    strickethrough_button.configure(text_color='white')
    strickethrough_button.configure(hover_color='#48b5ff')
    menu_button.configure(text_color='white')
    menu_button.configure(hover_color='#48b5ff')
    settings_menu_button.configure(text_color='white')
    settings_menu_button.configure(hover_color='#48b5ff')
    website_button.configure(text_color='white')
    settings_frame.configure(fg_color='black')
    notes_list_main_frame.configure(fg_color='black')
    if mini_window != None:
        mini_window.configure(fg_color='black')
    if mini_textbox != None:
        mini_textbox.configure(text_color='white')
        mini_textbox.configure(fg_color='black')
    save_theme("dark")

def color_change_light():
    print("Applying Light theme...")
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
    strickethrough_button.configure(text_color='black')
    strickethrough_button.configure(hover_color='#48b5ff')
    menu_button.configure(text_color='black')
    menu_button.configure(hover_color='#48b5ff')
    settings_menu_button.configure(text_color='black')
    settings_menu_button.configure(hover_color='#48b5ff')
    website_button.configure(text_color='white')
    settings_frame.configure(fg_color='#e3e3e3')
    notes_list_main_frame.configure(fg_color='#e3e3e3')
    if mini_window != None:
        mini_window.configure(fg_color='#F1F1F1')
    if mini_textbox != None:
        mini_textbox.configure(text_color='black')
        mini_textbox.configure(fg_color='#F1F1F1')
    save_theme("light")

def color_change_earth():
    print("Applying Earth theme...")
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
    strickethrough_button.configure(text_color='#4a5568')
    strickethrough_button.configure(hover_color='white')
    menu_button.configure(text_color='#4a5568')
    menu_button.configure(hover_color='white')
    settings_menu_button.configure(text_color='#4a5568')
    settings_menu_button.configure(hover_color='white')
    website_button.configure(text_color='white')
    settings_frame.configure(fg_color='#f5f5f5')
    notes_list_main_frame.configure(fg_color='#f5f5f5')
    if mini_window != None:
        mini_window.configure(fg_color='#f5f5f5')
    if mini_textbox != None:
        mini_textbox.configure(text_color='#4a5568`1')
        mini_textbox.configure(fg_color='#f5f5f5')
    save_theme("mutedearth")

def color_change_orange():
    print("Applying Amber theme...")
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
    strickethrough_button.configure(text_color='#FFB000')
    strickethrough_button.configure(hover_color='#bd8200')
    menu_button.configure(text_color='#FFB000')
    menu_button.configure(hover_color='#bd8200')
    settings_menu_button.configure(text_color='#FFB000')
    settings_menu_button.configure(hover_color='#bd8200')
    website_button.configure(text_color='#FFB000')
    settings_frame.configure(fg_color='#282828')
    notes_list_main_frame.configure(fg_color='#282828')
    if mini_window != None:
        mini_window.configure(fg_color='#282828')
    if mini_textbox != None:
        mini_textbox.configure(text_color='#FFB000')
        mini_textbox.configure(fg_color='#282828')
    save_theme("orange")

def color_change_green():
    print("Applying Terminal Green theme...")
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
    strickethrough_button.configure(text_color='#00FF66')
    strickethrough_button.configure(hover_color='#00b849')
    menu_button.configure(text_color='#00FF66')
    menu_button.configure(hover_color='#00b849')
    settings_menu_button.configure(text_color='#00FF66')
    settings_menu_button.configure(hover_color='#00b849')
    website_button.configure(text_color='#00FF66')
    settings_frame.configure(fg_color='#282828')
    notes_list_main_frame.configure(fg_color='#282828')
    if mini_window != None:
        mini_window.configure(fg_color='#282828')
    if mini_textbox != None:
        mini_textbox.configure(text_color='#00FF66')
        mini_textbox.configure(fg_color='#282828')
    save_theme("green")

def color_change_pink():
    print("Applying Pretty Pink theme...")
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
    strickethrough_button.configure(text_color='black')
    strickethrough_button.configure(hover_color='white')
    menu_button.configure(text_color='black')
    menu_button.configure(hover_color='white')
    settings_menu_button.configure(text_color='black')
    settings_menu_button.configure(hover_color='white')
    website_button.configure(text_color='white')
    settings_frame.configure(fg_color='#FFC1DA')
    notes_list_main_frame.configure(fg_color='#FFC1DA')
    if mini_window != None:
        mini_window.configure(fg_color='#FFC1DA')
    if mini_textbox != None:
        mini_textbox.configure(text_color='white')
        mini_textbox.configure(fg_color='#FFC1DA')
    save_theme("pink")

def color_change_earthy():
    print("Applying Earthy theme...")
    toolbar.configure(fg_color='#AEC8A4')
    window.configure(fg_color='#c5e3ba')
    textbox.configure(fg_color='#c5e3ba', text_color='#8A784E')
    theme_label.configure(text_color='#8A784E')
    bold_button.configure(text_color='#8A784E')
    bold_button.configure(hover_color='#c5e3ba')
    italic_button.configure(text_color='#8A784E')
    italic_button.configure(hover_color='#c5e3ba')
    underline_button.configure(text_color='#8A784E')
    underline_button.configure(hover_color='#c5e3ba')
    heading_button.configure(text_color='#8A784E')
    heading_button.configure(hover_color='#c5e3ba')
    heading2_button.configure(text_color='#8A784E')
    heading2_button.configure(hover_color='#c5e3ba')
    strickethrough_button.configure(text_color='#8A784E')
    strickethrough_button.configure(hover_color='#c5e3ba')
    menu_button.configure(text_color='#8A784E')
    menu_button.configure(hover_color='#c5e3ba')
    settings_menu_button.configure(text_color='#8A784E')
    settings_menu_button.configure(hover_color='#c5e3ba')
    website_button.configure(text_color='#8A784E')
    website_button.configure(hover_color='#c5e3ba')
    settings_frame.configure(fg_color='#c5e3ba')
    notes_list_main_frame.configure(fg_color='#c5e3ba')
    if mini_window != None:
        mini_window.configure(fg_color='#E7EFC7')
    if mini_textbox != None:
        mini_textbox.configure(text_color='#8A784E')
        mini_textbox.configure(fg_color='#E7EFC7')
    save_theme("earthy")

def color_change_velvet():
    print("Applying Red Velvet theme...")
    toolbar.configure(fg_color='#4A102A')
    window.configure(fg_color='#85193C')
    textbox.configure(fg_color='#85193C', text_color='white')
    theme_label.configure(text_color='white')
    bold_button.configure(text_color='white')
    bold_button.configure(hover_color='#85193C')
    italic_button.configure(text_color='white')
    italic_button.configure(hover_color='#85193C')
    underline_button.configure(text_color='white')
    underline_button.configure(hover_color='#85193C')
    heading_button.configure(text_color='white')
    heading_button.configure(hover_color='#85193C')
    heading2_button.configure(text_color='white')
    heading2_button.configure(hover_color='#85193C')
    strickethrough_button.configure(text_color='white')
    strickethrough_button.configure(hover_color='#85193C')
    menu_button.configure(text_color='white')
    menu_button.configure(hover_color='#85193C')
    settings_menu_button.configure(text_color='white')
    settings_menu_button.configure(hover_color='#85193C')
    website_button.configure(text_color='white')
    website_button.configure(hover_color='#85193C')
    settings_frame.configure(fg_color='#85193C')
    notes_list_main_frame.configure(fg_color='#85193C')
    if mini_window != None:
        mini_window.configure(fg_color='#85193C')
    if mini_textbox != None:
        mini_textbox.configure(text_color='white')
        mini_textbox.configure(fg_color='#85193C')
    save_theme("velvet")

def color_change_menlon():
    print("Applying Watermenlon theme...")
    toolbar.configure(fg_color='#4edb1f')
    window.configure(fg_color='#FFAAAA')
    textbox.configure(fg_color='#FFAAAA', text_color='black')
    theme_label.configure(text_color='#399918')
    bold_button.configure(text_color='#399918')
    bold_button.configure(hover_color='#ECFFE6')
    italic_button.configure(text_color='#399918')
    italic_button.configure(hover_color='#ECFFE6')
    underline_button.configure(text_color='#399918')
    underline_button.configure(hover_color='#ECFFE6')
    heading_button.configure(text_color='#399918')
    heading_button.configure(hover_color='#ECFFE6')
    heading2_button.configure(text_color='#399918')
    heading2_button.configure(hover_color='#ECFFE6')
    strickethrough_button.configure(text_color='#399918')
    strickethrough_button.configure(hover_color='#ECFFE6')
    menu_button.configure(text_color='#399918')
    menu_button.configure(hover_color='#ECFFE6')
    settings_menu_button.configure(text_color='#399918')
    settings_menu_button.configure(hover_color='#ECFFE6')
    website_button.configure(text_color='#399918')
    website_button.configure(hover_color='#ECFFE6')
    settings_frame.configure(fg_color='#FFAAAA')
    notes_list_main_frame.configure(fg_color='#FFAAAA')
    if mini_window != None:
        mini_window.configure(fg_color='#FFAAAA')
    if mini_textbox != None:
        mini_textbox.configure(text_color='black')
        mini_textbox.configure(fg_color='#FFAAAA')
    save_theme("menlon")

# Theme button
theme_buttons = [
    ("JoltNotes", color_change_JoltNotes, 'white'),
    ("Silicon Chip", color_change_silicon, 'white'),
    ("Dark Mode", color_change_dark, 'white'),
    ("Light Mode", color_change_light, 'white'),
    ("Mutted Earth", color_change_earth, 'white'),
    ("Terminal Amber", color_change_orange, 'white'),
    ("Terminal Green", color_change_green, 'white'),
    ("Pretty Pink", color_change_pink, 'white'),
    ("Earthy Green", color_change_earthy, 'white'),
    ("Red Velvet", color_change_velvet, 'white'),
    ("Watermelon Vibes", color_change_menlon, 'white'),
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

base_font_family = "Helvetica"
base_font_size = 12

FONT_NORMAL = tkFont.Font(family=base_font_family, size=base_font_size)
FONT_BOLD = tkFont.Font(family=base_font_family, size=base_font_size, weight="bold")
FONT_ITALIC = tkFont.Font(family=base_font_family, size=base_font_size, slant="italic")
FONT_BOLD_ITALIC = tkFont.Font(family=base_font_family, size=base_font_size, weight="bold", slant="italic")
FONT_HEADING = tkFont.Font(family=base_font_family, size=25, weight="bold")
FONT_HEADING2 = tkFont.Font(family=base_font_family, size=20, weight="bold")
FONT_HEADING3 = tkFont.Font(family=base_font_family, size=17, weight="bold")

# --- Modified load_note function ---
def load_note():
    try:
        if not os.path.exists(filepath):
            # ... (your existing migration logic)
            old_filepath = os.path.join(data_dir, "notes.txt")
            if os.path.exists(old_filepath):
                with open(old_filepath, "r") as file:
                    loaded_text = file.read()
                    textbox.delete('0.0', 'end')
                    textbox.insert('0.0', loaded_text)
                print(f'Migrated from old note format: {old_filepath}')
            return

        with open(filepath, "r") as file:
            data = json.load(file)

        textbox.delete('0.0', 'end')
        textbox.insert('0.0', data.get("content", ""))

        tk_text = textbox._textbox

        # Clear all existing tags before applying new ones to prevent conflicts from previous loads
        for tag in tk_text.tag_names():
            if tag.startswith("format_"): # Assuming all your custom format tags start with "format_"
                tk_text.tag_remove(tag, "1.0", "end")

        for format_item in data.get("formatting", []):
            format_type = format_item.get("type")
            ranges = format_item.get("ranges", [])

            for start, end in ranges:
                tag_name = f"format_{format_type}_{start.replace('.', '_')}_{end.replace('.', '_')}"

                # Configure the tag with specific font objects or attributes
                # Ensure the tag doesn't already exist before configuring
                if tag_name not in tk_text.tag_names():
                    if format_type == "bold":
                        tk_text.tag_configure(tag_name, font=FONT_BOLD)
                    elif format_type == "italic":
                        tk_text.tag_configure(tag_name, font=FONT_ITALIC)
                    elif format_type == "underline":
                        tk_text.tag_configure(tag_name, underline=True) # Underline is a simple boolean attribute
                    elif format_type == "overstrike":
                        tk_text.tag_configure(tag_name, overstrike=True) # Overstrike is a simple boolean attribute
                    elif format_type == "heading":
                        tk_text.tag_configure(tag_name, font=FONT_HEADING)
                    elif format_type == "heading2":
                        tk_text.tag_configure(tag_name, font=FONT_HEADING2)
                    elif format_type == "heading3":
                        tk_text.tag_configure(tag_name, font=FONT_HEADING3)

                # Apply the tag
                tk_text.tag_add(tag_name, start, end)

        print(f'Note loaded with formatting from: {filepath}')
    except json.JSONDecodeError:
        print("Error decoding JSON file. The file might be corrupted.")
    except Exception as e:
        print(f'Error loading note: {e}')

def apply_format_to_selection(format_type):
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

current_view = "textbox" # "textbox", "settings", "notes_list"

def set_current_view(view_name):
    global current_view
    
    # Hide all possible content frames first
    textbox.pack_forget()
    settings_frame.pack_forget()
    notes_list_main_frame.pack_forget() # The new notes list frame

    # Pack the requested view
    if view_name == "textbox":
        textbox.pack(fill='both', expand=True)
    elif view_name == "settings":
        settings_frame.pack(fill='both', expand=True, pady=20) # Use fill/expand for settings frame
    elif view_name == "notes_list":
        populate_notes_list_frame() # Re-populate the list each time it's shown
        notes_list_main_frame.pack(fill='both', expand=True, pady=20) # Use fill/expand for notes list frame
    
    current_view = view_name
    print(f"Current view set to: {current_view}")

def toggle_settings():
    if current_view == "settings":
        set_current_view("textbox")
    else:
        set_current_view("settings")

def toggle_notes_list():
    if current_view == "notes_list":
        set_current_view("textbox")
    else:
        set_current_view("notes_list")

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

menu_button = CTk.CTkButton(toolbar, text='Menu', command=toggle_notes_list, fg_color='transparent', hover_color="#48b5ff", width=30)
menu_button.pack(side='left', padx=5)

settings_menu_button = CTk.CTkButton(toolbar, text='⚙️', command=toggle_settings, fg_color='transparent', hover_color="#48b5ff", width=30)
settings_menu_button.pack(side='left', padx=5)

textbox.bind("<KeyRelease>", save_note_debounced)

textbox.bind('<Command-BackSpace>', delete_line)
textbox.bind('<Control-BackSpace>', delete_line)
window.bind('<Command-s>', lambda event: open_mini()) 
window.bind('<Control-s>', lambda event: open_mini())

notes_list_main_frame = CTk.CTkScrollableFrame(window)

# --- Populate Notes List Frame (NEW) ---
def populate_notes_list_frame():
    for widget in notes_list_main_frame.winfo_children():
        widget.destroy()

    CTk.CTkLabel(notes_list_main_frame, text="Your Notes", font=("Helvetica", 20, "bold")).pack(pady=(10, 15))

    note_files = [f for f in os.listdir(data_dir) if f.endswith('.json')]
    
    if not note_files:
        CTk.CTkLabel(notes_list_main_frame, text="No notes found.", text_color="gray").pack(pady=5)
    else:
        note_files_sorted = sorted(note_files, key=lambda f: os.path.getmtime(os.path.join(data_dir, f)), reverse=True)

        for note_file in note_files_sorted:
            note_name = note_file.replace(".json", "")
            btn = CTk.CTkButton(notes_list_main_frame, text=note_name, 
                                command=lambda nf=note_file: load_note_and_return_to_textbox(os.path.join(data_dir, nf)),
                                fg_color='transparent', hover_color="#48b5ff",
                                anchor="w")
            btn.pack(fill="x", pady=2, padx=10)

def load_note_and_return_to_textbox(file_path):
    load_note(file_path)
    set_current_view("textbox")

textbox.bind("<KeyRelease>", save_note_debounced)

textbox.bind('<Command-BackSpace>', delete_line)
textbox.bind('<Control-BackSpace>', delete_line)
window.bind('<Command-s>', lambda event: open_mini())
window.bind('<Control-s>', lambda event: open_mini())

def save_theme(theme_name):
    try:
        with open(settings_path, "w") as f:
            json.dump({"theme": theme_name}, f)
    except Exception as e:
        print(f"Error saving theme: {e}")

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

def apply_saved_theme():
    saved_theme = load_theme()
    if saved_theme == "dark":
        color_change_dark()
    elif saved_theme == "JoltNotes":
        color_change_JoltNotes()
    elif saved_theme == "silicon":
        color_change_silicon()
    elif saved_theme == "white":
        color_change_light()
    elif saved_theme == "earth":
        color_change_earth()
    elif saved_theme == "orange":
        color_change_orange()
    elif saved_theme == "green":
        color_change_green()
    elif saved_theme == "pink":
        color_change_pink()
    elif saved_theme == "earthy":
        color_change_earthy()
    elif saved_theme == "velvet":
        color_change_velvet()
    elif saved_theme == "menlon":
        color_change_menlon()
    else:
        color_change_JoltNotes()

apply_saved_theme()

load_note()

window.after(100, bring_to_front_non_topmost)

window.mainloop()