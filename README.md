# JoltNotes Lite
**Simple, minimalist note-taking for macOS**

## About JoltNotes Lite
JoltNotes Lite is an ultra-minimalist note-taking application designed for simplicity. It features a single textbox that fills the entire window, allowing you to focus solely on your thoughts. With automatic saving on each keystroke and instant loading when you launch the app, JoltNotes Lite eliminates distractions and gets out of your way.

## Key Features
- **Single-Note Focus**: One persistent note that's always available
- **Auto-Save**: Your note saves automatically with each keystroke
- **Instant Loading**: Your note loads immediately when you open the app
- **Distraction-Free**: Clean interface with just what you need - nothing more

## Installation Guide

### System Requirements
- macOS on Intel-based Macs
- Tested on macOS Sequoia 15.3.2 and Monterey 12.7.6

## Resolving macOS Security Warnings
When first launching JoltNotes Lite, you may encounter a security warning stating "JoltNotesLite is damaged and can't be opened." This is due to macOS Gatekeeper security features.
### Option 1: Using System Settings

1. Try to open the app
2. Go to System Settings > Privacy & Security
3. Look for a message about JoltNotesLite and click "Open Anyway"

### Option 2: Using Terminal
If the "Open Anyway" button doesn't appear, you can use Terminal:

1. Open Terminal (Applications > Utilities > Terminal)
2. Navigate to where you installed the app:

`cd /Applications`

(If you installed elsewhere, adjust the path accordingly)

Run this command (you'll need to enter your password):

`sudo xattr -dr com.apple.quarantine JoltNotesLite.app`

Try opening JoltNotes Lite again

> Note: Commands using **sudo** require administrator privileges. Only use Terminal commands if you understand their function. The developer will explore Apple's code signing and notarization process in future releases for a smoother experience.

# Using JoltNotes Lite

## Starting a Note:
Simply click anywhere in the window and start typing

## Saving Your Work:
No save button needed - your note automatically saves every one second without activity

## Loading Previous Notes:
Your previous note loads automatically when you launch the app

### About the JoltNotes Family
JoltNotes Lite is part of the JoltNotes application family:

- **JoltNotes** - Our upcoming full-featured note-taking application
- **JoltNotes Lite** - This simplified, single-note version
- **JoltminiNotes** - Our compact sticky-notes style application

## Support and Feedback
If you encounter issues or have suggestions for improvement, please open an issue on our GitHub repository.
###
#
*JoltNotes Lite is currently built for Intel-based Macs only. Apple Silicon support is planned for future releases.*
