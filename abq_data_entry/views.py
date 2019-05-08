import tkinter as tk
from tkinter import messagebox

class MainMenu(tk.Menu):
    """The Application's main menu"""

    def __init__(self, parent, settings, callbacks, **kwargs):
        super().__init__(parent, **kwargs)

        # The file menu
        file_menu = tk.Menu(self, tearoff=False)
        file_menu.add_command(label="Select file...", command=callbacks["file->select"])
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=callbacks["file->quit"])
        self.add_cascade(label="File", menu=file_menu)

        # The option menu
        options_menu = tk.Menu(self, tearoff=False)
        options_menu.add_checkbutton(label="Autofill Date", variable=settings["autofill date"])
        options_menu.add_checkbutton(label="Autofill Sheet Data", variable=settings["autofill sheet data"])
        self.add_cascade(label="Options", menu=options_menu)

        # The help menu
        help_menu = tk.Menu(self, tearoff=False)
        help_menu.add_command(label="About...", command=self.show_about)
        self.add_cascade(label="Help", menu=help_menu)

    def show_about(self):
        """Show the about dialog"""

        about_message = "ABQ Data Entry"
        about_detail = "by Kenneth Chua \n For assistance please contact the author."

        messagebox.showinfo(title="About", message=about_message, detail=about_detail)
