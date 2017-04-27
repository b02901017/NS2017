from graph_tool.all import *
import networkx as nx
import time
import community
import sys
from scoringfunction import drawpart, internal_density, edges_inside, expansion, cut_ratio, TPR, numofcommunities

dataset = [ "lesmis", "polbooks", "netscience", "facebook_combined","as-22july06"]


for i in range(i):

    G = nx.Graph()   
    G_gt = Graph(directed=False)                         
    print(dataset[i])
    print(time.time() - t0)     
    for v in G_gt.vertices():
        G.add_node(v) 
    for e in G_gt.edges():                                                                
        G.add_edge(e.source(),e.target()) 
    partition = {}
    for j in range (len(com)):
        partition[j]= com[j]
    drawpart(G,partition, "./data/"+dataset[i]+"/"+dataset[i]+"_gt.png")
    print ("number of nodes :%s" %G.number_of_nodes())
    print ("number of edges :%s" %G.number_of_edges())
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