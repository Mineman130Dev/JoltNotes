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
JoltNotes Lite v1.1.0
Ever wanted a new notes app that's super minimalist? Well, JoltNotes Lite is just for you! JoltNotes Lite features a single textbox for typing. This means only one note is available at all times within JoltNotes Lite, making it as simple as possible! The note saves automatically and loads upon opening the application.

Textbox:
The Textbox is the whole window, press anywhere inside of it to start typing your note!

Loading Notes:
Notes are loaded upon opening the application! Theres now no need for manually loading notes.

Saving Notes:
There is no longer a save button, the note is saved each keystorke. This is a only temporarily solution to removing the save button.

This release of JoltNotes Lite is built for Intel Macs ONLY, and has only been tested on "Sequoia-15.3.2" and "Monterey-12.7.6"