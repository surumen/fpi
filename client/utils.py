import pandas as pd


def change_empty_df_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    change dataframe values from "-" to 0
    """
    mapping = {'-': 0}
    replace_dict = {}
    for columns in df.columns:
        replace_dict[columns] = mapping

    return df.replace(replace_dict)
