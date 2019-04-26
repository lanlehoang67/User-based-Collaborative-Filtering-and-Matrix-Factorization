import numpy as np
def biased_matrix_factorization(D,W,H,K,beta=0.0002,lamda=0.02,steps=5000):
    H= H.T
    bs=[]
    bi=[]
    es=[]
    cc=0
    u = np.sum(D)/len(D)
    for s in range(len(D)):
        bs.append((np.sum(D[s,:]-u))/len(D))
    for i in range(len(D[1,:])):
        bi.append((np.sum(D[:,i]-u))/len(D))
    for step in range(steps):
        for s in range(len(D)):
            for i in range(len(D[s])):
                if D[s,i] > 0:
                    cc= D[s,i]-( u+bs[s]+bi[i]+ np.dot(W[s,:],H[:,i]))
                    u = u + beta*cc
                    bs[s] += beta*(cc-lamda*bs[s])
                    bi[i] += beta*(cc-lamda*bi[i])
                    for k in range(K):
                        W[s][k] = W[s][k] + beta * (2 * cc * H[k][i] - lamda * W[s][k])
                        H[k][i] = H[k][i] + beta * (2 * cc * W[s][k] - lamda * H[k][i])
        e = 0
        for i in range(len(D)):
            for j in range(len(D[i])):
                if D[i][j] > 0:
                    e = e + pow(D[i][j] - np.dot(W[i,:],H[:,j]), 2)
                    for k in range(K):
                        e = e + (lamda/2) * (pow(W[i][k],2) + pow(H[k][j],2))
        if e < 0.001:
            break
    return W,H,bs,bi,u
R = [
     [5,3,0,1],
     [4,0,0,1],
     [1,1,0,5],
     [1,0,0,4],
     [0,1,5,4],
    ]

N = len(R)
M = len(R[0])
K = 2
W = np.random.rand(N,K)
H = np.random.rand(M,K)
def predict():
    ru = R.copy()
    w,h,bs,bi,u = biased_matrix_factorization(R,W,H,K)
    for i in range(len(R)):
        for j in range(len(R[i])):
            ru[i,j] = u+bs[i]+bi[j]+np.dot(w[i,:],h[:,j])
    return ru
print('W:')
print(W)
print('H:')
print(H)
print(predict())