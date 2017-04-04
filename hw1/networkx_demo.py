import networkx as nx             
import matplotlib.pyplot as plt 
import sys
import numpy as np
import time
import csv
from multiprocessing import Pool
import time
import itertools
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

def readcat(filename): 
	f = open(filename, 'r')
	mat = [] 
	while True :
		line = f.readline()
		if len(line) == 0:
			break
		results = line.split(",")
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



# def chunks(l, n):
#     """Divide a list of nodes `l` in `n` chunks"""
#     l_c = iter(l)
#     while 1:
#         x = tuple(itertools.islice(l_c, n))
#         if not x:
#             return
#         yield x


# def _betmap(G_normalized_weight_sources_tuple):
#     """Pool for multiprocess only accepts functions with one argument.
#     This function uses a tuple as its only argument. We use a named tuple for
#     python 3 compatibility, and then unpack it when we send it to
#     `betweenness_centrality_source`
#     """
#     return nx.betweenness_centrality_source(*G_normalized_weight_sources_tuple)


# def betweenness_centrality_parallel(G, processes=None):
#     """Parallel betweenness centrality  function"""
#     p = Pool(processes=processes)
#     node_divisor = len(p._pool)*4
#     node_chunks = list(chunks(G.nodes(), int(G.order()/node_divisor)))
#     num_chunks = len(node_chunks)
#     bt_sc = p.map(_betmap,
#                   zip([G]*num_chunks,
#                       [True]*num_chunks,
#                       [None]*num_chunks,
#                       node_chunks))

#     # Reduce the partial solutions
#     bt_c = bt_sc[0]
#     for bt in bt_sc[1:]:
#         for n in bt:
#             bt_c[n] += bt[n]
#     return bt_c

