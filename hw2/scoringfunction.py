import networkx as nx
import sys
import numpy as np
import matplotlib.colors as colors
import random
import matplotlib.pyplot as plt
def internal_density (G, partition):
    # the average density of the node belongs to each commmnities
    val = 0.
    n = G.number_of_nodes()
    for com in set(partition.values()) :
        list_nodes = [nodes for nodes in partition.keys()
                            if partition[nodes] == com]
        H = G.subgraph(list_nodes)
        ns = H.number_of_nodes()
        val  += ns * nx.density(H)
    return val / n

def edges_inside(G, partition):
    # the ration between total numberof edges and the edgs in th community
    val = 0.
    m = G.number_of_edges()
    for com in set(partition.values()) :
        list_nodes = [nodes for nodes in partition.keys()
                            if partition[nodes] == com]
        H = G.subgraph(list_nodes)
        ms = H.number_of_edges()
        val  += ms
    return val/m

def TPR(G, partition):
    #fraction of nodes in S that belong to a triad
    val = 0.
    n = G.number_of_nodes()
    for com in set(partition.values()) :
        list_nodes = [nodes for nodes in partition.keys()
                            if partition[nodes] == com]
        H = G.subgraph(list_nodes)
        ns = H.number_of_nodes()
        if ns  > 3 :
            triangles = float(np.sum(nx.triangles(H).values()))/((ns)*(ns-1)*(ns-2)/6*3)
            val += ns*triangles
    return  val/n

def expansion(G, partition):
    # measures the number of edges per node that point outside the cluster
    val = 0.
    n = G.number_of_nodes()
    for com in set(partition.values()) :
        list_nodes = [nodes for nodes in partition.keys()
                            if partition[nodes] == com]
        H = G.subgraph(list_nodes)
        ds = np.sum(G.degree(list_nodes).values())
        ns = H.number_of_nodes()
        ms = H.number_of_edges()
        cs  = float(ds - 2*ms)
        val  += cs
    return  val/n
def cut_ratio(G, partition):
   #the fraction of existing edges (out of all possible edges) leaving the cluster
    val = 0.
    n = G.number_of_nodes()

    for com in set(partition.values()) :
        list_nodes = [nodes for nodes in partition.keys()
                            if partition[nodes] == com]
        H = G.subgraph(list_nodes)
        ds = np.sum(G.degree(list_nodes).values())
        ns = H.number_of_nodes()
        ms = H.number_of_edges()
        cs  = float(ds - 2*ms)
        val += cs / (n - ns)
    return  val/n
def numofcommunities(partition): 
    #the nummber of communities
    
    return  len(set(partition.values()))
def drawpart(G, partition, name):
    size = float(len(set(partition.values())))
    pos = nx.spring_layout(G)
    count = 0 
    for com in set(partition.values()) :
        count += 1
        color = colors.cnames.values()[random.randint(0,len(colors.cnames.values())-1)]
        list_nodes = [nodes for nodes in partition.keys()
                                    if partition[nodes] == com]
        nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20, node_color=color  )
    nx.draw_networkx_edges(G,pos, alpha=0.5)
    plt.savefig(name)
    plt.clf()