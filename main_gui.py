import tkinter as tk
from file_selector import FileSelector
from column_selector import ColumnSelector
from comparator_gui import ComparatorGUI

class ExcelComparatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Excel Comparator")

        self.file_selector = FileSelector(master, self.update_columns)
        self.column_selector = ColumnSelector(master)
        self.comparator_gui = ComparatorGUI(master, self.file_selector, self.column_selector)

    def update_columns(self):
        self.column_selector.update_columns(self.file_selector.file_paths)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelComparatorApp(root)
    root.mainloop()
