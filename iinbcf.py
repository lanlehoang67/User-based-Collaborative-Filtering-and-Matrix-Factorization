import numpy as np 
from uunbcf import UserKNN
#item-item
class ItemKNN(UserKNN):
    pass
R = np.array([
    [1,4,5,0,3],
    [5,1,0,5,2],
    [4,1,2,5,0],
    [0,3,4,0,4]
])
knn = ItemKNN(R.T)
print(knn.predict_all().T)