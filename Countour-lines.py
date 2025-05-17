import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))  # Changed Y to Y**2 to ensure positive values under sqrt

plt.contour(X, Y, Z, levels=10, cmap="plasma")  # Fixed typo: countour -> contour
plt.colorbar(label="Height")
plt.title("Contour Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")  # Added for completeness
plt.show()