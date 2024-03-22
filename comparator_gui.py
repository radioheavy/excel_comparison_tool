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
        # Kullanıcıdan işlem başlatma onayı alma
        if not messagebox.askyesno("Onay", "Karşılaştırmayı başlatmak istediğinize emin misiniz?"):
            messagebox.showinfo("Bilgi", "Karşılaştırma işlemi iptal edildi.")
            return

        file_paths = self.file_selector.file_paths
        column1_name = self.column_selector.column1_name_var.get().strip()
        column2_name = self.column_selector.column2_name_var.get().strip()

        if not all(file_paths):
            messagebox.showerror("Hata", "Lütfen her iki dosyayı da seçin.")
            return

        if not column1_name or not column2_name:
            messagebox.showerror("Hata", "Her iki dosya için de bir sütun seçin.")
            return

        df1 = read_excel(file_paths[0])
        df2 = read_excel(file_paths[1])

        if column1_name not in df1.columns or column2_name not in df2.columns:
            messagebox.showerror("Hata", "Seçilen sütun bir veya her iki dosyada bulunamadı.")
            return

        # Kullanıcıya işlemin başladığını bildir
        messagebox.showinfo("Bilgi", "Karşılaştırma işlemi başlıyor...")

        matched_data = compare_columns(df1, df2, column1_name, column2_name)

        if matched_data.empty:
            messagebox.showinfo("Bilgi", "Eşleşen veri bulunamadı.")
            return

        # Dosya kaydetme diyalogu
        output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if output_path:
            write_excel(matched_data, output_path)
            messagebox.showinfo("Başarılı", f"Eşleşen veriler {output_path} dosyasına yazıldı.")
        else:
            messagebox.showinfo("Bilgi", "Kaydetme işlemi iptal edildi.")
