import numpy
def matrix_factorization(D, K, W, H, steps=5000, beta=0.0002, lamda=0.02):
    H = H.T
    for step in range(steps):
        for i in range(len(D)):
            for j in range(len(D[i])):
                if D[i][j] > 0:
                    eij = D[i][j] - numpy.dot(W[i,:],H[:,j])
                    for k in range(K):
                        W[i][k] = W[i][k] + beta * (2 * eij * H[k][j] - lamda * W[i][k])
                        H[k][j] = H[k][j] + beta * (2 * eij * W[i][k] - lamda * H[k][j])
        eR = numpy.dot(W,H)
        e = 0
        for i in range(len(D)):
            for j in range(len(D[i])):
                if D[i][j] > 0:
                    e = e + pow(D[i][j] - numpy.dot(W[i,:],H[:,j]), 2)
                    for k in range(K):
                        e = e + (lamda/2) * (pow(W[i][k],2) + pow(H[k][j],2))
        if e < 0.001:
            break
    return W, H.T
D = [
     [5,3,0,1],
     [4,0,0,1],
     [1,1,0,5],
     [1,0,0,4],
     [0,1,5,4],
    ]

D = numpy.array(D)

N = len(D)
M = len(D[0])
K = 2

W = numpy.random.rand(N,K)
H = numpy.random.rand(M,K)
print('W:')
print(W)
print('H:')
print(H)
nW, nH = matrix_factorization(D, K, W, H)
nD = numpy.dot(nW, nH.T)
print(nW)
print(nH)
