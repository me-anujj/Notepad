import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os


class Notepad:
    _root = Tk()

    width = 300
    height = 300
    TextArea = Text(_root)
    Menubar = Menu(_root)
    FileMenu = Menu(Menubar, tearoff=0)
    EditMenu = Menu(Menubar, tearoff=0)
    HelpMenu = Menu(Menubar, tearoff=0)
    scrollbar = Scrollbar(TextArea)
    _file = None

    def __init__(self, **kwargs):

        # Set Icon
        # try:
        #     self._root.wm_iconbitmap("Notepad.ico")
        # except KeyError:
        #     pass

        # set Window Size
        try:
            self.height = kwargs['height']
        except KeyError:
            pass

        try:
            self.width = kwargs['width']
        except KeyError:
            pass

        self._root.title("Untitled-Notepad")

        screen_width = self._root.winfo_screenwidth()
        screen_height = self._root.winfo_screenheight()

        left = (screen_width // 2) - (self.width // 2)
        top = (screen_height // 2) - (self.height // 2)

        self._root.geometry(f'{self.width}x{self.height}+{left}+{top}')

        self._root.grid_rowconfigure(0, weight=1)
        self._root.grid_columnconfigure(0, weight=1)

        self.TextArea.grid(sticky=N + E + S + W)

        # File Menu
        self.FileMenu.add_command(label="New", command=self.new_file)
        self.FileMenu.add_command(label="Open", command=self.open_file)
        self.FileMenu.add_command(label="Save", command=self.save_file)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit", command=self.quit_application)

        self.Menubar.add_cascade(label="File", menu=self.FileMenu)

        # Edit Menu
        self.EditMenu.add_command(label="Cut", command=self.cut)
        self.EditMenu.add_command(label="Copy", command=self.copy)
        self.EditMenu.add_command(label="Paste", command=self.paste)

        self.Menubar.add_cascade(label="Edit", menu=self.EditMenu)

        # Help Menu
        self.HelpMenu.add_command(label="About Notepad", command=self.show_about)
        self.Menubar.add_cascade(label="Help", command=self.HelpMenu)

        self._root.configure(menu=self.Menubar)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.scrollbar.configure(command=self.TextArea.yview)
        self.TextArea.configure(yscrollcommand=self.scrollbar.set)

    def quit_application(self):
        self._root.destroy()

    def show_about(self):
        showinfo("Notepad", "Anuj Agarwal")

    def open_file(self):
        self._file = askopenfilename(defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self._file == "":
            self._file = None
        else:

            self._root.title(os.path.basename(self._file) + "-Notepad")
            self.TextArea.delete(1.0, END)

            file = open(self._file, "r")
            self.TextArea.insert(1.0, file.read())
            file.close()

    def new_file(self):
        self._root.title("Untitled-Notepad")
        self._file = None
        self.TextArea.delete(1.0, END)

    def save_file(self):
        if self._file == None:
            self._file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if self._file == "":
                self._file = None
            else:
                file = open(self._file, "w")
                file.write(self.TextArea.get(1.0, END))
                file.close()

                self._root.title(os.path.basename(self._file + "-Notepad"))

        else:
            file = open(self._file, "w")
            file.write(self.TextArea.get(1.0, END))
            file.close()

    def cut(self):
        self.TextArea.event_generate("<<Cut>>")

    def copy(self):
        self.TextArea.event_generate("<<Copy>>")

    def paste(self):
        self.TextArea.event_generate("<<Paste>>")

    def run(self):
        self._root.mainloop()


notepad = Notepad(width=600, height=600)
notepad.run()
