import pandas as pd

def conversion(file_path, start_row=10):
    df = pd.read_excel(file_path, skiprows=start_row, usecols='B:F', engine='xlrd')

    df.columns = ["Product name", "Product code", "Product group", "Sales quantity", "Sales amount in USD"]

    df["Date of sale"] = None

    curent_date = None
    rows_to_keep = []

    for i, row in df.iterrows():
        name = str(row["Product name"]).strip()

        try:
            parse_date = pd.to_datetime(name, format="%d.%m.%Y", errors="raise")
            curent_date = parse_date
            print(curent_date)

        except Exception:
            df.at[i, "Date of sale"] = curent_date
            rows_to_keep.append(i)

    df = df.loc[rows_to_keep].reset_index(drop=True)

    return df