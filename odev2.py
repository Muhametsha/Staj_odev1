import pandas as pd
import numpy as np

data_file = "C:/Users/Muhametsha/OneDrive/Masaüstü/STAJ DEFTER/IRIS.csv"
df = pd.read_csv(data_file)

df.loc[df['species'] == 'Iris-setosa', 'species'] = 'elma'
print(df)

excel_file = "C:/Users/Muhametsha/OneDrive/Masaüstü/STAJ DEFTER/123.xlsx"
df.to_excel(excel_file, index=False)

df.loc[df['species'] == 'Iris-setosa', 'species'] = 'elma'
print(df)

asv = [5, 13, 21, 0.2]

normalize = []
for x in asv:
    normalize.append((x - np.min(asv)) / (np.max(asv) - np.min(asv)))

print(normalize)


#For dongusu ile yapilmiş hali
import pandas as pd
import numpy as np

# İris veri setini yükleme
data_file = "C:/Users/Muhametsha/OneDrive/Masaüstü/STAJ DEFTER/IRIS.csv"
df = pd.read_csv(data_file)

# Son sütunu çıkararak diğer sütunları alıyoruz
columns_to_normalize = df.columns[:-1]

# Normalleştirme işlemi için asv listesini oluşturma
asv = df[columns_to_normalize].values

# Normalleştirme işlemi
normalized_data = []
for column in range(asv.shape[1]):
    column_data = asv[:, column]
    normalized_column = (column_data - np.min(column_data)) / (np.max(column_data) - np.min(column_data))
    normalized_data.append(normalized_column)

# Normalleştirilmiş veri setini DataFrame olarak oluşturma
normalized_df = pd.DataFrame(np.transpose(normalized_data), columns=columns_to_normalize)

print("Normalleştirilmiş Iris veri seti:")
print(normalized_df)

#kutuphaneyle yapılmış hali
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# İris veri setini yükleme
data_file = "C:/Users/Muhametsha/OneDrive/Masaüstü/STAJ DEFTER/IRIS.csv"
df = pd.read_csv(data_file)

# Son sütunu hariç diğer sütunları alıyoruz
columns_to_normalize = df.columns[:-1]

# Normalizasyon için MinMaxScaler kullanma
scaler = MinMaxScaler()
df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

print("Normalleştirilmiş Iris veri seti:")
print(df)
