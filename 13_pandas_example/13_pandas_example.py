import pandas as pd

def read_csv():
    df = pd.read_csv("sample.csv")
    print(df[df["value"]>df["value"].mean()])

def read_excel():
    df = pd.read_excel("sample.xlsx")
    df.to_csv("sample_data.csv", index=False)

if __name__ == '__main__':
    read_excel()