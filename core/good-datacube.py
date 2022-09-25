from calendar import day_abbr
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set() # plot styling
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title("Key Metrics Data Cube")
ax.set_xlabel("Sustainability")
ax.set_ylabel("Safety")
ax.set_zlabel("Impact")
ax.set_xlim((0, 1))
ax.set_ylim((0, 1))
ax.set_zlim((0, 1))
X, y = make_blobs(n_samples=1000, n_features=3, centers=4, cluster_std=0.17, center_box=(0.1, 0.9))
kmeans.fit(X)
y_means = kmeans.predict(X)
print(y_means)

print(X[:5])
print(y[:5])
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y_means)

susdata = []
safedata = []
impactdata = []

ax.scatter3D(susdata, safedata, impactdata, cmap='Red');
# plt.show()
plt.savefig("./output/good-datacube.png")