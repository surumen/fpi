

def change_values(df):
    """
    change dataframe values from "-" to 0
    """
    mapping = {'-' : 0}
    replace_dict = {}
    for columns in df.columns:
        replace_dict[columns] = mapping
        
    return df.replace(replace_dict)
