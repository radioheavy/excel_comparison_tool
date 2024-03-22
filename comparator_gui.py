import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tooltip import ToolTip  # ToolTip sınıfını import edin
from comparator import compare_columns
from excel_handler import read_excel, write_excel

class ComparatorGUI:
    def __init__(self, master, file_selector, column_selector):
        self.master = master
        self.file_selector = file_selector
        self.column_selector = column_selector

        self.progress = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress.pack()

        self.compare_button = tk.Button(master, text="Compare", command=self.compare)
        self.compare_button.pack()

        # Compare butonu için tooltip ekleme
        self.compare_button_tooltip = ToolTip(self.compare_button)
        self.compare_button.bind("<Enter>", lambda e: self.compare_button_tooltip.show_tip("Karşılaştırmayı başlatır."))
        self.compare_button.bind("<Leave>", lambda e: self.compare_button_tooltip.hide_tip())

    def compare(self):
        if not messagebox.askyesno("Onay ✅", "Karşılaştırmayı başlatmak istediğinize emin misiniz?"):
            messagebox.showinfo("İptal Edildi ❌", "Karşılaştırma işlemi iptal edildi.")
            return

        self.progress["maximum"] = 100
        self.progress["value"] = 0
        self.master.update_idletasks()

        file_paths = self.file_selector.file_paths
        column1_name = self.column_selector.column1_name_var.get().strip()
        column2_name = self.column_selector.column2_name_var.get().strip()

        if not all(file_paths):
            messagebox.showerror("Hata ❌", "Lütfen her iki dosyayı da seçin.")
            return

        if not column1_name or not column2_name:
            messagebox.showerror("Hata ❌", "Lütfen her iki dosyadan bir sütun seçin.")
            return

        self.progress["value"] = 50
        self.master.update_idletasks()

        df1 = read_excel(file_paths[0])
        df2 = read_excel(file_paths[1])

        if column1_name not in df1.columns or column2_name not in df2.columns:
            messagebox.showerror("Hata ❌", "Seçilen sütun dosyalardan birinde bulunamadı.")
            return

        self.progress["value"] = 75
        self.master.update_idletasks()

        matched_data = compare_columns(df1, df2, column1_name, column2_name)

        if matched_data.empty:
            messagebox.showinfo("Sonuç ⚠️", "Eşleşen veri bulunamadı.")
        else:
            output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
            if output_path:
                write_excel(matched_data, output_path)
                messagebox.showinfo("Başarılı ✅", f"Eşleşen veriler {output_path} dosyasına yazıldı.")

        self.progress["value"] = 100
        self.master.update_idletasks()
