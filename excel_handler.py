import pandas as pd
from tkinter import messagebox

def read_excel(file_path):
    """Excel dosyasını okur ve pandas DataFrame olarak döndürür. Hata durumunda kullanıcıya mesaj gösterir."""
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        messagebox.showerror("Hata", f"Dosya okunamadı: {e}")
        return None

def write_excel(dataframe, output_path):
    """DataFrame'i Excel dosyasına yazar. Hata durumunda kullanıcıya mesaj gösterir."""
    try:
        dataframe.to_excel(output_path, index=False)
    except Exception as e:
        messagebox.showerror("Hata", f"Dosya yazılamadı: {e}")
