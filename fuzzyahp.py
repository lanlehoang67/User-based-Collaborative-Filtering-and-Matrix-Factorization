import numpy as np 
from ahp import AHP
class Fuzzy(AHP):
    def __init__(self,R):
        self.R = R
        self.L = np.zeros(R.shape)
        self.U = np.zeros(R.shape)
        for i in range(len(R)):
            for j in range(len(R)):
                if(self.R[i][j]==1):
                    self.L[i,j] = 1
                    self.U[i,j] = 3
                elif(self.R[i][j]==9):
                    self.L[i,j] = 7
                    self.U[i,j] = 9
                elif(self.R[i,j]%2==0 and int(self.R[i,j])==self.R[i,j]):
                    self.R[i,j] += 1
                    self.L[i,j] = self.R[i][j]-2
                    self.U[i,j] = self.R[i][j] +2
                elif(int(self.R[i,j])!=self.R[i,j]):
                    if((1/self.R[i,j])%2==0):
                        self.R[i,j] = 1/((1/self.R[i,j])+1)
                        self.L[i,j] = 1/((1/self.R[i,j])+2)      
                        self.U[i,j] = 1/((1/self.R[i,j])-2)
                    else:
                        self.L[i,j] = 1/((1/self.R[i,j])+2)      
                        self.U[i,j] = 1/((1/self.R[i,j])-2)
                else:
                    self.L[i,j] = self.R[i][j]-2
                    self.U[i,j] = self.R[i][j] +2 
    def geometric_mean(self):
        L = M = R = np.ones((R.shape[0],3))
        RI = np.zeros((self.R.shape[0],3))
        for i in range(len(RI)):
            for j in range()
        return RI 
R = np.array([
        [1,5,4,7],
        [1/5,1,1/2,3],
        [1/4,2,1,3],
        [1/7,1/3,1/3,1]
])
fz = Fuzzy(R)
print(fz.L)
print(fz.R)
print(fz.U)
print(fz.geometric_mean())