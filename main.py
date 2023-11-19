import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Define the complex plane to plot the Mandelbrot set
xmin, xmax, ymin, ymax = -2, 2, -2, 2
npts = 400
x, y = np.meshgrid(np.linspace(xmin, xmax, npts), np.linspace(ymin, ymax, npts))
c = x + 1j*y

# Define the maximum number of iterations for the Mandelbrot set calculation
maxiter = 100

# Define a function to calculate the Mandelbrot set
def mandelbrot(c, maxiter):
    z = c
    for i in range(maxiter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return maxiter

# Calculate the Mandelbrot set
M = np.frompyfunc(mandelbrot, 2, 1)(c, maxiter).astype(float)

# Define the color map
# cmap = plt.cm.get_cmap('jet')
cmap = mpl.colormaps['jet']

# Plot the Mandelbrot set
plt.figure(figsize=(8,8))
plt.imshow(M, cmap=cmap, extent=(xmin, xmax, ymin, ymax))
plt.axis('off')
plt.show()