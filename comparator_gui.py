import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tooltip import ToolTip  # tooltip.py dosyasından ToolTip'i import et
from comparator import compare_columns
from excel_handler import read_excel, write_excel
from file_selector import FileSelector
from column_selector import ColumnSelector

class ComparatorGUI:
    def __init__(self, master, file_selector, column_selector):
        self.master = master
        self.file_selector = file_selector
        self.column_selector = column_selector

        self.progress = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress.pack()

        self.compare_button = tk.Button(master, text="Compare", command=self.compare)
        self.compare_button.pack()

        # Tooltip için
        self.compare_button_tooltip = ToolTip(self.compare_button)
        self.compare_button.bind("<Enter>", lambda e: self.compare_button_tooltip.show_tip("Karşılaştırmayı başlatır."))
        self.compare_button.bind("<Leave>", lambda e: self.compare_button_tooltip.hide_tip())

        # Yükleniyor animasyonu için
        self.loading_label = tk.Label(master, text="", fg="blue")
        self.loading_label.pack()

    def animate_loading(self, step=0):
        states = ["", ".", "..", "...", "...."]
        self.loading_label.config(text="Yükleniyor" + states[step % len(states)])
        self.master.after(500, self.animate_loading, step+1)

    def compare(self):
        self.animate_loading()

        file_paths = self.file_selector.file_paths
        column1_name = self.column_selector.column1_name_var.get().strip()
        column2_name = self.column_selector.column2_name_var.get().strip()

        if not all(file_paths) or not column1_name or not column2_name:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
            self.loading_label.config(text="")
            self.progress["value"] = 0
            return

        df1 = read_excel(file_paths[0])
        df2 = read_excel(file_paths[1])

        if column1_name not in df1.columns or column2_name not in df2.columns:
            messagebox.showerror("Hata", "Seçilen sütun dosyalardan birinde bulunamadı.")
            self.loading_label.config(text="")
            self.progress["value"] = 0
            return

        matched_data = compare_columns(df1, df2, column1_name, column2_name)

        if matched_data.empty:
            messagebox.showinfo("Sonuç", "Eşleşen veri bulunamadı.")
        else:
            output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
            if output_path:
                write_excel(matched_data, output_path)
                messagebox.showinfo("Başarılı", f"Eşleşen veriler {output_path} dosyasına yazıldı.")

        self.progress["value"] = 100
        self.master.update_idletasks()
        self.loading_label.config(text="")