import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from xml.dom.minidom import parse
from xml.dom import minidom
DOMTree=parse("go_obo.xml")
collection=DOMTree.documentElement # get the root element of the document
terms=collection.getElementsByTagName('term') # a list of 'term' elements;Returns the matching element nodes and their children's NodeList。
n=0
for i in terms: # count the term element
    n=n+1
print('the total number of terms is '+str(n))
dic = {}
result = {}
all_list = []
trans_list=[]
judge=[] # judge is used to store the data of whether "translation" is exist

def find_parents(node_id, parent_ids): # def a function to find all child note and immediae parent node
    is_as = dic[node_id]
    if len(is_as):
        for all_id in is_as:
            parent_ids.add(all_id)
            find_parents(all_id, parent_ids)
# find the translation related nodes
# the is_a represent a subclass = the child node of current node
for node in terms:
    id = node.getElementsByTagName("id")[0].childNodes[0].data
    is_as = []
    defstr=node.getElementsByTagName("defstr")[0].childNodes[0].data
    for is_a in node.getElementsByTagName("is_a"):
        is_as.append(is_a.childNodes[0].data) # store the child nodes in is_as
    dic[id] = is_as
    if defstr.find("translation") !=-1 :
        judge.append(1)
    else:
        judge.append(0)
    result[id] = 0
# count the child note of terms
for key in dic.keys():
    parent_ids = set()
    find_parents(key, parent_ids)
    for parent_id in parent_ids:
        result[parent_id] += 1
# creat lists to select value of all and trans term from result
for i, (key,value) in enumerate(result.items()):
    all_list.append(value)
    if judge[i]==1:
        trans_list.append(value)
#draw the boxplot of the distribution of child nodes across terms related to translation
plt.boxplot(result.values(), vert=True, showmeans=True)
plt.title('Distribution of child node number of all GO terms')
plt.xlabel("all GO terms")
plt.ylabel("Number of Child nodes")
plt.show()
#draw the boxplot of the distribution of chaild nodes across all terms
plt.boxplot(trans_list, vert=True, showmeans=True)
plt.title('Distribution of child node number of translation related terms ')
plt.xlabel("Translation related term")
plt.ylabel("Number of Child nodes")
plt.show()
#compare the average of trans and all
avg_trans=sum(trans_list)/len(trans_list)
avg_all=sum(all_list)/len(all_list)
print("the average number of childnote in overall GO is "+str(avg_all))
print("the average number of childnote in translation term is "+str(avg_trans))
# print the comment
if avg_trans<avg_all:
	print("the translation terms contain, on average, a smaller number of child nodes than the overall Gene Ontology")
elif avg_trans>avg_all:
	print("the translation terms contain, on average, a greater number of child nodes than the overall Gene Ontology")
else:
	print ("They contain an equal number of average child nodes")
