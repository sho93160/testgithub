import pandas as pd

df = pd.DataFrame({
    'nom': ['arthur', 'matthias', 'theo', 'valou'],
    'age': [28, 20, 26, 18]
})

df.to_csv('dataframe.csv')

print(df)
