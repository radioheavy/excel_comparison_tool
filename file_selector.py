import tkinter as tk
from tkinter import filedialog

class FileSelector:
    def __init__(self, master, update_columns_callback):
        self.master = master
        self.update_columns_callback = update_columns_callback
        self.file_paths = [None, None]

        self.file1_button = tk.Button(master, text="Select First Excel File", command=lambda: self.select_file(1))
        self.file1_button.pack()

        self.file2_button = tk.Button(master, text="Select Second Excel File", command=lambda: self.select_file(2))
        self.file2_button.pack()

    def select_file(self, file_number):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if file_number == 1:
            self.file_paths[0] = file_path
        else:
            self.file_paths[1] = file_path
        self.update_columns_callback(self.file_paths)
