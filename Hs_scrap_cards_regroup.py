import pandas as pd

df = pd.read_csv('hscards.csv')

# Nbr victoire par cartes
df['Nombre de victoires'] = df['Taux de victoire'] / 100 * df['Nombre de parties']

# Regrouper les cartes
grouped_df = df.groupby(['Nom', 'Date'], as_index=False).agg({'Coût': 'first', 'Quantité': 'sum', 'Nombre de parties': 'sum', 'Nombre de victoires': 'sum'})

# Calcule du taux de victoires
grouped_df['Taux de victoire'] = grouped_df['Nombre de victoires'] / grouped_df['Nombre de parties'] * 100

# Nbr total parties par cartes
grouped_df['Nombre total de parties'] = grouped_df.groupby('Nom')['Nombre de parties'].transform('sum')

# Supp colonnes
grouped_df = grouped_df.drop(['Nombre de victoires', 'Nombre de parties'], axis=1)

# Placer dans un csv
grouped_df.to_csv('hsregroupcards.csv', index=False)