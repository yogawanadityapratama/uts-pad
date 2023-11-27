import numpy as np
import pandas as pd

# Membaca file CSV
file_path = 'dataset_pasien.csv'
data = pd.read_csv(file_path)

# Soal no. 1b
missing_values = data.isnull().sum()
data_types = data.dtypes

result = pd.DataFrame({
    'Total Missing Value': missing_values,
    'Tipe Data': data_types
})
print(result)

# Soal no. 1c
mean_height = data['Tinggi_Badan'].mean()
data['Tinggi_Badan'].fillna(mean_height, inplace=True)

print("\nDataset setelah imputasi:")
print(data)

