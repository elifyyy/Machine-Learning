from sklearn.decomposition import PCA
from sklearn import manifold
import ReadFile as rf
import matplotlib.pyplot as plt


#with PCA
pca = PCA(n_components=2)
reduced_samples_pca = pca.fit_transform(rf.samples)


#with MDS
mds =  manifold.MDS(n_components=2)
reduced_samples_mds = mds.fit_transform(rf.samples)


#with isomap
isomap=manifold.Isomap(n_neighbors=5,n_components=2)
reduced_samples_isomap = isomap.fit_transform(rf.samples)


#with LLE
lle=manifold.LocallyLinearEmbedding(n_neighbors=5,n_components=2,eigen_solver='dense')
reduced_samples_lle = lle.fit_transform(rf.samples)


print("PCA : ")
#print(reduced_samples_pca)
print("MDS : ")
print(reduced_samples_mds)
print("ISOMAP : ")
print(reduced_samples_isomap)
print("LLE : ")
print(reduced_samples_lle)

#visualization
plt.scatter(reduced_samples_pca[:,0],reduced_samples_pca[:,1],c='r',alpha=0.5)
plt.title("PCA in 2-D")
plt.xlabel('label1')
plt.ylabel('label2')
plt.show()

plt.scatter(reduced_samples_mds[:,0],reduced_samples_mds[:,1],c='b',alpha=0.5)
plt.title("MDS in 2-D")
plt.xlabel('label1')
plt.ylabel('label2')
plt.show()

plt.scatter(reduced_samples_isomap[:,0],reduced_samples_isomap[:,1],c='g',alpha=0.5)
plt.title("ISOMAP in 2-D")
plt.xlabel('label1')
plt.ylabel('label2')
plt.show()

plt.scatter(reduced_samples_lle[:,0],reduced_samples_lle[:,1],c='r',alpha=0.5)
plt.title("LLE in 2-D")
plt.xlabel('label1')
plt.ylabel('label2')
plt.show()