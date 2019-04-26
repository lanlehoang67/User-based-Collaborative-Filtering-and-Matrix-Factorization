import numpy as np 
from ahp import AHP

class DSAHP(AHP):
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d 
    def Probability(self):
        N = sum(self.a[0])
    def Mass(self,Di):
        return Di/sum(Di)
    def Bel(self,Di,array):
        b = array
        mass = self.Mass(Di)
        arr= np.zeros(b.shape)
        for i in range(len(b)):
            if len(b[i]) ==2:  
                    #khong co subset
                    arr[i] = mass[i]
        for i in range(len(b)):
            if len(b[i])+1== len(b):
                arr[i] = sum(mass)
            elif len(b[i])>2:
                for j in range(len(b)):
                        if b[j] in b[i]:
                            arr[i] += mass[j] 
        return arr
    def Pl(self,Di,array):
        b = array
        mass = self.Mass(Di)
        arr =np.zeros(b.shape)
        check=[]
        for i in range(len(b)):
            if len(b[i])+1 == len(b):
                arr[i]=sum(mass)
            else:
                if len(b[i]) ==2:
                    for j in range(len(b)):
                        if b[i] in b[j]:
                            arr[i] += mass[j]
                elif len(b[i]) >2:
                    for j in range(len(b)):
                        if b[j] in b[i]:
                            arr[i] += mass[j]
        return arr      



d = np.array(['C1','C2','C1C2'])

b = np.array(['A1','A2','A3','A1A2','A1A3','A2A3','A1A2A3'])
c = np.array([5,2,3])
a = np.array([
    [3,2,2,3,0,0,0],
    [1,0,3,1,2,3,0]
])

ds = DSAHP(a,b,c,d)
print(ds.Mass(a[1]))
print(ds.Pl(a[1],b))
# k = (a[1,1] ==a)
# print(k)