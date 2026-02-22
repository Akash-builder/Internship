import numpy as np 
np.random.seed(9) 
approval = np.random.binomial(1, 0.6, 150)  # 150 applications, 60% 
approval 
print("Total Approved Loans:", np.sum(approval)) 
print("Approval Percentage:", np.mean(approval) * 100) 