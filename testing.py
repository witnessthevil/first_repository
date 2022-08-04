import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,100)
y = -abs(x) + 1
plt.plot(x, y, '-r', label='y=-abs(x) + 1')
plt.title('Graph of y=-abs(x)+1')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()