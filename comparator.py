from tkinter import messagebox

def compare_columns(dataframe1, dataframe2, column1_name, column2_name):
    """İki DataFrame'deki belirli sütunları karşılaştırır ve eşleşen verileri döndürür. Eksik sütunlar varsa hata mesajı gösterir."""
    if column1_name not in dataframe1.columns or column2_name not in dataframe2.columns:
        messagebox.showerror("Hata", "Belirtilen sütunlardan biri veya her ikisi dosyalarda bulunamadı.")
        return None
    matched_data = dataframe1[dataframe1[column1_name].isin(dataframe2[column2_name])]
    return matched_data
