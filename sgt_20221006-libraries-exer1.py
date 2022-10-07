
import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('_mpl-gallery')

# make data
x = np.linspace(-10, 10, 21)
y = x**3 + 5

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

plt.show()