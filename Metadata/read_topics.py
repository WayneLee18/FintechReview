import pandas as pd
import numpy as np


df = pd.read_csv('topic_index.csv',header = None)
df1 = pd.read_csv('metadata.csv')
for topics_index in range(1,9):
    topics_index = int(topics_index)
    ind = df.index[df[1] == topics_index]
    dff = pd.DataFrame(index=range(sum(df[1] == topics_index)), columns=['Title','Authors'])
    for i in range(sum(df[1] == topics_index)):
        title = df1['Title'][df1.index[df1['ID']== df[0][ind[i]]]].iloc[0]
        name = df1['Authors'][df1.index[df1['ID']== df[0][ind[i]]]].iloc[0]
        #print(name)
        dff['Title'][i] = title
        dff['Authors'][i] = name
        
    dff.to_csv(str(topics_index)+'.csv',index=False)
        


    
