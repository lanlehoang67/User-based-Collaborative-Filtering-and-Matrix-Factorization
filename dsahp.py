import numpy as np 
from ahp import AHP

class DSAHP(AHP):
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d 
    def Probability(self):
        N = sum(self.c)
    def Mass(self,Di):
        N = sum(self.c)
        return Di/N
    def Bel(self,Di):
        d = ''.join(map(str,self.d))
        mass = self.Mass(Di)
        Bel = np.zeros(mass.shape)
        print(d[1,1])
        d_check = d
        for i in range(len(d)):
            if(len(d[i])==1):
                Bel[i] == mass[i]
            elif(len(d[i])>1):
                for j in range(d.shape[0]):
                    print(d[i][j])
                    d_check = (d[i][j] == d)
                    print(d_check)





d = np.array([
    ['C1'],
    ['C2'],
    ['C1','C2']
],dtype=object)

b = ['A1','A2','A3',['A1','A2'],['A1','A3'],['A2','A3'],['A1','A2','A3']]
c = np.array([5,2,3])
a = np.array([
    [3,2,2,3,0,0,0],
    [1,0,3,1,2,3,0]
])
ds = DSAHP(a,b,c,d)
ds.Bel(c)
# k = (a[1,1] ==a)
# print(k)