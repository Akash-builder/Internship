import numpy as np 
np.random.seed(42) 
days = 30 
# 1) Daily customers (Poisson) 
daily_customers = np.random.poisson(lam=120, size=days) 
# 2) Purchase amount (Normal) -> per day average purchase amount 
purchase_amount = np.random.normal(loc=1500, scale=300, size=days) 
purchase_amount = np.round(purchase_amount, 2) 
# 3) Product category selection (Multinomial) -> 4 categories per day 
# A=Electronics, B=Clothing, C=Grocery, D=Books 
category_prob = [0.35, 0.30, 0.25, 0.10] 
product_categories = np.random.multinomial(100, category_prob, size=days) 
# 4) Delivery time (Poisson) -> average delivery days per day 
delivery_time = np.random.poisson(lam=4, size=days) 
# 5) Waiting time between orders (Exponential) -> in minutes 
waiting_time = np.random.exponential(scale=3, size=days) 
waiting_time = np.round(waiting_time, 2) 
# 6) Product quality (Binomial) -> defective products per day out of 100 
defective_products = np.random.binomial(n=100, p=0.05, size=days) 
# ---------------- ANALYSIS ---------------- # 
print("========= 30 DAYS E-COMMERCE DATA ANALYSIS (NUMPY ONLY) =========\n") 
# Daily customers analysis 
print("1) DAILY CUSTOMERS (Poisson)") 
print("Total Customers:", np.sum(daily_customers)) 
print("Average Customers per Day:", np.mean(daily_customers)) 
print("Peak Customers in a Day:", np.max(daily_customers)) 
print("Lowest Customers in a Day:", np.min(daily_customers)) 
# Purchase amount analysis 
print("\n2) PURCHASE AMOUNT (Normal)") 
print("Average Purchase Amount:", np.mean(purchase_amount)) 
print("Max Purchase Amount:", np.max(purchase_amount)) 
print("Min Purchase Amount:", np.min(purchase_amount)) 
# Product category analysis 
print("\n3) PRODUCT CATEGORY SELECTION (Multinomial)") 
total_categories = np.sum(product_categories, axis=0) 
print("Total Category Sales (A,B,C,D):", total_categories) 
best_category = np.argmax(total_categories) 
print("Best Category Index (0=A,1=B,2=C,3=D):", best_category) 
# Delivery time analysis 
print("\n4) DELIVERY TIME (Poisson)") 
print("Average Delivery Time (days):", np.mean(delivery_time)) 
print("Max Delivery Time (days):", np.max(delivery_time)) 
# Waiting time analysis 
print("\n5) WAITING TIME BETWEEN ORDERS (Exponential)") 
print("Average Waiting Time (minutes):", np.mean(waiting_time)) 
print("Max Waiting Time (minutes):", np.max(waiting_time)) 
# Product quality analysis 
print("\n6) PRODUCT QUALITY (Binomial)") 
print("Total Defective Products:", np.sum(defective_products)) 
print("Average Defective per Day:", np.mean(defective_products)) 
print("Max Defective in a Day:", np.max(defective_products)) 
print("\n===============================================================") 