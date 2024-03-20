import tkinter as tk
from tkinter import filedialog
from excel_handler import read_excel, write_excel  # read_excel fonksiyonunu içe aktar
from comparator import compare_columns

class ComparatorGUI:
    def __init__(self, master, file_selector, column_selector):
        self.master = master
        self.file_selector = file_selector
        self.column_selector = column_selector

        self.compare_button = tk.Button(master, text="Compare", command=self.compare)
        self.compare_button.pack()

    def compare(self):
        file_paths = self.file_selector.file_paths
        column1_name = self.column_selector.column1_name_var.get()
        column2_name = self.column_selector.column2_name_var.get()

        if not all(file_paths):
            print("Please select both files.")
            return

        if not column1_name or not column2_name:
            print("Please select a column from both files.")
            return

        df1 = read_excel(file_paths[0])
        df2 = read_excel(file_paths[1])
        matched_data = compare_columns(df1, df2, column1_name, column2_name)

        output_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                   filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if output_path:
            write_excel(matched_data, output_path)
            print(f"Matched data written to {output_path}")
        else:
            print("Save cancelled, the data was not saved.")
