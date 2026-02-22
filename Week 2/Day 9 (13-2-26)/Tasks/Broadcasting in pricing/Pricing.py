import numpy as np 
# Product prices (1D array) 
prices = np.array([1000, 1500, 2000, 2500]) 
# Discounts for customer types (1D array) 
discounts = np.array([0.05, 0.10, 0.20]) 
# Broadcasting: convert shapes for 2D calculation 
# discounts -> (3,1) and prices -> (1,4) 
final_prices = prices * (1 - discounts[:, np.newaxis]) 
# Cheapest price for each product 
cheapest_prices = final_prices.min(axis=0) 
print("Base Prices:", prices) 
print("\nDiscounts:", discounts) 
print("\nFinal Price Table (rows=customer types, cols=products):\n", 
final_prices) 
print("\nCheapest Price for each Product:\n", cheapest_prices)