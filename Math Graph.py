import matplotlib.pyplot as plt

import numpy as np

value = np.random.randint(1,10,10)

plt.bar(range(len(value)),value)

plt.show()
