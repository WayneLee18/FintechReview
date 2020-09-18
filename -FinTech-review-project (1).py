#!/usr/bin/env python
# coding: utf-8

# In[20]:


#INSTALL PyPDF2 library

get_ipython().run_line_magic('pip', 'install PyPDF2')


# In[21]:


# merge the pdfs


    
from PyPDF2 import PdfFileMerger

pdfs = ['fintech.pdf', 'fintechreview.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

a=merger.write("result.pdf")
merger.close()


# In[22]:


# count the number of pages in the merged pdf
import PyPDF2

# pdf file object

pdfFileObj = open('result.pdf', 'rb')

# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# number of pages in pdf
print ('the number of pages in this merged pdf is:')
print(pdfReader.numPages)


# In[23]:



#  EXTRACT  text from a specific page of the merged  pdfs in this example from the first page

import PyPDF2

pdfFileObj = open('result.pdf', 'rb')

# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)



def text_of_page(k):
    # k page object
    pageObj = pdfReader.getPage(k)
    
    # this will print the text and remove \n and replace by single space
    
    content_content=pageObj.extractText().replace('\n', "")
    return content_content

print('content of the page requested is')

text_of_page(2)


# In[24]:


# to extract all text of the merged  pdfs

import PyPDF2

pdfFileObject = open('result.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
a =[]
count = pdfReader.numPages

for i in range(count):
    page = pdfReader.getPage(i)
    Report=page.extractText()
    a.append(Report)
Report='\n'.join(a)
print(Report)


# In[25]:


#lengh of the text

print(len(Report))


# In[26]:


# Cleaning text, lower casing all words

for char in '!"#$%&\'()*+,/:;<=>?@[\\]^`{|}~ \n':
    Report=Report.replace(char,' ')
    Report = Report.lower()
    print(Report)


# In[27]:


# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s) 

Report_split=Report.split()
print (Report_split)


# In[28]:


#lengh of the splitted and cleaned text

print(len(Report_split))


# In[29]:


#Output a List of the 50th most common words (Sorted from Highest to Lowest)

from collections import Counter
Counter(Report_split).most_common(50)


# In[30]:


# Initializing Dictionary (in case you wnat to work with it)

d = {}

# counting number of times each word comes up in list of words (in dictionary)
for word in Report_split: 
    d[word] = d.get(word, 0) + 1

    
word_freq = []
for key, value in d.items():
    word_freq.append((value, key))
    
    
word_freq.sort(reverse=True) 
print(word_freq)


# In[31]:



# COUNT THE OCCURENCE OF A   SPECIFIC WORD (if you enter a work not in teh ext it gives error message, 
#you can edit the code to get a message instead
# thsi can be simplified by making a function
# or maybe splitting words except for certian words: artificial intelligence, machine learning

wordcount= {}
for word in Report.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1


my_word1="fintech"

print (my_word1, wordcount[my_word1])


# In[39]:


# This is easier one you can type the words you want in keyw

keywords = ['fintech', 'blockchain','crowdfunding','innovation']
worddict = {}


for word in Report_split:
    worddict[word] = worddict[word]+1 if word in worddict else 1
print([{x, worddict[x]} for x in keywords])


# In[40]:


ahmad=[{x, worddict[x]} for x in keywords]
print (ahmad)


# In[45]:


import numpy as np
import pandas as pd

#index=['keyword1','keyword2']
df = pd.DataFrame(ahmad,columns=['values','keywords'])

print(df)


# In[59]:


import matplotlib.pyplot as plt


df.plot(x='keywords', y='values',kind='bar',color='R',title='count occurency of the keywords')


# In[62]:


import pandas as pd
import matplotlib.pyplot as plt


#Set descriptions:



#ax = plt.gca()

ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='green')


#Plot the data:
my_colors = 'red','Blue'  #'rgbkymc'red, green, blue, black, etc.

df.plot(
    x='keywords', 
    y='values', 
    kind='bar', 
    color=my_colors,
    title= 'count occurency of the keywords'
)

plt.show()

