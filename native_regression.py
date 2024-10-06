from matrix import *
import matplotlib.pyplot as plt

matrix = transpose(loadtxt("textfiles/dataset1.txt"))
X = matrix[0]
Y = matrix[1]

Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

print([[b],[m]])

plt.plot(X,Y,'ro')
plt.plot(X,Y2)
plt.show()