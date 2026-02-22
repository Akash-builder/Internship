import numpy as np 
np.random.seed(6) 
response_time = np.random.exponential(scale=0.5, size=100)  # 100 requests 
response_time = np.round(response_time, 3) 
print("Average Response Time:", np.mean(response_time)) 
print("Max Response Time:", np.max(response_time)) 