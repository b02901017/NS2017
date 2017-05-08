import matplotlib.pyplot as plt 
import sys
import numpy as np
import time
import csv
import time
import networkx as nx
from networkx.utils import powerlaw_sequence, create_degree_sequence
import plfit
from networkx_degree import plotdistributuin
def powerlaw_network(alpha, size):
    while True:  
        s=[]
        while len(s)<size:
            nextval = int(nx.utils.powerlaw_sequence(1, alpha)[0]) #100 nodes, power-law exponent 2.5
            if nextval!=0:
                s.append(nextval)
        if sum(s)%2 == 0:
            break
    G = nx.configuration_model(s)
    G= nx.Graph(G) # remove parallel edges
    G.remove_edges_from(G.selfloop_edges())

    d = nx.degree(G)
    # calculate the giant componet return is a subgraph
    giant = max(nx.connected_component_subgraphs(G), key=len)
    degree = list(G.degree().values())
    results = plfit.plfit(degree)
    S = float(giant.number_of_nodes())/G.number_of_nodes()
    print("{0},{1},{2},{3},{4},{5} ".format(alpha, G.number_of_nodes(), G.number_of_edges() ,S, results.plfit()[1], results.plfit()[0]))
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
    plotdistributuin(data, "img/{0}_{1}.png".format(alpha,size))
    # remove the graph
    G.clear()
    giant.clear()
    data = []

    # draw and show graph
    plt.clf()
    nx.draw_spring(G,nodelist=d.keys(), node_color = "#FF8800", node_size=[10*v/np.mean(list(d.values())) for v in d.values()])
    plt.savefig('powerlaw_A{0}_S{1}.png'.format(alpha,size) ) 

    
if __name__ == "__main__" :
    alpha = [1.9310 , 2.4710, 3.271, 6.378]
    size = [100 , 1000, 10000]
    print ("alpha,nodes,edges,S,re_alpha,re_dim")
    for a in alpha:
        for s in size:
             powerlaw_network(a, s)


    
