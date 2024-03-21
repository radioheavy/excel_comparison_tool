import os
import tkinter as tk
from tkinter import filedialog, messagebox

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
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xls;*.xlsx")])
        if file_path and os.path.isfile(file_path):
            self.file_paths[file_number - 1] = file_path
            self.update_columns_callback()
        else:
            messagebox.showerror("Error", "Invalid file path or format.")
