import numpy as np
import astropy
import astropy.units as u

file = open('/home/boitelc/AST4930/HW7/sed.txt', 'r')
data = np.loadtxt(file, delimiter = ',')


x = data[:, 0] * (u.micron)
y = data[:, 1] * (u.erg/u.s)/(u.micron)

mask = (data[:, 0] >= 10) & (data[:, 0] <= 1000)

fullData = data[mask]

x = fullData[:, 0] * (u.micron)
y = fullData[:, 1] * (u.Lsun)/(u.micron)

x = np.flip(x)
y = np.flip(y)

value = np.trapz(y, x)
units = value.to(u.erg/u.s)

print(units)
