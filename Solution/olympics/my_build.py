import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    data=pd.read_csv("olympics.csv",skiprows=1)
    data=data.rename(columns={'01 !': 'Gold_S', '02 !': 'Siver_S','03 !':'Bronze_S'})
    data=data.rename(columns={'01 !.1': 'Gold_W', '02 !.1': 'Siver_W','03 !.1':'Bronze_W'})
    data=data.rename(columns={'01 !.2': 'Gold_G', '02 !.2': 'Siver_G','03 !.2':'Bronze_G'})
    data['country name'] = data['Unnamed: 0'].str.split('(').str.get(0)
    data=data.drop('Unnamed: 0',axis=1)
    data=data.drop(data.tail(1).index)
    return data
    
def first_country(data):
    return data.head(1)
    
def gold_medal(data):
    return data.loc[data["Gold_S"]==data.iloc[:,1].max(),'country name']


def biggest_difference_in_gold_medal(data):
    data['diff']=data['Gold_W']-data['Gold_S']
    return data.loc[data["diff"]==data['diff'].min(),'country name']

def get_points(data):
    g=data['Gold_G'].values
    gnew=[i * 3 for i in g]
    s=data['Siver_G'].values
    snew=[i*2 for i in s]
    b=data['Bronze_G'].values
    gnew=np.array(gnew)
    snew=np.array(snew)
    points=gnew+snew+b
    data['points']=points
    return data['points']
def kmeans():
    #for finding optimum value of K
    distortions = []
    X=data.drop('country name',axis=1)
    K = range(1,10)
    for k in K:    
        kmeanModel = KMeans(n_clusters=k).fit(X)
        kmeanModel.fit(X)
        distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
    #Plot the elbow
    plt.plot(K, distortions, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.title('The Elbow Method showing the optimal k')
    plt.show()
    print("The optimum value of K is 4\n")
    #Using KMeans for 4 clusture
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(X)
    print("Cluster center :\n\n\n{}".format(kmeans.cluster_centers_))
    