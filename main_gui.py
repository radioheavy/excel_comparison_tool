import tkinter as tk
from comparator_gui import ComparatorGUI
from file_selector import FileSelector
from column_selector import ColumnSelector

if __name__ == "__main__":
    root = tk.Tk()
    column_selector = ColumnSelector(root)
    file_selector = FileSelector(root, column_selector.update_columns)
    app = ComparatorGUI(root, file_selector, column_selector)
    root.mainloop()
