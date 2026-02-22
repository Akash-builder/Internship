import numpy as np 
np.random.seed(42) 
waiting_times = np.random.exponential(scale=5, size=30) 
print(waiting_times) 