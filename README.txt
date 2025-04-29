## Running JoltNotes Lite on macOS

You might see a warning that "JoltNotesLite" is damaged and can't be opened. This is a macOS security thing.

If you don't see an "Open Anyway" button in System Settings > Privacy & Security after trying to open the app, here's a Terminal command you can try:

1.  Open Terminal (Applications > Utilities > Terminal).
2.  Type this and press Enter:
    ```bash
    cd /Applications
    ```
    (If you put the app somewhere else, type `cd` then the folder path).
3.  Type this and press Enter (you might need your computer password):
    ```bash
    sudo xattr -dr com.apple.quarantine JoltNotesLite.app
    ```
4.  Try opening JoltNotes Lite again.

This command removes the quarantine flag that macOS places on downloaded files and may allow you to open the application.

Note: Running commands with `sudo` requires administrator privileges. Be cautious when executing commands in the Terminal and ensure you understand what they do. This workaround is provided for users who encounter issues with Gatekeeper. For a more seamless experience in the future, the developer will explore Apple's code signing and notarization process at a later date.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
JoltNotes Lite
Ever want a new notes app thats super minimalist? Well JoltNotes Lite is just for you! It's super light weight using only 71 lines of code, and its super simple! Theres two buttons and one text box, one button saves your note and the other one loads the note. I wanted to make this as lightweight as possible so there is no auto save and there is not space for any notes but one.

Textbox:
The Textbox is almost the whole window, press anywhere inside of it to start typing your note!

Loading Notes:
Anytime you save your note, it will automatically load when you next open the application. You could use the Load Button anytime you want to load your saved note.

Saving Notes:
The Save Button allows you to save your note, once thats done you could use the Load Button to manually load your saved note.

This release of JoltNotes Lite is built for Intel Macs ONLY, and has only been tested on "Sequoia" and "Monterey"

I plan on making this application have more features such as:
-Side bar for multiple notes
-Remove/relocate save & load buttons
-Make the UI highly customizable
-Allow drawing on the note textbox