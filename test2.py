import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#https://www.kite.com/python/answers/how-to-do-exponential-and-logarithmic-curve-fitting-in-python
#https://numpy.org/devdocs/user/absolute_beginners.html

x_data = np.array([10, 20, 30, 40, 50, 100, 270])
y_data = np.array([1, 3, 5, 7, 9, 10, 13])

log_x_data = np.log(x_data)
log_y_data = np.log(y_data)

curve_fit = np.polyfit(log_x_data, y_data, 1)
#print(curve_fit) 


y = 3.7984 * log_x_data - 7.52478
plt.plot(log_x_data, y_data, "ro")
plt.plot(log_x_data, y, "-")
#print(log_x_data)
b = log_x_data
#.reshape(7,1)
#print(b)

df = pd.DataFrame(log_x_data, y)
#print(df)
#df.to_csv('pd.csv')
data = pd.read_csv('pd.csv')
#np.savetxt('np.csv', a, fmt='%.2f', delimiter=',', header='1,  2')

