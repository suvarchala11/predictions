# -*- coding: utf-8 -*-
"""predictions

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vTQdf1VnJQMB8fYpbBs4MDQom93IUlmv
"""

from sklearn import tree
features = [[23,3],[24,4],[80,12],[90,15]]
labels = ['0','0','1','1']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print(clf.predict([[75,14]]))