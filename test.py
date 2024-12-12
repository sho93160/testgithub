import pandas as pd

df = pd.DataFrame({
    'nom': ['arthur', 'matthias', 'theo'],
    'age': [28, 22, 26]
})

pd.to_csv(df)

print(df)
