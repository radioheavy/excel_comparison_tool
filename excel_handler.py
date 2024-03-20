import pandas as pd
from tkinter import messagebox

def read_excel(file_path):
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        messagebox.showerror("Hata", f"Dosya okunamadı: {e}")
        return None

def write_excel(dataframe, output_path):
    try:
        dataframe.to_excel(output_path, index=False)
    except Exception as e:
        messagebox.showerror("Hata", f"Dosya yazılamadı: {e}")
