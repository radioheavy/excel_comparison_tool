import tkinter as tk
from tkinter import filedialog, messagebox
from comparator import compare_columns
from excel_handler import read_excel, write_excel

class ComparatorGUI:
    def __init__(self, master, file_selector, column_selector):
        self.master = master
        self.file_selector = file_selector
        self.column_selector = column_selector

        self.compare_button = tk.Button(master, text="Compare", command=self.compare)
        self.compare_button.pack()

    def compare(self):
        file_paths = self.file_selector.file_paths
        column1_name = self.column_selector.column1_name_var.get().strip()
        column2_name = self.column_selector.column2_name_var.get().strip()

        if not all(file_paths):
            messagebox.showerror("Error", "Please select both files.")
            return

        if not column1_name or not column2_name:
            messagebox.showerror("Error", "Please select a column from both files.")
            return

        df1 = read_excel(file_paths[0])
        df2 = read_excel(file_paths[1])

        if column1_name not in df1.columns or column2_name not in df2.columns:
            messagebox.showerror("Error", "The selected column does not exist in one of the files.")
            return

        matched_data = compare_columns(df1, df2, column1_name, column2_name)

        if matched_data.empty:
            messagebox.showinfo("Info", "No matching data found.")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if output_path:
            write_excel(matched_data, output_path)
            messagebox.showinfo("Success", f"Matching data written to {output_path}")
