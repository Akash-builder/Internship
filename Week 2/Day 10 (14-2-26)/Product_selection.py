import numpy as np 
np.random.seed(5) 
# Probabilities for product selection 
p = [0.4, 0.3, 0.2, 0.1] 
product_counts = np.random.multinomial(100, p)  # 100 customers 
print("Product A,B,C,D counts:", product_counts)