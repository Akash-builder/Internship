import numpy as np 
np.random.seed(3) 
cases = np.random.poisson(45, 30) 
print("Total Emergency Cases:", np.sum(cases)) 
print("Max Cases in a Day:", np.max(cases))