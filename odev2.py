import pandas as pd

data_file = "C:/Users/Muhametsha/OneDrive/Masaüstü/STAJ DEFTER/IRIS.csv"
df = pd.read_csv(data_file)


df.loc[df['species'] == 'Iris-setosa', 'species'] = 'elma'
print(df)

excel_file = "C:/Users/Muhametsha/OneDrive/Masaüstü/STAJ DEFTER/123.xlsx"
df.to_excel(excel_file, index=False)

df.loc[df['species'] == 'Iris-setosa', 'species'] = 'elma'
print(df)
