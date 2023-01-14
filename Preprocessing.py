import pandas as pd
import numpy as np
input = pd.read_csv("Recipe.csv")
df = input[['name','tags','ingredients']].head(10000).copy()
df['ingredients'] = df['ingredients'].str.lower().str.replace('[^a-zA-Z,\s]','', regex=True)
df['tags'] = df['tags'].str.lower().str.replace('[^0-9-a-zA-Z,\s]','', regex=True)
df1 = df[df['tags'].str.contains('european')].copy()
df1['cuisine'] = 'european'
df2 = df[df['tags'].str.contains('indian')].copy()
df2['cuisine'] = 'indian'
df3 = df[df['tags'].str.contains('japanese')].copy()
df3['cuisine'] = 'japanese'
df4 = df[df['tags'].str.contains('north-american')].copy()
df4['cuisine'] = 'north-american'
df_v = pd.concat([df1,df2,df3,df4])
df_v['type'] = ''
df_v = df_v.reset_index()
for i in range(len(df_v)):
    tags = df_v.loc[i].tags
    if('vegetarian' in tags):
        df_v.loc[i, ['type']] = 'veg'
    else:
        df_v.loc[i, ['type']] = 'non-veg'
df_v.reset_index()
input = pd.read_csv("Allergy.csv")
input['Allergy'] = input['Allergy'].str.lower()
input['Food'] = input['Food'].str.lower()
df_v.to_csv('recipe_preprocessed.csv', index=False)
input.to_csv('Allergy.csv')