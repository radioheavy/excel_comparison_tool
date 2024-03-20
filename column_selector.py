import tkinter as tk
from tkinter import ttk
from excel_handler import read_excel

class ColumnSelector:
    def __init__(self, master):
        self.master = master

        self.column1_label = tk.Label(master, text="Select the column from the first file:")
        self.column1_label.pack()

        self.column1_name_var = tk.StringVar(master)
        self.column1_dropdown = ttk.Combobox(master, textvariable=self.column1_name_var)
        self.column1_dropdown.pack()

        self.column2_label = tk.Label(master, text="Select the column from the second file:")
        self.column2_label.pack()

        self.column2_name_var = tk.StringVar(master)
        self.column2_dropdown = ttk.Combobox(master, textvariable=self.column2_name_var)
        self.column2_dropdown.pack()

    def update_columns(self, file_paths):
        if file_paths[0]:
            df = read_excel(file_paths[0])
            self.column1_dropdown['values'] = df.columns.tolist()
            if df.columns.tolist():
                self.column1_dropdown.current(0)

        if file_paths[1]:
            df = read_excel(file_paths[1])
            self.column2_dropdown['values'] = df.columns.tolist()
            if df.columns.tolist():
                self.column2_dropdown.current(0)
