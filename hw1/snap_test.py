from snap import * 
import sys
import numpy as np
import time
import csv

def readfile(filename): 
	f = open(filename, 'r')
	mat = [] 
	while True :
		line = f.readline()
		if len(line) == 0:
			break
		if line.startswith('#'):
			continue
		results = map(int, line.split("	"))
		mat.append(results)
	f.close()
	return mat


def writefile(filename, data) :
	f = open(filename,"w")
	w = csv.writer(f)
	w.writerows(data)
	f.close()



if __name__ == "__main__" :

	myedge = []
	result = []  
	myedge = readfile(sys.argv[1]) 
	mynode = np.unique(myedge)
	G = TUNGraph.New()     
	for i in range (len(mynode)):   
		G.AddNode(mynode[i])                                                              
	for i in range (len(myedge)):                                                                 
		G.AddEdge(myedge[i][0],myedge[i][1])  

	t0 = time.time()                                  
	print ("number of nodes :%s, time:%s" %(G.GetNodes(),time.time() - t0))
	t0 = time.time() 
	print ("number of edges :%s, time:%s" %(G.GetEdges(),time.time() - t0))
	t0 = time.time()
	Degree = []
	result_degree = TIntV()
	GetDegSeqV(G, result_degree)
	for i in range(result_degree.Len()):
		Degree.append([i, result_degree[i]])
	print ("Degree, time:%s" %(time.time() - t0))
	writefile('Degree.csv',Degree)
	Degree.sort(key=lambda x: x[1])
	
	G.DelNode(Degree[0][0])

	t0 = time.time()
	Nodes = TIntFltH()
	Edges = TIntPrFltH()
	GetBetweennessCentr(G, Nodes, Edges, 1.0)
	Betweenness = []
	for node in Nodes:
		Betweenness.append([node, Nodes[node]])
	print ("Betweenness, time:%s" %(time.time() - t0))
	writefile('Betweenness.csv',Betweenness)

	t0 = time.time()
	Closeness = []
	for NI in G.Nodes():
		CloseCentr = GetClosenessCentr(G, NI.GetId())
		Closeness.append([NI.GetId(), CloseCentr])
	print ("Betweenness, time:%s" %(time.time() - t0))
	writefile('Closeness.csv',Closeness)

	t0 = time.time()
	Pagerank = []
	PRankH = TIntFltH()
	GetPageRank(G, PRankH)
	for item in PRankH:
		Pagerank.append([item, item, PRankH[item]]) 
	print ("Pagerank, time:%s" %(time.time() - t0))
	writefile('Pagerank.csv',Pagerank)


	