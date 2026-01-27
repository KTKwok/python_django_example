import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("14_pandas_csv_division.csv")
    df["numerator"] = pd.to_numeric(df["numerator"], errors="coerce")
    df["denominator"] = pd.to_numeric(df["denominator"], errors="coerce")
    df["result"] = df["numerator"]/df["denominator"]
    df["result"] = df["result"].round(4)
    df.to_csv("sample_output.csv", index=False)