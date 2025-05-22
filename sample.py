import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

a=np.linspace(0,10,100)
b=a*2

plt.plot(a,b)
plt.xlabel('x_sample')
plt.ylabel('y_sample')
plt.title('this is test')
plt.grid(True)
plt.show()

