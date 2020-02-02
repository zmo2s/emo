import praw
import re
import requests
import random
from requests_html import HTMLSession

from bs4 import BeautifulSoup as BSHTML
import urllib.request
reddit = praw.Reddit(client_id='pJHcuxpiL64Rhg',
                     client_secret='MkjdzRQk55mIRqOBnpS2Nwuwsqk',
                     user_agent='my user agent')



response3=""
o=""
i=0
e=""
list = []
v = random.randint(0, 20)
for submission in reddit.subreddit('animereactionimages').hot(limit=1000):
    if i < 30 :
      list.append(submission.url)
 
#print(list)


def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  



import praw
import re
import requests
import random
from requests_html import HTMLSession

from bs4 import BeautifulSoup as BSHTML
import urllib.request
reddit = praw.Reddit(client_id='pJHcuxpiL64Rhg',
                     client_secret='MkjdzRQk55mIRqOBnpS2Nwuwsqk',
                     user_agent='my user agent')



response3=""
o=""
i=0
e=""
list = []
v = random.randint(0, 20)
for submission in reddit.subreddit('animereactionimages').hot(limit=1000):
    if i < 30 :
      list.append(submission.url)
 
#print(list)


def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  



p=0
list2 = []
j = random.randint(0, 100)
for cle in list :

 if cle.endswith('.jpg') or cle.endswith('.png') or cle.endswith('.gif'):
  if p==j : 
   o=o+" "+cle
 p+=1
print(o)
  

