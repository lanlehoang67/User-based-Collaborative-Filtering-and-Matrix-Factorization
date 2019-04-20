import numpy as np 

class Fuzzy(AHP):
    def __init__(self,R):
        self.R = R
        self.L = np.zeros(R.shape)
        self.U = np.zeros(R.shape)
        for i in range(len(R)):
            for j in range(len(R)):
                if(R[i][j]==1):
                    L[i][j] = 1
                    R[i][j] = 3
                elif(R[i][j]==9):
                    L[i][j] = 7
                    R[i][j] = 9
                else:
                    

