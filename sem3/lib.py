import numpy as np
x=np.array([0,1,2,3,4,5])
y=np.array([2,3,4,5,6,7])
a=(np.mean(x*y)-np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2) #среднее значение mean()
b=np.mean(y)-a*np.mean(x)
A=np.array([1,2,3,4])
B=np.array([2,3,4,5])
print(A.dot(B)) #скалярное произведение
C=A@B #cкалярное произведение
print(C)
print(a,b)
