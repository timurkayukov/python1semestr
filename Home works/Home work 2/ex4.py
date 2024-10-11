import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('iris_data.csv')
features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
combinations = [(x, y) for i, x in enumerate(features) for y in features[i+1:]]
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()
for i, (x, y) in enumerate(combinations):
    ax = axes[i]
    ax.scatter(data[x], data[y], alpha=0.5)
    ax.set_title(f'{x} vs {y}')
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    A = np.vstack([data[x], np.ones(len(data[x]))]).T
    m, c = np.linalg.lstsq(A, data[y], rcond=None)[0]
    ax.plot(data[x], m * data[x] + c, 'r', label='y={:.2f}x+{:.2f}'.format(m, c))
    ax.legend()
    ax.grid()
plt.tight_layout()
plt.show()
for x, y in combinations:
    A = np.vstack([data[x], np.ones(len(data[x]))]).T
    m, c = np.linalg.lstsq(A, data[y], rcond=None)[0]
    print(f'Коэффициенты для {x} и {y}: m = {m:.2f}, c = {c:.2f}')

