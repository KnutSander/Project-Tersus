# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:19:13 2020

@author: ArifM
"""
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from CC.models import Employee
from CC.models import RiskGroup


# Need to store the file with the models py file and table definition
from .getTimesWashed import *


# Will encode centroids onto their correct mapping
# High = 2
# Med = 1
# Low = 0
# Worked with testing. Might need integration testing
# Returns the array back in correct label
def LabelEncoding(labels, centroids_y):
    C_copy = centroids_y.copy()
    HMLindex = [0, 0, 0]
    
    low = 99999
    high = 0
    for i in centroids_y:
        if i < low:
            low = i
        HMLindex[2] = centroids_y.index(low)
    
    C_copy.remove(low)
    
    for i in centroids_y:
        if i > high:
            high = i
        HMLindex[0] = centroids_y.index(high)
    C_copy.remove(high)
    
    HMLindex[1] = centroids_y.index(C_copy[0])
    
    
    
    for i in range(len(labels)):
        if labels[i] == HMLindex[0]:
            labels[i] = 2
        elif labels[i] == HMLindex[1]:
            labels[i] = 1
        elif labels[i] == HMLindex[2]:
            labels[i] = 0
    
    return labels


# Returns an array with labelled data
def Clustering():
    timesWashed = getTimesWashed()
    # Should return dictionary that results in proper clustering analysis
    
    IDs = list(timesWashed.keys())
    Count = list(timesWashed.values())    

    # This is how the dictionary MUST BE DISPLAYED,
    # COLUMNS TITLES MUST BE SPECIFIED LIKE SO

    # Input Data goes here as pandas dataframe
    # InputData = pd.read_csv('out.csv')
    InputData = pd.DataFrame()
    InputData['EmployeeID'] = IDs
    InputData['Count'] = Count
    
    X = InputData.to_numpy()
    # Explain difference between numpyarray and dataframe to other fellas
    
    kmeans = KMeans(n_clusters=3, random_state=9042001)
    kmeans.fit(X)

    # Centre markers of the clusters, will be two in this case.
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    labelColumn = np.hstack(labels)
    
    Output = pd.DataFrame(X)
    Output['Labels'] = labels
    
    Output = Output.drop(columns=[1], axis=1)
    OutArray = []
    
    # centroid array is just a list containing the values of the y locations of centroids
    centroidArray = list(centroids[:, 1])

    # Label encoding ensures that
    # High centroid = 2
    # Med centroid = 1
    # Low centroid = 0
    labels = LabelEncoding(labels, centroidArray)
    # Save risk group data
    for row in Output.itertuples(index=False):
        employee = Employee.objects.get(uid=row[0])
        riskIDAdjust = RiskGroup.objects.all()[0].id
        employee.risk_group = RiskGroup.objects.get(id=(row[1]+riskIDAdjust))
        employee.save()

    OutArray = [list(Output[0]), list(Output['Labels'])]
    return OutArray

# Outputs to dataframe here, take output from here
# Output here is the correct functioning output, use this output
