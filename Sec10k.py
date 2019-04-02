import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
global word

import random
#random.seed( 3 )
word=list()
np.random.seed(3)

vocab_frame=list()

x=pd.read_excel("C:/Users/harishs/Desktop/Stamper/Press Release.xlsx")

#x=x[:1000]
print(len(x))

stopwords = nltk.corpus.stopwords.words('english')
#print(stopwords[:10])

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

totalvocab_stemmed = []
totalvocab_tokenized = []
for i in x['NewsFeed']:
    allwords_stemmed = tokenize_and_stem(i) #for each item in 'synopses', tokenize/stem
    totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list
    
    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)
vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
print('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')
#print(vocab_frame.head())

from sklearn.feature_extraction.text import TfidfVectorizer

#define vectorizer parameters
tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200,
                                 min_df=0.2, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

tfidf_matrix = tfidf_vectorizer.fit_transform(x["NewsFeed"]) #fit the vectorizer to synopses

print(tfidf_matrix.shape)


terms = tfidf_vectorizer.get_feature_names()

from sklearn.metrics.pairwise import cosine_similarity
dist = 1 - cosine_similarity(tfidf_matrix)

from sklearn.cluster import KMeans

num_clusters = 5

km = KMeans(n_clusters=num_clusters)

km.fit(tfidf_matrix)

clusters = km.labels_.tolist()

#from sklearn.externals import joblib

#uncomment the below to save your model 
#since I've already run my model I am loading from the pickle

#joblib.dump(km,  'doc_cluster.pkl')

#km = joblib.load('C:/Users/harishs/Desktop/document_cluster-master/doc_cluster.pkl')
#clusters = km.labels_.tolist()

arts = { 'title': x['Title'],'Articles': x['NewsFeed'], 'cluster': clusters, 'Index' : x['Article Number']}


print(arts['Articles'])

frame=pd.DataFrame(arts)
#
#frame = pd.DataFrame(arts, index = [clusters] , columns = ['title','cluster','Articles','Index'])
frame.to_csv("C:/Users/harishs/Desktop/kmeans.csv")

#print(frame["Articles"])
print(len(frame["Articles"]))

print(frame['cluster'].value_counts())

#grouped = frame['Title'].groupby(frame['cluster'])

#print(cluster)

#from __future__ import print_function

print("Top terms per cluster:")
print()
#sort cluster centers by proximity to centroid
print("Top terms per cluster:")
print()
#sort cluster centers by proximity to centroid
order_centroids = km.cluster_centers_.argsort()[:, ::-1] 

for i in range(num_clusters):
    print("Cluster %d words:" % i, end='')
    
    for ind in order_centroids[i, :6]: #replace 6 with n words per cluster
        print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
    print() #add whitespace
    print() #add whitespace
    
    print("Cluster %d titles:" % i, end='')
    for title in frame['title']:
        print(' %s,' % title)
    print() #add whitespace
    print() #add whitespace
    
print()
print()


import os  # for os.path.basename

import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn.manifold import MDS

MDS()

# convert two components as we're plotting points in a two-dimensional plane
# "precomputed" because we provide a distance matrix
# we will also specify `random_state` so the plot is reproducible.
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)

pos = mds.fit_transform(dist)  # shape (n_components, n_samples)

xs, ys = pos[:, 0], pos[:, 1]
print()
print()

cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e'}

cluster_names = {0: 'Business', 
                 1: 'R & D', 
                 2: 'Share Market', 
                 3: 'Product', 
                 4: 'Heterogenous'}
                 
#print(len(frame["title"]))
#print(len(frame["cluster"]))

df = pd.DataFrame(dict(x=xs, y=ys, label=frame["cluster"], title=frame['Index'])) 
print(df)

#group by cluster
groups = df.groupby('label')


# set up plot
fig, ax = plt.subplots(figsize=(30, 19)) # set size
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling

