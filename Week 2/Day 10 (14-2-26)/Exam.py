import numpy as np 
np.random.seed(4) 
result = np.random.binomial(1, 0.6, 100)  # 100 students, 70% pass prob 
print("Total Passed:", np.sum(result)) 
print("Pass Percentage:", np.mean(result) * 100) 