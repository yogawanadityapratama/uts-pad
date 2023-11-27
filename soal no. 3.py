import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [6, np.nan, 8, 9, 10],
    'C': [11, 12, 13, np.nan, 15]
}

df = pd.DataFrame(data)

# Melakukan feature scaling menggunakan metode standardization
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Membuat DataFrame dari data yang telah discaling
df_scaled = pd.DataFrame(scaled_data, columns=df.columns)

# Menampilkan DataFrame setelah scaling
print("\nDataFrame setelah scaling (standardization):")
print(df_scaled)