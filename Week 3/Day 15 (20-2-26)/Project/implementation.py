import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Sample dataset
data = {
"CustomerID": range(1,21),
"Age":[34,45,29,50,37,41,33,39,28,31,42,36,40,30,38,44,35,32,48,47],
"Gender":["Male","Female","Male","Female","Male","Female","Male","Female","Male","Female","Female","Male","Male","Female","Male","Female","Male","Female","Male","Female"],
"Tenure":[12,5,24,3,18,8,15,2,20,10,6,14,11,7,13,9,16,4,19,1],
"PlanType":["Premium","Basic","Premium","Basic","Premium","Basic","Premium","Basic","Premium","Basic",
"Premium","Basic","Premium","Basic","Premium","Basic","Premium","Basic","Premium","Basic"],
"MonthlyCharges":[70,30,90,25,80,35,75,28,85,32,40,65,78,33,82,29,76,31,88,27],
"TotalCharges":[840,150,2160,75,1440,280,1125,56,1700,320,240,910,858,231,1066,261,1216,124,1672,27],
"Churn":["No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","Yes","No","No","Yes","No","Yes","No","Yes","No","Yes"],
"ContractType":["Month-to-month","Month-to-month","One year","Month-to-month","Two year","Month-to-month","One year","Month-to-month","Twoyear","Month-to-month",
"Month-to-month","One year","Two year","Month-to-month","One year","Month-to-month","Two year","Month-to-month","Two year","Month-to-month"]
}
df = pd.DataFrame(data)
# 1. Churn distribution
plt.figure(figsize=(6,4))
sns.countplot(x="Churn", data=df)
plt.title("Customer Churn Distribution")
plt.show()
# 2. Churn vs Contract Type
plt.figure(figsize=(6,4))
sns.countplot(x="ContractType", hue="Churn", data=df)
plt.title("Churn by Contract Type")
plt.show()
# 3. Monthly Charges distribution by Churn
plt.figure(figsize=(6,4))
sns.boxplot(x="Churn", y="MonthlyCharges", data=df)
plt.title("Monthly Charges vs Churn")
plt.show()
# 4. High-risk customers (short tenure, high charges)
high_risk = df[(df['Tenure'] <= 6) & (df['MonthlyCharges'] > 50)]
print("High Risk Customers:\n",
high_risk[['CustomerID','Tenure','MonthlyCharges','Churn']])
# 5. Revenue impact
revenue_churned = df[df['Churn']=='Yes']['MonthlyCharges'].sum()
revenue_active = df[df['Churn']=='No']['MonthlyCharges'].sum()
print(f"Revenue from Churned Customers: ${revenue_churned}")
print(f"Revenue from Active Customers: ${revenue_active}")
plt.figure(figsize=(6,4))
plt.bar(['Churned','Active'], [revenue_churned, revenue_active],
color=['red','green'])
plt.title("Revenue Impact of Churn")
plt.ylabel("Monthly Revenue ($)")
plt.show()