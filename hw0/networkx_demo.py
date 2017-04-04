import networkx as nx             
import matplotlib.pyplot as plt 
import sys
import numpy as np

def readfile(filename): 
	f = open(filename, 'r')
	mat = [] 
	while True :
		line = f.readline()
		if len(line) == 0 :
			break
		results = map(int, line.split(" "))
		mat.append(results)
	f.close()
	return mat






if __name__ == "__main__" :

	if len(sys.argv) != 2: 
		print ('You have to check your argument')
		sys.exit()
	else:
		myedge = []
		result = []  
		for filename in sys.argv[1:1+1] : 
			myedge = readfile(filename) 
		# print (myedge)
		G = nx.Graph()                                        
		for i in range (len(myedge)):                                                                 
			G.add_edge(myedge[i][0],myedge[i][1])                                    
		print ("number of nodes:%s" %G.number_of_nodes())
		print ("number of edges:%s\n" %G.number_of_edges())
		print ("average clustering:%s" %nx.average_clustering(G) )
		print ("is bipartite:%s" %nx.is_bipartite(G) )
		nodes = G.nodes()
		path=nx.all_pairs_shortest_path(G)
		print ("path from %s to %s:%s:\n" %(nodes[0],nodes[1],path[nodes[0]][nodes[1]]))
		pos = nx.shell_layout(G) 
		#d = nx.degree(G)
		
		b = nx.betweenness_centrality(G)
		c = nx.closeness_centrality(G)
		d = nx.degree(G)
		print ("betweenness centrality:%s" %np.mean(b.values()))
		print ("closeness centrality:%s" %np.mean(c.values()))
		print ("degree:%s" %np.mean(d.values()))
		
		nx.draw_spring(G,nodelist=b.keys(), node_size=[30*v/np.mean(b.values()) for v in b.values()])
		# graphviz, shell, circular, spectral, spring
		# nx.draw(G,pos,with_labels=False,node_size = 30) 
		plt.show()
		# pos = nx.shell_layout(G) 
		# nx.draw(G,pos,with_labels=False,node_size = 30) 
		# plt.show() 
