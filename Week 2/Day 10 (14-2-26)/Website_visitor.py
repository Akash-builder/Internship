import numpy as np 
np.random.seed(2) 
visitors = np.random.poisson(1200, 365) 
print("Average Visitors:", np.mean(visitors)) 
print("Peak Day Visitors:", np.max(visitors)) 