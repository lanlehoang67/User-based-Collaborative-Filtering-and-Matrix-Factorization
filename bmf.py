import numpy 

def biased_matrix_factorization(D,K,steps,beta,lamda):
    S,I,P =[],[],[]
    u= []
    for i in range(len(D)):
        for j in range(len(D[i])):
            u