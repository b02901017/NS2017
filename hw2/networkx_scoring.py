import matplotlib.pyplot as plt 
import matplotlib.colors as colors
import sys
import numpy as np
import time
import csv
import time
import itertools
import networkx as nx
import community
import random
from scoringfunction import internal_density, edges_inside, expansion, cut_ratio, TPR, numofcommunities

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
    G = nx.read_gml(sys.argv[1]+".gml")
    # myedge = readfile(sys.argv[1]) #for facebook
    # G = nx.Graph()                                        
    # for i in range (len(myedge)):                                                                 
	# 	G.add_edge(myedge[i][0],myedge[i][1]) 
    t0 = time.time()                                  
    print ("number of nodes :%s, time:%s" %(G.number_of_nodes(),time.time() - t0))
    t0 = time.time() 
    print ("number of edges :%s, time:%s" %(G.number_of_edges(),time.time() - t0))
    method = ["Louvain"] 
    for i in range(len(method)):
        partition = readpart(sys.argv[1]+"_%s.txt" %method[i])
        print ("======= %s =======" %method[i])
        t0 = time.time()
        print ("internal density :%s" %internal_density(G,partition))
        t0 = time.time()
        print ("edges inside :%s" %edges_inside(G,partition))
        t0 = time.time()
        print ("TPR :%s"%TPR(G,partition))
        t0 = time.time()
        print ("expansion :%s" %expansion(G,partition))
        t0 = time.time()
        print ("cut ratio :%s" %cut_ratio(G,partition))
        t0 = time.time()
        print ("modularity :%s" %community.modularity(partition, G))
        print ("commnity :%s" %numofcommunities(partition))
