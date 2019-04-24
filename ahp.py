import numpy as np

class AHP():
    def __init__(self,R,A,B,C,RI):
        self.R = R
        self.A = A
        self.B = B
        self.C = C
        self.RI= RI
    def calculate(self,R):
        R_sqr = R.dot(R)
        R_sum = np.zeros((R.shape[0],1))
        R_div = np.zeros((R.shape[0],1))
        for i in range(len(R)):
            R_sum[i] = sum(R[i])
        for i in range(len(R_sum)):
            R_div[i] = R_sum[i]/sum(R_sum)
        return R_div
    def priority_vector(self,R):
        return self.calculate(R)- self.calculate(R.dot(R))
    def normalize_matrix(self,R):
        R_rev = R.T
        R_sum = np.zeros((R.shape[0],1))
        R_div = np.zeros(R.shape)
        for i in range(len(R)):
            R_sum[i] = sum(R_rev[i])
        for i in range(len(R)):
            for j in range(len(R)):
                R_div[i][j] =  R_rev[i][j]/R_sum[i]
        R_nor = R_div.T
        R_nor2 = np.zeros((R.shape[0],1))
        weights = R_nor2.copy()
        for i in range(len(R)):
            R_nor2[i] = sum(R_nor[i])
        for i in range(R_nor2.shape[0]):
            weights[i] = R_nor2[i]/sum(R_nor2)
        return weights
    def consistency_ratio(self,R):
        print(R.dot(self.priority_vector(R)))
        n = R.shape[0]
        R_cr = R.dot(self.normalize_matrix(R))
        c_vector = np.divide(R_cr, self.normalize_matrix(R))
        lamda_max = np.mean(c_vector)
        CI = (lamda_max-n)/(n-1)
        CR = CI / self.RI[n-1]
        if CR <0.1:
            return CR
        else:
            return 0


R =np.array( [
    [1,5,9],
    [1/5,1,3],
    [1/9,1/3,1]
])
RI= np.array([
    0,0,0.52,0.89,1.11,1.25,1.35,1.40,1.45,1.49,1.52,1.54,1.56,1.58,1.59
])
ahp = AHP(R,0.78,0.74,0.75,RI)
print(ahp.consistency_ratio(R))
