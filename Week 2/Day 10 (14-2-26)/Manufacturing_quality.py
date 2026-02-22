import numpy as np 
np.random.seed(8) 
# 1 = Defective, 0 = Good 
quality = np.random.binomial(1, 0.08, 200)  # 200 products, 8% defect rate 
print("Total Defective Products:", np.sum(quality)) 
print("Defect Percentage:", np.mean(quality) * 100) 