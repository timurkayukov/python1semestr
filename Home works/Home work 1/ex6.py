import numpy as np
def mnk(x,y):
    x=np.array(x)
    y=np.array(y)
    a = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)  # среднее значение mean()
    b = np.mean(y) - a * np.mean(x)
    return float(a),float(b)
print(mnk(list(map(int,input().split())),list(map(int,input().split()))))
