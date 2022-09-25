from calendar import day_abbr
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title("Key Metrics Data Cube")
ax.set_xlabel("Sustainability")
ax.set_ylabel("Safety")
ax.set_zlabel("Impact")
ax.set_xlim((0, 1))
ax.set_ylim((0, 1))
ax.set_zlim((0, 1))

susdata = [0.8, 0.3, 0.4]
safedata = [0.35, 0.8, 0.6, ]
impactdata = [0.66, 0.8, 0.5]

ax.scatter3D(susdata, safedata, impactdata, cmap='Red');
plt.savefig("./output/bad-datacube.png")