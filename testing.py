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

print(sys.argv[1])

matrix = transpose(loadtxt(sys.argv[1]))
#print(matrix)

X = matrix[0]
Y = matrix[1]
Y2 = []

Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))

for i in X:
    Y2.append(b + m * i)


plt.plot(X,Y,'ro')
plt.plot(X,Y2)
plt.show()