import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
# Load dataset 
df = pd.read_csv("titanic.csv") 
# ============================== 
# KPI CALCULATIONS 
# ============================== 
total_passengers = len(df) 
total_survivors = df['Survived'].sum() 
total_non_survivors = total_passengers - total_survivors 
survival_rate = (total_survivors / total_passengers) * 100 
print("===== OVERALL KPIs =====") 
print("Total Passengers:", total_passengers) 
print("Total Survivors:", total_survivors) 
print("Total Non-Survivors:", total_non_survivors) 
print("Overall Survival Rate: {:.2f}%".format(survival_rate)) 
# ============================== 
# Survival by Gender 
# ============================== 
print("\n===== Survival Rate by Gender =====") 
print(df.groupby('Sex')['Survived'].mean() * 100) 
# ============================== 
# Survival by Passenger Class 
# ============================== 
print("\n===== Survival Rate by Passenger Class =====") 
print(df.groupby('Pclass')['Survived'].mean() * 100) 
# ============================== 
# Age Groups 
# ============================== 
bins = [0, 12, 19, 59, 100] 
labels = ['Child', 'Teen', 'Adult', 'Senior'] 
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels) 
print("\n===== Survival Rate by Age Group =====") 
print(df.groupby('AgeGroup')['Survived'].mean() * 100) 
# ============================== 
# Embarkation Port 
# ============================== 
print("\n===== Survival Rate by Embarkation Port =====") 
print(df.groupby('Embarked')['Survived'].mean() * 100) 
# ============================== 
# Family Size 
# ============================== 
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1 
print("\n===== Survival Rate by Family Size =====") 
print(df.groupby('FamilySize')['Survived'].mean() * 100) 
# ============================== 
# VISUALIZATIONS 
# ============================== 
sns.set(style="whitegrid") 
# 1. Survival Distribution 
plt.figure() 
df['Survived'].value_counts().plot.pie(autopct='%1.1f%%') 
plt.title("Survival Distribution") 
plt.ylabel("") 
plt.show() 
# 2. Survival by Gender 
plt.figure() 
sns.barplot(x='Sex', y='Survived', data=df) 
plt.title("Survival Rate by Gender") 
plt.show() 
# 3. Survival by Passenger Class 
plt.figure() 
sns.countplot(x='Pclass', hue='Survived', data=df) 
plt.title("Survival by Passenger Class") 
plt.show() 
# 4. Age Distribution by Survival 
plt.figure() 
sns.histplot(data=df, x='Age', hue='Survived', bins=30, kde=True) 
plt.title("Age Distribution by Survival") 
plt.show() 
# 5. Fare vs Survival 
plt.figure() 
sns.boxplot(x='Survived', y='Fare', data=df) 
plt.title("Fare vs Survival") 
plt.show() 
# 6. Survival by Embarkation Port 
plt.figure() 
sns.barplot(x='Embarked', y='Survived', data=df) 
plt.title("Survival Rate by Embarkation Port") 
plt.show() 
# 7. Family Size Impact 
plt.figure() 
sns.lineplot(x='FamilySize', y='Survived', data=df) 
plt.title("Survival Rate by Family Size") 
plt.show()