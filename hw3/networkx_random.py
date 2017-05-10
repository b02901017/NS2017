import matplotlib.pyplot as plt 
import sys
import numpy as np
import time
import csv
import time
import networkx as nx
import plfit
from networkx.utils import powerlaw_sequence, create_degree_sequence
from networkx_degree import plotdistributuin



def random_network(n, m):

    
    G= nx.erdos_renyi_graph(n, 2*m/n*(n-1), seed=None)
    
    d = nx.degree(G)
    # calculate the giant componet return is a subgraph
    giant = max(nx.connected_component_subgraphs(G), key=len)
    degree = list(G.degree().values())
    results = plfit.plfit(degree)
    S = float(giant.number_of_nodes())/G.number_of_nodes()
    print("{0},{1},{2},{3},{4} ".format(G.number_of_nodes(), G.number_of_edges() ,S, results.plfit()[1], results.plfit()[0]))
    distribution = []
    for d in  set(degree):
        distribution.append([d,degree.count(d)])

    # orgin degree dirstribution 
    distribution = np.asarray(distribution)
    # log scale 
    distribution_log = np.log(distribution)
    # cumulative distribution 
    cumulative = list(map(lambda i: [distribution[i,0],np.sum(distribution[i:,1])], np.arange(distribution.shape[0])))
    cumulative = np.log(cumulative)
    data = []
    data.append(distribution)
    data.append(distribution_log)
    data.append(cumulative)
    plotdistributuin(data, "img/erd{0}_{1}.png".format(n,m))
    # remove the graph
    data = []
    d = G.degree()
    # draw and show graph
    fig = plt.figure(figsize=(16,12))
    plt.clf()
    nx.draw_spring(G,nodelist=d.keys(), node_color = "#FF8800", node_size=[10*v/np.mean(list(d.values())) for v in d.values()])
    plt.savefig('erd_net{0}_{1}.png'.format(n,m) ) 
    
if __name__ == "__main__" :
    
    data = [[100, 172], [1000, 1904],[10000, 35741],
    [100, 125] ,[1000, 1295],[10000 ,12244],
    [100 ,69],[1000 ,709],[10000 ,7302],
    [100 ,53],[1000 ,506],[10000 ,5128],]
    print ("nodes,edges,S,re_alpha,re_dim")
    for d in data:     
        random_network(d[0], d[1])


