import numpy as np 
from ahp import AHP
class Fuzzy(AHP):
    def __init__(self,R):
        self.R = R
        self.L = np.zeros(R.shape)
        self.M = np.zeros((R.shape[0],3))
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
        for i in range(len(R)):
            for j in range(3):
                self.M[i,:] = [self.L[i,j],self.R[i,j],self.U[i,j]]  
    def geometric_mean(self):
        L,M,R = [],[],[]
        RI = np.zeros((self.R.shape[0],3))
        for i in range(len(RI)):
            L.append(self.avg_sum(self.L[i,:]))
            M.append(self.avg_sum(self.R[i,:]))
            R.append(self.avg_sum(self.U[i,:]))
        return L,M,R
    def avg_sum(self,array):
        s = 0
        for i in range(len(array)):
            s = s+array[i]
        return s/len(array)
    def fuzzy_weights(self):
        L,M,R = self.geometric_mean()
        weights = np.zeros((4,3))
        sumall = [sum(L),sum(M),sum(R)]
        sumall = np.array(sumall)
        for i in range(len(self.M)):
            for j in range(3):
                weights[i,j] = 1/sumall[j]*self.M[i,j]
        return weights
    def defuzzication(self):
        fuzzy_weights = self.fuzzy_weights()
        weights = np.zeros((fuzzy_weights.shape[0],1))
        for i in range(len(weights)):
            weights[i] = sum(fuzzy_weights[i])/len(fuzzy_weights[i])
        return weights
    def check(self):
        weights = self.defuzzication()
        if sum(weights) <= 1:
            print(weights)
            print(sum(weights))
        else:
            weights = weights/sum(weights)
            print(weights)
R = np.array([
        [1,5,4,7],
        [1/5,1,1/2,3],
        [1/4,2,1,3],
        [1/7,1/3,1/3,1]
])
fz = Fuzzy(R)
# print(fz.L)
# print(fz.R)
# print(fz.U)
# print(fz.M)
fz.check()
