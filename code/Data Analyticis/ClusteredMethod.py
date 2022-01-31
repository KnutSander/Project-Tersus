 # -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:19:13 2020

@author: ArifM
"""
#Need to store the file with the models py file and table definition
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

timesWashed = FUNCTION_THAT_RETURNS_DICTIONARY()


IDs = list(timesWashed.keys())
Count = list(timesWashed.values())    
    
    
#This is how the dictionary MUST BE DISPLAYED, 
#COLUMNS TITLES MUST BE SPECIFIED LIKE SO


#Input Data goes here as pandas dataframe
#InputData = pd.read_csv('out.csv') 
InputData = pd.DataFrame()
InputData['EmployeeID'] = IDs
InputData['Count'] = Count

X = InputData.to_numpy()
#Explain difference between numpyarray and dataframe to other fellas

kmeans = KMeans(n_clusters = 3)
kmeans.fit(X)


#Centre markers of the clusters, will be two in this case.
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

labelColumn = np.hstack(labels)

Output = pd.DataFrame(X)
Output['Labels'] = labels

Output = Output.drop(columns=[1],axis=1)

#Outputs to dataframe here, take output from here
#Output here is the correct functioning output, use this output


