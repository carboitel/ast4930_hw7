import numpy as np


file = open('/home/boitelc/AST4930/HW7/sed.txt', 'r')
data = np.loadtxt(file, delimiter = ',')

x = data[:, 0]
y = data[:, 1]

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,1)

ax.plot(x,y)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_ylabel('luminosity')
ax.set_xlabel('wavelength')

plt.savefig('boitel_carolina_hw7.png')
