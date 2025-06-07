# JoltNotes

**Simple, minimalist note-taking for macOS and Windows**

## About JoltNotes

### JoltNotes is an ultra-minimalist note-taking application designed for simplicity and instant access to your thoughts.

- It features a single textbox that fills nearly the entire window, keeping your focus solely on your content.

- Automatic saving activates after just one second of inactivity, ensuring your work is always safe.

- Your notes load instantly when you launch the app, seamlessly picking up where you left off.

- The toolbar above the textbox allows you to easily format your text with bold, italic, underline, and ~~strikethrough~~ styles.

- Condense your headings with the "H" dropdown button on the toolbar, offering H1, H2, and H3 options.

- Personalize your experience by choosing from a vibrant array of themes accessible via the ⚙️ (Settings) icon. Themes include "Dark Mode," "Light Mode," "Terminal Amber," "Pretty Pink," and "Red Velvet."

- Apple Silicon Exclusive: On M1, M2, and newer Apple Silicon Macs, a special "Silicon" theme is automatically applied, reflecting the chip's distinctive aesthetic.

- A compact "Mini Jolt" window provides a stripped-down, always-on-top view for quick notes without cluttering your main workspace.

JoltNotes eliminates distractions and gets out of your way, letting you focus on what truly matters: **your thoughts**.

## Key Features

- **Single-Note Focus**: One persistent note that's always available
- **Auto-Save**: Your note saves automatically with each keystroke
- **Instant Loading**: Your note loads immediately when you open the app
- **Distraction-Free**: Clean interface with just what you need - nothing more

## Installation Guide

### System Requirements

- macOS Intel-based: macOS Monterey or later
- macOS Silicon-based: Apple M1 Chip or later

## Resolving macOS Security Warnings

When first launching JoltNotes, you may encounter a security warning stating "JoltNotes is damaged and can't be opened." This is due to macOS Gatekeeper security features.

### Option 1: Using System Settings

1. Try to open the app
2. Go to System Settings > Privacy & Security
3. Look for a message about JoltNotes and click "Open Anyway"

### Option 2: Using Terminal

If the "Open Anyway" button doesn't appear, you can use Terminal:

1. Open Terminal (Applications > Utilities > Terminal)
2. Navigate to where you installed the app:

`cd /Applications`

(If you installed elsewhere, adjust the path accordingly)

Run this command (you'll need to enter your password):

`sudo xattr -dr com.apple.quarantine JoltNotes.app`

Try opening JoltNotes again

> Note: Commands using **sudo** require administrator privileges. Only use Terminal commands if you understand their function. The developer will explore Apple's code signing and notarization process in future releases for a smoother experience.

# Using JoltNotes

## Starting a Note:

Simply click anywhere in the window and start typing (Multiple notes are planned for later release)

## Saving Your Work:

No save button needed - your note automatically saves every one second without activity

## Loading Previous Notes:

Your previous note loads automatically when you launch the app

## Support and Feedback

If you encounter issues or have suggestions for improvement, please open an issue on our GitHub repository.