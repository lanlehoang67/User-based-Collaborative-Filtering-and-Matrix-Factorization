import numpy as np
import math as mt
#user-user
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
        sim = self.Sim()
        sim_pre = sim[u,:].copy()
        return self.check(u,i,sim_pre)
    def check(self,u,i,sim):
        for r in range(sim.shape[0]):
            if(self.r[r,i]==0):
                sim[r]=0
        return self.sort(sim,2,u,i)
    # def most_similar(self,u,item,array):
    #     arr =np.zeros((array.shape[0],array.shape[0]))
    #     for i in range(len(array)):
    #         for j in range(len(array)):
    #             arr[j] = array-array[j]
    #     for i in range(len(arr)):
    #         for j in range(len(arr)):
    #             if arr[i,j] ==0:
    #                 arr[i,j] =100
    #     min = np.min(np.absolute(arr))
    #     for i in range(len(arr)):
    #         for j in range(len(arr)):
    #             if arr[i,j] == min:
    #                 return self.real_pre(u,i,j,item)
    def sort(self,array,K,user,i):
        users_index = array.argsort()[-K:]
        return self.real_pre(user,users_index,i)
    def real_pre(self,user,users,i):
        sim = self.Sim()
        sum_sim_nei = sim[user,users[0]]*self.r[users[0],i]+sim[user,users[1]]*self.r[users[1],i]
        rui = sum_sim_nei/(np.absolute(sim[user,users[0]])+np.absolute(sim[user,users[1]]))
        return rui
    def predict_all(self):
        r_after = np.zeros(self.r.shape)
        for i in range(len(self.r)):
            for j in range(len(self.r[i])):
                if(self.r[i,j]==0):
                    r_after[i,j]=self.predict(i,j)
                else:
                    r_after[i,j]= self.r[i,j]
        return np.round(r_after)

R = np.array([
    [1,4,5,0,3],
    [5,1,0,5,2],
    [4,1,2,5,0],
    [0,3,4,0,4]
])
knn = UserKNN(R)
print(knn.predict_all())
