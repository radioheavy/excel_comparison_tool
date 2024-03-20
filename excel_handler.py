import pandas as pd

def read_excel(file_path):
    """Excel dosyasını okur ve pandas DataFrame olarak döndürür."""
    return pd.read_excel(file_path)

def write_excel(dataframe, output_path):
    """DataFrame'i Excel dosyasına yazar."""
    dataframe.to_excel(output_path, index=False)
