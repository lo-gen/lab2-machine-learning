from numpy import *
import matplotlib.pyplot as plt
import sys

def powers(list, power1, power2):
    new_matrix = []
    for n in range(len(list)):
        new_list = []
        for m in range(power1, power2 + 1):
             new_list.append(list[n]**m)
        new_matrix.append(new_list)
    return array(new_matrix)

matrix = transpose(loadtxt(sys.argv[1]))

X = matrix[0]
Y = matrix[1]
Y2 = []

X2 = linspace(X[0],X[len(X)-1],int((X[len(X)-1] - X[0])/0.2)).tolist()


Xp  = powers(X,0,int(sys.argv[2]))
Yp  = powers(Y,1,1)
Xpt = Xp.transpose()

A = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
A = A[:,0]

def poly(a, x):
    y = 0
    for i in range(len(a)):
        y += a[i] * (x ** i)    #Räknar ut värdet för y, följer: y = a0 + a1x + a2x^2... + anx^n
    return y

for i in X2: 
    Y2.append(poly(A, i))

plt.plot(X, Y,'ro') 
plt.plot(X2, Y2) 
plt.show()