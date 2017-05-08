import matplotlib.pyplot as plt 
import sys
import numpy as np
import time
import csv
import time
import networkx as nx
from networkx.utils import powerlaw_sequence, create_degree_sequence
from networkx_degree import plotdistributuin
from functools import reduce


tol = 1e-15
max_iter = 10000
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
    S = float(giant.number_of_nodes())/G.number_of_nodes()
    distribution = []
    for d in  set(degree):
        distribution.append([d,degree.count(d)])
    return(S, np.asarray(distribution).astype(np.float32))

def generatingfunction(alist, x):
    return np.sum(list(map(lambda k : k[1] * np.power(x, k[0]), alist)))

def pk(distribution):
    pk_ = distribution
    pk_[:,1] = pk_[:,1]/np.sum(pk_[:,1])
    return pk_

def qk(distribution):
    qk_ = pk(distribution)
    k_mu = np.dot(qk_[:,0], qk_[:,1])
    qk_[:,1] = qk_[:,1] / k_mu
    qk_[:,1] = np.multiply(qk_[:,1], qk_[:,0])
    qk_[:,0] = qk_[:,0] - 1
    return qk_

def numericalmethod(distribution):
    #get the probability of destribution pk and  qk
    pk_ = pk(distribution)
    qk_ = qk(distribution)

    # numerical methods
    u0 = 0
    u1 = generatingfunction(qk_, u0)
    i = 0
    while abs(u1 - u0 ) > tol: 
        u0 = u1
        u1 = generatingfunction(qk_, u1)
        i += 1 
        if i > max_iter:
            break

    # plot the function
    xs = np.linspace(0,1,1000) # 1000 linearly spaced numbers
    ys = list(map(lambda x: generatingfunction(qk_, x), xs))
    # g1(x) = y
    plt.plot(xs,ys)
    # x = y
    plt.plot(xs,xs, '--')
    plt.xlabel("u")
    plt.ylabel("y")
    plt.text(u1+.025, u1+.025, "u={0:.3f}".format(u1))
    plt.plot(u1, u1,  'ro')
    plt.savefig('gen_A{0}_S{1}.png'.format(a,s) ) 
    plt.clf()
    return (1- u1)
if __name__ == "__main__" :
    alpha = [1.831, 2.741, 3.271, 6.378]
    size = [100 , 1000, 10000, 100000]
    print("alpha,size,graph,numerical")
    for a in alpha:
        for s in size:
            (S, distribution) = powerlaw_network(a, s)
            S_n = numericalmethod(distribution)
            print("{0},{1},{2:.3f},{3:.3f}".format(a,s,S, S_n))
            