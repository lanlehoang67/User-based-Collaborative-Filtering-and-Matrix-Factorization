import numpy as np
import math as mt
class UserKNN():

    def __init__(self,r):
        self.r =r
    def norm(self,r):
        temp =0
        for i in range(len(r)):
                temp += r[i]**2
        return mt.sqrt(temp)
    def Sim(self):
        sim = np.zeros((self.r.shape[0],self.r.shape[0]))
        for i in range(len(self.r)):
           for j in range(len(self.r)):
               sim[i,j] = (np.dot(self.r[i,:],self.r[j,:]))/(self.norm(self.r[i,:])*self.norm(self.r[j,:]))
        return sim
    def predict(self,u,i):
        near_users = []
        for j in range(len(self.r)):
            if(self.r[j,i]!=0):
                near_users.append(self.r[j,i])
        sim = self.Sim()
        print(self.sort(sim,2))
        
    def sort(self,array,K):
        users_index = array[3].argsort()[-K:]
        print(array)
        return users_index
if __name__ == "__main__":
    R = np.array([
        [1,4,5,0,3],
        [5,1,0,5,2],
        [4,1,2,5,0],
        [0,3,4,0,4]
    ])
    print(len(R))
    knn = UserKNN(R)
    print(knn.Sim())
    print(knn.predict(3,0))