##iterate through groups to layer the plot
##note that I use the cluster_name and cluster_color dicts with the 'name' lookup to return the appropriate color/label
for name, group in groups:
    ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, 
            label=cluster_names[name], color=cluster_colors[name], 
            mec='none')
    ax.set_aspect('auto')
    ax.tick_params(\
        axis= 'x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelbottom='off')
    ax.tick_params(\
        axis= 'y',         # changes apply to the y-axis
        which='both',      # both major and minor ticks are affected
        left='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelleft='off')
    
ax.legend(numpoints=1)  #show legend with only 1 point
#
##add label in x,y position with the label as the film title
for i in range(len(df)):
    ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['title'], size=8)  

    
    
plt.show() #show the plot

#class TopToolbar(mpld3.plugins.PluginBase):
#    """Plugin for moving toolbar to top of figure"""
#
#    JAVASCRIPT = """
#    mpld3.register_plugin("toptoolbar", TopToolbar);
#    TopToolbar.prototype = Object.create(mpld3.Plugin.prototype);
#    TopToolbar.prototype.constructor = TopToolbar;
#    function TopToolbar(fig, props){
#        mpld3.Plugin.call(this, fig, props);
#    };
#
#    TopToolbar.prototype.draw = function(){
#      // the toolbar svg doesn't exist
#      // yet, so first draw it
#      this.fig.toolbar.draw();
#
#      // then change the y position to be
#      // at the top of the figure
#      this.fig.toolbar.toolbar.attr("x", 150);
#      this.fig.toolbar.toolbar.attr("y", 400);
#
#      // then remove the draw function,
#      // so that it is not called again
#      this.fig.toolbar.draw = function() {}
#    }
#    """
#    def __init__(self):
#        self.dict_ = {"type": "toptoolbar"}
#df = pd.DataFrame(dict(x=xs, y=ys, label=frame["cluster"], title=frame["title"])) 
#
##group by cluster
#groups = df.groupby('label')
#
##define custom css to format the font and to remove the axis labeling
#css = """
#text.mpld3-text, div.mpld3-tooltip {
#  font-family:Arial, Helvetica, sans-serif;
#}
#
#g.mpld3-xaxis, g.mpld3-yaxis {
#display: none; }
#
#svg.mpld3-figure {
#margin-left: -200px;}
#"""
#
## Plot 
#fig, ax = plt.subplots(figsize=(14,6)) #set plot size
#ax.margins(0.03) # Optional, just adds 5% padding to the autoscaling
#
##iterate through groups to layer the plot
##note that I use the cluster_name and cluster_color dicts with the 'name' lookup to return the appropriate color/label
#for name, group in groups:
#    points = ax.plot(group.x, group.y, marker='o', linestyle='', ms=18, 
#                     label=cluster_names[name], mec='none', 
#                     color=cluster_colors[name])
#    ax.set_aspect('auto')
#    labels = [i for i in group.title]
#    
#    #set tooltip using points, labels and the already defined 'css'
#    tooltip = mpld3.plugins.PointHTMLTooltip(points[0], labels,
#                                       voffset=10, hoffset=10, css=css)
#    #connect tooltip to fig
#    mpld3.plugins.connect(fig, tooltip, TopToolbar())    
#    
#    #set tick marks as blank
#    ax.axes.get_xaxis().set_ticks([])
#    ax.axes.get_yaxis().set_ticks([])
#    
#    #set axis as blank
#    ax.axes.get_xaxis().set_visible(False)
#    ax.axes.get_yaxis().set_visible(False)
#
#    
#ax.legend(numpoints=1) #show legend with only one dot
#
#mpld3.display() #show the plot

#uncomment the below to export to html
#html = mpld3.fig_to_html(fig)
#
#print(html)

#############Hierarchy Clustering##########

from scipy.cluster.hierarchy import ward, dendrogram

linkage_matrix = ward(dist) #define the linkage_matrix using ward clustering pre-computed distances
#print(linkage_matrix)
import sys
#sys.setrecursionlimit(100000000)
#
#fig, ax = plt.subplots(figsize=(150, 200)) # set size
#ax = dendrogram(linkage_matrix, orientation="right", labels=frame["title"]);
###
#plt.tick_params(\
#    axis= 'x',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off')
##
#plt.tight_layout() #show plot with tight layout
##
##uncomment below to save figure
#plt.savefig('C:/Users/harishs/Desktop/ward_clusters.png', dpi=200)



###########LDA##################################

import string
def strip_proppers(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent) if word.islower()]
    return "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
    
from nltk.tag import pos_tag

def strip_proppers_POS(text):
    tagged = pos_tag(text.split()) #use NLTK's part of speech tagger
    non_propernouns = [word for word,pos in tagged if pos != 'NNP' and pos != 'NNPS']
    return non_propernouns
    
from gensim import corpora, models, similarities 

#remove proper names
#titles=x['Title']
preprocess = [strip_proppers(doc) for doc in frame['Articles']]

#tokenize
tokenized_text = [tokenize_and_stem(text) for text in preprocess]

#remove stop words
texts = [[word for word in text if word not in stopwords] for text in tokenized_text]

dictionary = corpora.Dictionary(texts)

#remove extremes (similar to the min/max df step used when creating the tf-idf matrix)
dictionary.filter_extremes(no_below=1, no_above=0.8)

#convert the dictionary to a bag of words corpus for reference
corpus = [dictionary.doc2bow(text) for text in texts]

#print(corpus)

lda = models.ldamulticore.LdaMulticore(corpus, num_topics=5, 
                            id2word=dictionary, workers=3, 
                            chunksize=100,
                            passes=1,iterations = 300)

#lda.show_topics()
#print(lda.get_document_topics(frame['Articles']))
                            
print(lda[corpus])
                            
topics_matrix = lda.show_topics(formatted=False, num_words=1000)
#print(topics_matrix)
topics_matrix=pd.DataFrame(topics_matrix)
topics_matrix.to_csv("C:/Users/harishs/Desktop/lda.csv")
topics_matrix = np.array(topics_matrix)



topic_words = topics_matrix[:,1]
#Firstt=get_topic_terms(0, topn=10)
#print()
for i in range(0,5):
    for j in range(0,100):
        word.append([i,topic_words[i][j]])
word=pd.DataFrame(word)
#for i in frame['Articles']:
#    doc_topic = lda.get_document_topics(i)
#    print(doc_topic)

#for i in range(10):
#    print("{} (top topic: {})".format(doc_topic[i]))
#print(lda.update(x['Title'][1]))

word.to_csv("C:/Users/harishs/Desktop/dic.csv")
   



##############DBSCAN##################
#
#from sklearn.cluster import DBSCAN
#from sklearn import metrics
#
#db = DBSCAN(eps=0.03, min_samples=3).fit(tfidf_matrix)
#
#
#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True
#labels = db.labels_
#labels=pd.DataFrame(labels)
#labels.to_csv("C:/Users/harishs/Desktop/lda.csv")

# Number of clusters in labels, ignoring noise if present.
#n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

#print('Estimated number of clusters: %d' % n_clusters_)

#print("Silhouette Coefficient:",metrics.silhouette_score(tfidf_matrix, labels))