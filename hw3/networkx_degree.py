import matplotlib.pyplot as plt 
import sys
import numpy as np
import time
import csv
import time
import networkx as nx
from scipy import linspace, polyval, polyfit, sqrt, stats, randn

# import powerlaw
# import plfit


def plotdistributuin(data, filename):
 
    title = ["origin", "log", "cumulative"]
    xlael = ["Num", "log(Num)", "log(Num)"]
    ylabel = ["Degree", "log(Degree)", "log(Degree)" ]
    fig = plt.figure(figsize=(36,12))
    for i in range (len(data)): 
        ax = fig.add_subplot(1, 3 ,i+1) 
        d = data[i]
        plt.xticks(np.array([]))
        plt.yticks(np.array([]))
        ax.scatter(d[:,0],d[:,1], s=20, c = 'b')
        ax.set_title(title[i], fontsize=32)
        ax.set_xlabel(xlael[i], fontsize=20)
        ax.set_ylabel(ylabel[i], fontsize=20)
        plt.tight_layout(pad=3.0, w_pad=5.0)
    fig.savefig(filename) 
    plt.clf()
     
    
if __name__ == "__main__" :
    G=nx.read_edgelist(sys.argv[1]) 
    print ("number of nodes :{0}" .format(G.number_of_nodes()))
    print ("number of edges :{0}" .format(G.number_of_edges()))
    degree = list(G.degree().values())
    # results = powerlaw.Fit(degree) 
    # print ("alpha :{0}" .format(results.power_law.alpha ))
    # print ("dmin :{0}" .format(results.power_law.xmin ))
    # results = plfit.plfit(degree)
    # print ("alpha :{0}" .format(results.plfit()[1] ))
    # print ("dmin :{0}" .format(results.plfit()[0] ))
    distribution = []
    for d in  set(degree):
        distribution.append([d,degree.count(d)])

    # orgin degree dirstribution 
    distribution = np.asarray(distribution)
    # log scale 
    distribution_log = np.log(distribution)
    (ar,br)=polyfit(distribution_log[:,0],distribution_log[:,1],1)
    print (ar)
    # cumulative distribution 
    cumulative = list(map(lambda i: [distribution[i,0],np.sum(distribution[i:,1])], np.arange(distribution.shape[0])))
    cumulative = np.log(cumulative)

    (ar,br)=polyfit(cumulative[:,0],cumulative[:,1],1)
    print (ar)
    # data = []
    # data.append(distribution)
    # data.append(distribution_log)
    # data.append(cumulative)
    # plotdistributuin(data, "img/Flickr.png")