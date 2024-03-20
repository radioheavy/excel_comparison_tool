def compare_columns(dataframe1, dataframe2, column1_name, column2_name):
    """İki DataFrame'deki belirli sütunları karşılaştırır ve eşleşen verileri döndürür."""
    matched_data = dataframe1[dataframe1[column1_name].isin(dataframe2[column2_name])]
    return matched_data
