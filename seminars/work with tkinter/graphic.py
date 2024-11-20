import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def mnk(x,y):
    x=np.array(x)
    y=np.array(y)
    a = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)  # среднее значение mean()
    b = np.mean(y) - a * np.mean(x)
    return float(a),float(b)
def read_csv(file):
