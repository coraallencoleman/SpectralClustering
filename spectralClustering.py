#Do spectral clustering on monkey social networks data
import numpy as np
from sklearn.cluster import KMeans

#import data
M1 = np.loadtxt("monkeyM1.txt")
M1.shape
M2 = np.loadtxt("monkeyM2.txt")
M2.shape
gender = np.loadtxt("gender.txt", dtype=str)


D = sum(M1) #degree matrix by summing over all columns to get a vector
D = np.diag(D) #to make it into a matrix 35 diagonal entries correspond t
lap = D-M1 #laplacian matrix
[e, v] = np.linalg.eig(lap) #e = eigenvectors, v is diagonal matrix of eigenvalues
vv = np.diag(v) #vector of eigenvalues

kmeans = KMeans(n_clusters=3, random_state=0).fit(M1)
kmeans.labels_
kmeans.cluster_centers_

figure(figsize=(10,5))
subplot(121)
title('Original unclustered data')
plot(M1[:,0], M1[:,1], '.')
xlabel('$x_1$'); ylabel('$x_2$')

#small example
X = np.array([[1, 2], [1, 4], [1, 0],
    [4, 2], [4, 4], [4, 0]])
kmeans_ex = KMeans(n_clusters=3, random_state=0).fit(X)
kmeans_ex.labels_
kmeans_ex.predict([[0, 0], [4, 4]])
kmeans_ex.cluster_centers_