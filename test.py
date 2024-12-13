import pandas as pd

df = pd.DataFrame({
    'nom': ['arthur', 'matthias', 'theo'],
    'age': [28, 20, 26]
})

df.to_csv('dataframe.csv')

print(df)
