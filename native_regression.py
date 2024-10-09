from matrix import *
import matplotlib.pyplot as plt
import sys

matrix = transpose(loadtxt(sys.argv[1]))

X = matrix[0]
Y = matrix[1]
Y2 = [] 

Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

for i in X:
    print(i)
    Y2.append(b + m * i)

plt.plot(X,Y,'ro')
plt.plot(X,Y2)
plt.show()