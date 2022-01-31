# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:26:10 2020

@author: ArifM
"""

import sklearn.datasets as f
import matplotlib as plt


x = f.make_classification(n_samples=100,n_features=6,n_informative=2,n_redundant=0,n_classes=2,n_clusters_per_class=2)

plt.pyplot.scatter(x[0])
plt.pyplot.show()
