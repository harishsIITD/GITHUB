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
import os
import sys
import csv



files = os.listdir('C:/Users/saragada/Desktop/Sec/Razmandi, Mark - secAnalytics/EDGAR_10X_S_2016')
#files=['1029800','1031896']
#files=['1029800']
import re
p=[]
itemlist=pd.DataFrame()
item1=[]
item2=[]
index=[]
infiles=[]
finalist1= pd.DataFrame()
list_=[]
list2=[]
finalist2=pd.DataFrame()
for i in files:
    m = os.listdir('C:/Users/saragada/Desktop/Sec/Razmandi, Mark - secAnalytics/EDGAR_10X_S_2016/'+str(i))
    #print(m)
    datad='a'
    for j in m:
        
        if re.search('item1.txt|item1_1.txt|item1[a-z].txt|item1[a-z]_1.txt',j):
            
            c='C:/Users/saragada/Desktop/Sec/Razmandi, Mark - secAnalytics/EDGAR_10X_S_2016/'+str(i)+'/'+str(j)
            infiles.append(c)
            
            
            
    with open('C:/Users/saragada/Desktop/Sec/Item1 outputs/outfile'+str(i)+'.txt', 'w') as f:
        for file in infiles:
            with open(file) as infile:
                f.write(infile.read()+'\n')
            #datad=''.join(line.rstrip() for line in datad1)
            #del datad1
            #print(datad)
#            datads=datad
#    item2.append(datads)
    index.append(i)
    finallist=open('C:/Users/saragada/Desktop/Sec/Item1 outputs/outfile'+str(i)+'.txt')
    #finallist=finallist.read()
    list_.append(finallist.read())
    lis2='C:/Users/saragada/Desktop/Sec/Item1 outputs/outfile'+str(i)+'.txt'
    list2.append(lis2)
finalist1['index']=index
finalist1['Text']=list_
         
finalist2['cik']=index
finalist2['Text']=list2



#itemlist=pd.DataFrame(finalist1)
finalist1.to_csv('Item1list.txt')
finalist2.to_csv('Item1list2.csv')
