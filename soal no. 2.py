import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [6, np.nan, 8, 9, 10],
    'C': [11, 12, 13, np.nan, 15]
}

df = pd.DataFrame(data)

def inputeMedian(value):
    median_value = df[value].median()
    df[value].fillna(median_value, inplace=True)

    print("Kolom {}".format(
        value
    ))

    print(df[value])

inputeMedian("A")
inputeMedian("B")
inputeMedian("C")