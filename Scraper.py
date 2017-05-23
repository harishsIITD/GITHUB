# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory



# Any results you write to the current directory are saved as output.

import re
import requests
from collections import OrderedDict
from bs4 import BeautifulSoup
from newspaper import *
import pandas as pd
from  tkinter import *
import logging
logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.ERROR)
global keyword1,keyword2
global news1,href1,ntitle1,ndt1,news2,href2,ntitle2,ndt2,notscraped
news1=[]
href1=[]

ntitle1=[]
ndt1=[]

news2=[]
href2=[]

ntitle2=[]
ndt2=[]
notscraped=[]

fontsize = {}
fontsize['Headline']    = 24
fontsize['Description'] = 18
fontsize['URL']         = 12
fontsize['Date']        = 12
fontsize['Navigation']  = 14


config = {}

config['mode']                     = "gui"
config['progname']                 = "NewsFeed"
config['refresh_every']            = 30		# Refresh interval in minutes
config['maxtime']                  = 30		# Maximum time (in days) to keep items

# Program default values that get saved automatically if changed:
config['geom_root']                = "900x600"  # Default
config['geom_info']                = "675x380"  #         window
config['geom_search']              = "350x200"  #                sizes
config['search_is_case_sensitive'] = 0          # Make new searches case sensitive?
config['search_match_whole_words'] = 0          # Match only entire words in searches?
config['search_only_unread']       = 0          # Search only in unread entries?
config['widescreen']               = False	# Widescreen view?



def bloombergcrawl(maxpage,keyword1):
    page=1 ##Start Page
    
    print(maxpage,keyword1)
    global news1,href1,ntitle1,ndt1,notscraped,notscraped
    
    while page <= maxpage:
        url='http://www.bloomberg.com/search?query='+ str(keyword1) +'&page='+str(page)
        #print(url)
        sourcecode = requests.get(url)
        plane_text= sourcecode.text
        soup= BeautifulSoup(plane_text,'lxml')
        
        for link in soup.findAll('a'):
            href=link.get('href')
            href1.append(href)
            href1=list(href1)
            #print(href1)
        page += 1
        
    href1=list(OrderedDict.fromkeys(href1))
    #print(href1)    
    for i in href1:
        
        if re.search('http://www.bloomberg.com/news/articles/', i):
            
            try:
                article1 = Article(i)
                article1.download()
                article1.parse()
                txt1=article1.text
                dt1=article1.publish_date
                tit1=article1.title
                news1.append(txt1)
            #summary1.append(sum1)
                ntitle1.append(tit1)
                ndt1.append(dt1)
            except ArticleException:
                print("ArticleException on url {}".format(i))
                notscraped.append(i)
                
            #print(i)
#            article1 = Article(i)
#            article1.download()
#            time.sleep(2)
            #print(article1.download())
#            article1.parse()
#            txt1=article1.text
#            dt1=article1.publish_date
#            tit1=article1.title
#            article1.nlp()
#            sum1=article1.summary
            
            
            #print(article1.summary)
            
            #print(article1.keywords)
    print("length:",len(news1))                     
    news1=[ndt1,ntitle1,news1]    
    news1=pd.DataFrame(news1)
    news1=news1.transpose()
    notscraped=pd.DataFrame(notscraped)
    #print("length:",len(news1))
    #print(news1)
    news1.columns = ['Date & Time', 'Title','NewsFeed']
    news1.to_csv("C:/Users/saragada/Desktop/GITHUB/news1.csv",index = False)
    notscraped.to_csv("C:/Users/saragada/Desktop/GITHUB/notscraped.csv")

def Thomasreuters(keyword2):
    
    global news2,href2,ntitle2,ndt2
    
    #url='http://www.reuters.com/search/news?blob=apple'
    url='http://www.reuters.com/search/news?blob='+str(keyword2)+'&sortBy=date&dateRange=pastMonth'
    print(url)
    sourcecode = requests.get(url)
    sourcecode = requests.get(url)
    plane_text= sourcecode.text
    soup= BeautifulSoup(plane_text,'lxml')
    for link in soup.findAll('a'):
        href=link.get('href')
        href2.append(href)
        href2=list(href2)
        
    href2=list(OrderedDict.fromkeys(href2))
    
    
    for j in href2:
        
        if re.search("/article/", j):
            print(j)
            
            j="http://www.reuters.com"+str(j)
            article2 = Article(j)
            article2.download()
            article2.parse()
            txt2=article2.text
            dt2=article2.publish_date
            tit2=article2.title
            
            print(txt2)
            news2.append(txt2)
            ntitle2.append(tit2)
            ndt2.append(dt2)
    
                         
    news2=[ndt2,ntitle2,news2]    
    news2=pd.DataFrame(news2)
    news2=news2.transpose()
    news2.columns = ['Date & Time', 'Title','NewsFeed']
    news2.to_csv("C:/Users/saragada/Desktop/GITHUB/news2.csv",index = False)
    

#class TkApp():
#    def __init__(s, parent):
#        global keyword3
        
bloombergcrawl(30,"apple")
#Thomasreuters("apple") 



#
#root=Tk()
#root.title(config['progname'])
#root.geometry(config['geom_root'])
#
#app = TkApp(root)
##app.change_content()
#root.protocol("WM_DELETE_WINDOW", quit)
#root.iconname(config['progname'])
#
#root.mainloop()    
    


     

