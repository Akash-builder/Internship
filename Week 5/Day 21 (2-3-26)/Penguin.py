import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=sns.load_dataset("penguins")
df
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.size
df.index
df.values
df.keys()
df.columns
df['species'].unique()
df['island'].unique()
df['sex'].unique()
df['species'].value_counts()
df['sex'].value_counts()
df['island'].value_counts()
df.isnull().sum()
df=df.dropna()
df
df.isnull().sum()
df.duplicated().sum()
total_penguins=len(df)
total_penguins
species_count=df['species'].value_counts()
species_percentage=df['species'].value_counts(normalize=True)*100
print("SPECIES COUNT:")
print(species_count)
print("PERCENTAGE OF SPECIES:")
print(species_percentage)
