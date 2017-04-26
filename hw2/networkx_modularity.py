import matplotlib.pyplot as plt 

import sys
import numpy as np
import time
import csv
import time
import itertools
import networkx as nx
import community
import random
import girvan_newman
from scoringfunction import drawpart
def readfile(filename): 
	f = open(filename, 'r')
	mat = [] 
	while True :
		line = f.readline()
		if len(line) == 0:
			break
		results = map(int, line.split(" "))
		mat.append(results)
	f.close()
	return mat
def writefile(filename, data) :
    f = open(filename,"w")
    w = csv.writer(f)
    keys = data.keys()
    values = data.values()
    for i in range (len(data)):
        w.writerow([keys[i],values[i]])
    f.close()
def readpart(filename) :
    data = {}
    with open(filename) as file :
        spamreader = csv.reader(file)
        for row in spamreader:
            # data[int(row[0])]= int(row[1]) #for facebook
            data[(row[0])]= row[1] 
        return data
if __name__ == "__main__" :
    # G = nx.read_gml(sys.argv[1])
    myedge = readfile(sys.argv[1]) 
    G = nx.Graph()                                        
    for i in range (len(myedge)):                                                                 
		G.add_edge(myedge[i][0],myedge[i][1])  
    t0 = time.time()                                  
    print ("number of nodes :%s, time:%s" %(G.number_of_nodes(),time.time() - t0))
    t0 = time.time() 
    print ("number of edges :%s, time:%s" %(G.number_of_edges(),time.time() - t0))
    t0 = time.time() 
    partition = community.best_partition(G)
    print ("modularity(Louvain) :%s, time:%s" %(community.modularity(partition, G),time.time() - t0))
    writefile (sys.argv[1][:len(sys.argv[1])-4]+'_Louvain.txt',partition)
    # #drawing
    # drawpart(G,partition, (sys.argv[1][:len(sys.argv[1])-4]+'_Louvain.png'))

    t0 = time.time() 
    partition = girvan_newman.girvan_newman(G)
    partition = tuple(sorted(p) for p in next(partition))
    temp = {}
    for i in range(len(partition)):
        for j in range(len(partition[i])):
            temp[partition[i][j]] = i
    partition = temp
    writefile (sys.argv[1][:len(sys.argv[1])-4]+'_girvan_newman.txt',partition)
    print ("modularity(girvan_newman) :%s, time:%s" %(community.modularity(partition, G),time.time() - t0))
    drawpart(G,partition, (sys.argv[1][:len(sys.argv[1])-4]+'_girvan_newman.png'))
    #drawing

	