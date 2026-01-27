import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("14_pandas_csv_division.csv")
    results = []

    for index, row in df.iterrows():
        if not row["numerator"].isdigit():
            results.append(None)
            continue
        if not row["denominator"].isdigit():
            results.append(None)
            continue
        if int(row["denominator"]) == 0:
            results.append(None)
            continue

        results.append(int(row["numerator"])/int(row["denominator"]))

    df['result'] = results

    df.to_csv("sample_output.csv", index=False)