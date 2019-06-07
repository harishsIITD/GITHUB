import math
import random
import numpy
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import metrics
from scipy.spatial.distance import cdist

a=[]
b=[]
for i in range(100):
       a.append(random.randrange(0,25)/10)
       b.append(random.randrange(0,25)/10)
       
colors = 10*["b","k","g","r","c"]

       
def merge(a, b): 
      
    merged_list = [(a[i], b[i]) for i in range(0, len(a))] 
    return merged_list
data=merge(a,b) 
X=np.array(data)


class K_Means_algo:
    def __init__(self, k=4, tol=0.0001, max_iter=500):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self, data):

        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid - original_centroid) / original_centroid * 100.0) > self.tol:
                    print(np.sum((current_centroid - original_centroid) / original_centroid * 100.0))
                    optimized = False

            if optimized:
                break

    def predict(self, data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification
clf = K_Means_algo(k=4, tol=0.0001, max_iter=500)
clf.fit(X)
print(clf.centroids)
f1 = plt.figure(1)

for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1],
                marker="o", color="k", s=150, linewidths=5)

for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=150, linewidths=5)
        
        
plt.show()       

Label=[]
for i in X:
    Label.append(clf.predict(i))
df=pd.DataFrame()
df['x']=a
df['y']=b
df['Label']=Label


distortions = []
K = range(1,10)
for k in K:
    kmeanModel =  K_Means_algo(k=k, tol=0.0001, max_iter=500)
    kmeanModel.fit(X)
    centroids=kmeanModel.centroids.values()
    distortions.append(sum(np.min(cdist(X, list(centroids), 'euclidean'), axis=1)) / X.shape[0])

# Plot the elbow
f1 = plt.figure(2)


plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()

 

df.to_csv('Data_with_labels.csv')