if __name__ == "__main__" :


	myedge = []
	result = []  
	# for filename in sys.argv[1:1+1] : 
	myedge = readfile(sys.argv[1]) 
	DVD = readcat('DVD.csv') 
	Music = readcat('Music.csv') 
	Book = readcat('Book.csv') 
	print('======== All ========')
	G = nx.Graph()                                        
	for i in range (len(myedge)):                                                                 
		G.add_edge(myedge[i][0],myedge[i][1])  
	t0 = time.time()                                  
	print ("number of nodes :%s, time:%s" %(G.number_of_nodes(),time.time() - t0))
	t0 = time.time() 
	print ("number of edges :%s, time:%s" %(G.number_of_edges(),time.time() - t0))
	t0 = time.time() 
	
	# print ("diameter :%s, time:%s" %(nx.diameter(G),time.time() - t0))
	t0 = time.time() 
	print ("network density :%s, time:%s" %(round(nx.density(G),8),time.time() - t0))
	# t0 = time.time() 
	# print ("mean geodesic distance :%s, time:%s" %(nx.average_shortest_path_length(G),time.time() - t0))
	t0 = time.time() 
	print ("assortativity coefficient :%s, time:%s" %(round(nx.degree_assortativity_coefficient(G),4),time.time() - t0))

	t0 = time.time() 
	degrees = G.degree()
	print ('degree time:%s' %(time.time() - t0))
	print ("maximum of degree :%s" %np.amax(degrees.values())) 
	print ("maximum of degree :%s" %np.amin(degrees.values()))
	print ("mean of degree :%s" %round(np.mean(degrees.values()),4))
	
	writefile('degrees.txt',degrees)

	print('======== Book ========')
	Booknodes = []
	for node in Book:
		try:
			G.remove_node(int(node[0]))
			Booknodes.append(int(node[0]))
		except Exception as e:
			pass

	K = nx.Graph()                                        
	for i in range (len(myedge)):                                                                 
		K.add_edge(myedge[i][0],myedge[i][1])  
	H = K.subgraph(Booknodes)	

	t0 = time.time()                                  
	print ("number of nodes :%s, time:%s" %(H.number_of_nodes(),time.time() - t0))
	t0 = time.time() 
	print ("number of edges :%s, time:%s" %(H.number_of_edges(),time.time() - t0))
	t0 = time.time() 
	try:
		print ("diameter :%s, time:%s" %(nx.diameter(G),time.time() - t0))
	except Exception as e:
		print ("diameter :%s, time:%s" %('infinite path length',time.time() - t0))
	t0 = time.time() 
	print ("network density :%s, time:%s" %(round(nx.density(H),8),time.time() - t0))
	t0 = time.time() 
	try:
		print ("mean geodesic distance :%s, time:%s" %(nx.average_shortest_path_length(G),time.time() - t0))
	except Exception as e:
		print ("mean geodesic distance :%s, time:%s" %('infinite path length',time.time() - t0))
	
	t0 = time.time() 
	print ("assortativity coefficient :%s, time:%s" %(round(nx.degree_assortativity_coefficient(H),4),time.time() - t0))

	t0 = time.time() 
	degrees = H.degree()
	print ('degree time:%s' %(time.time() - t0))
	print ("maximum of degree :%s" %np.amax(degrees.values())) 
	print ("maximum of degree :%s" %np.amin(degrees.values()))
	print ("mean of degree :%s" %round(np.mean(degrees.values()),4))
	
	writefile('degreesBook.txt',degrees)

	t0 = time.time() 
	clustering = nx.clustering(H)
	print ('clustering time:%s' %(time.time() - t0))
	print ("maximum of clustering :%s" %round(np.amax(clustering.values()),4)) 
	print ("minimum of clustering :%s" %round(np.amin(clustering.values()),4))
	print ("mean of clustering:%s" %round(np.mean(clustering.values()),4))
	writefile('clusteringBook.txt',clustering)

	print('======== Music ========')
	Musicnodes = []
	for node in Music:
		try:
			G.remove_node(int(node[0]))
			Musicnodes.append(int(node[0]))
		except Exception as e:
			pass

	K = nx.Graph()                                        
	for i in range (len(myedge)):                                                                 
		K.add_edge(myedge[i][0],myedge[i][1])  
	H = K.subgraph(Musicnodes)	

	t0 = time.time()                                  
	print ("number of nodes :%s, time:%s" %(H.number_of_nodes(),time.time() - t0))
	t0 = time.time() 
	print ("number of edges :%s, time:%s" %(H.number_of_edges(),time.time() - t0))
	t0 = time.time() 
	try:
		print ("diameter :%s, time:%s" %(nx.diameter(G),time.time() - t0))
	except Exception as e:
		print ("diameter :%s, time:%s" %('infinite path length',time.time() - t0))
	t0 = time.time() 
	print ("network density :%s, time:%s" %(round(nx.density(H),8),time.time() - t0))
	t0 = time.time() 
	try:
		print ("mean geodesic distance :%s, time:%s" %(nx.average_shortest_path_length(G),time.time() - t0))
	except Exception as e:
		print ("mean geodesic distance :%s, time:%s" %('infinite path length',time.time() - t0))
	
	t0 = time.time() 
	print ("assortativity coefficient :%s, time:%s" %(round(nx.degree_assortativity_coefficient(H),4),time.time() - t0))

	t0 = time.time() 
	degrees = H.degree()
	print ('degree time:%s' %(time.time() - t0))
	print ("maximum of degree :%s" %np.amax(degrees.values())) 
	print ("maximum of degree :%s" %np.amin(degrees.values()))
	print ("mean of degree :%s" %round(np.mean(degrees.values()),4))
	
	writefile('degreesMusic.txt',degrees)

	t0 = time.time() 
	betweenness =  nx.betweenness_centrality(H)
	print ('betweenness time:%s' %(time.time() - t0))
	print ("maximum of betweenness :%s" %round(np.amax(betweenness.values()),4)) 
	print ("minimum of betweenness :%s" %round(np.amin(betweenness.values()),4))
	print ("mean of betweenness:%s" %round(np.mean(betweenness.values()),4))
	writefile('betweennessMusic.txt',betweenness)

	t0 = time.time() 
	closeness = nx.closeness_centrality(H)
	print ('betweenness time:%s' %(time.time() - t0))
	print ("maximum of closeness :%s" %round(np.amax(closeness.values()),4)) 
	print ("minimum of closeness :%s" %round(np.amin(closeness.values()),4))
	print ("mean of closeness:%s" %round(np.mean(closeness.values()),4))
	writefile('closenessMusic.txt',closeness)

	t0 = time.time() 
	eigenvector = nx.eigenvector_centrality(H)
	print ('eigenvector time:%s' %(time.time() - t0))
	print ("maximum of eigenvector :%s" %round(np.amax(eigenvector.values()),4)) 
	print ("minimum of eigenvector :%s" %round(np.amin(eigenvector.values()),4))
	print ("mean of eigenvector:%s" %round(np.mean(eigenvector.values()),4))
	writefile('eigenvectorMusic.txt',eigenvector)

	t0 = time.time() 
	clustering = nx.clustering(H)
	print ('clustering time:%s' %(time.time() - t0))
	print ("maximum of clustering :%s" %round(np.amax(clustering.values()),4)) 
	print ("minimum of clustering :%s" %round(np.amin(clustering.values()),4))
	print ("mean of clustering:%s" %round(np.mean(clustering.values()),4))
	writefile('clusteringMusic.txt',clustering)


	print('======== DVD ========')
	DVDnodes = []
	for node in DVD:
		try:
			G.remove_node(int(node[0]))
			DVDnodes.append(int(node[0]))
		except Exception as e:
			pass

	K = nx.Graph()                                        
	for i in range (len(myedge)):                                                                 
		K.add_edge(myedge[i][0],myedge[i][1])  
	H = K.subgraph(DVDnodes)	

	t0 = time.time()                                  
	print ("number of nodes :%s, time:%s" %(H.number_of_nodes(),time.time() - t0))
	t0 = time.time() 
	print ("number of edges :%s, time:%s" %(H.number_of_edges(),time.time() - t0))
	t0 = time.time() 
	try:
		print ("diameter :%s, time:%s" %(nx.diameter(G),time.time() - t0))
	except Exception as e:
		print ("diameter :%s, time:%s" %('infinite path length',time.time() - t0))
	t0 = time.time() 
	print ("network density :%s, time:%s" %(round(nx.density(H),8),time.time() - t0))
	t0 = time.time() 
	try:
		print ("mean geodesic distance :%s, time:%s" %(nx.average_shortest_path_length(G),time.time() - t0))
	except Exception as e:
		print ("mean geodesic distance :%s, time:%s" %('infinite path length',time.time() - t0))
	
	t0 = time.time() 
	print ("assortativity coefficient :%s, time:%s" %(round(nx.degree_assortativity_coefficient(H),4),time.time() - t0))

	t0 = time.time() 
	degrees = H.degree()
	print ('degree time:%s' %(time.time() - t0))
	print ("maximum of degree :%s" %np.amax(degrees.values())) 
	print ("maximum of degree :%s" %np.amin(degrees.values()))
	print ("mean of degree :%s" %round(np.mean(degrees.values()),4))
	
	writefile('degreesDVD.txt',degrees)

	t0 = time.time() 
	betweenness =  nx.betweenness_centrality(H)
	print ('betweenness time:%s' %(time.time() - t0))
	print ("maximum of betweenness :%s" %round(np.amax(betweenness.values()),4)) 
	print ("minimum of betweenness :%s" %round(np.amin(betweenness.values()),4))
	print ("mean of betweenness:%s" %round(np.mean(betweenness.values()),4))
	writefile('betweennessDVD.txt',betweenness)

	t0 = time.time() 
	closeness = nx.closeness_centrality(H)
	print ('betweenness time:%s' %(time.time() - t0))
	print ("maximum of closeness :%s" %round(np.amax(closeness.values()),4)) 
	print ("minimum of closeness :%s" %round(np.amin(closeness.values()),4))
	print ("mean of closeness:%s" %round(np.mean(closeness.values()),4))
	writefile('closenessDVD.txt',closeness)

	t0 = time.time() 
	eigenvector = nx.eigenvector_centrality(H)
	print ('eigenvector time:%s' %(time.time() - t0))
	print ("maximum of eigenvector :%s" %round(np.amax(eigenvector.values()),4)) 
	print ("minimum of eigenvector :%s" %round(np.amin(eigenvector.values()),4))
	print ("mean of eigenvector:%s" %round(np.mean(eigenvector.values()),4))
	writefile('eigenvectorDVD.txt',eigenvector)

	t0 = time.time() 
	clustering = nx.clustering(H)
	print ('clustering time:%s' %(time.time() - t0))
	print ("maximum of clustering :%s" %round(np.amax(clustering.values()),4)) 
	print ("minimum of clustering :%s" %round(np.amin(clustering.values()),4))
	print ("mean of clustering:%s" %round(np.mean(clustering.values()),4))
	writefile('clusteringDVD.txt',clustering)



