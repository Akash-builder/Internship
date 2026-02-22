import numpy as np 
np.random.seed(7) 
calls = np.random.poisson(25, 24)  # avg 25 calls/hour 
print("Total Calls in 24 Hours:", np.sum(calls)) 
print("Max Calls in an Hour:", np.max(calls)) 