import matplotlib.pyplot as plt 
import sys
import numpy as np
import time
import csv
import time
import networkx as nx
import random
import operator
S = 0
I = 1




class SI_model:
    def __init__(self, G, beta, mode = "uniform"):
        self.G = G
        nx.set_node_attributes(self.G, 'state', S)
        self.beta = beta
        self.mode = mode
        self.i_list = []
        self.s_list = list(self.G.nodes())
        self.hist = []
    
    def checkstate(self, node):

        if node["state"] == I:
            return False
        else:
            return True 

    def propogation(self, neighbor):
        if not neighbor:
            return
        suspected = list(filter(lambda n: self.checkstate(self.G.node[n]) ,neighbor))
        if not suspected:
            return
        if self.mode == "uniform":
            for s in suspected:
                if np.random.rand() < self.beta :
                    self.infected(s)
        if self.mode == "degree":
            suspected = sorted(G.degree(suspected).items(), key=operator.itemgetter(1), reverse=True)
            k = 0 
            for i in range(len(suspected)):
                s = suspected[k][0]
                if np.random.rand() < self.beta :
                    self.infected(s)
                if not self.checkstate(self.G.node[s]):
                    k += 1 
        return
    def infected(self, target):
        if  self.G.node[target]['state'] == I :
            return
        self.G.node[target]['state'] = I
        self.s_list.remove(target)
        self.i_list.append(target)

        
    def run(self) :
        target = random.choice(self.s_list)
        self.infected(target)
        i = 0 
        while len(self.s_list) > 0: 
            neighbors = list(map(lambda i : G.neighbors(i), self.i_list))
            for n in neighbors : 
                self.propogation(n)
            self.hist.append([i,len(self.s_list),len(self.i_list)])
            i += 1

            

    
if __name__ == "__main__" :
    G = nx.read_gml(sys.argv[1])
    t0 = time.time()                                  
    print ("number of nodes :%s, time:%s" %(G.number_of_nodes(),time.time() - t0))
    t0 = time.time() 
    print ("number of edges :%s, time:%s" %(G.number_of_edges(),time.time() - t0))

    # model = SI_model(G, 0.8, mode = "degree")
    # model.run()
    # hist = np.asarray(model.hist)
    # plt.plot(hist[:,0], hist[:,1]/G.number_of_nodes(), 'r', label='degree')
    # plt.plot(hist[:,0], hist[:,2]/G.number_of_nodes(), 'r')
    # plt.figure(figsize=(12,9))
    # model = SI_model(G, 0.99, mode = "uniform")
    # model.run()
    # hist = np.asarray(model.hist)
    # # plt.plot(hist[:,0], hist[:,1]/G.number_of_nodes(), 'b', label='0.99')
    # plt.plot(hist[:,0], hist[:,2]/G.number_of_nodes(), 'b', label='0.99')

    # model = SI_model(G, 0.8, mode = "uniform")
    # model.run()
    # hist = np.asarray(model.hist)
    # # plt.plot(hist[:,0], hist[:,1]/G.number_of_nodes(), 'orange', label='0.8')
    # plt.plot(hist[:,0], hist[:,2]/G.number_of_nodes(), 'orange', label='0.8')

    # model = SI_model(G, 0.5, mode = "uniform")
    # model.run()
    # hist = np.asarray(model.hist)
    # # plt.plot(hist[:,0], hist[:,1]/G.number_of_nodes(), 'g', label='0.5')
    # plt.plot(hist[:,0], hist[:,2]/G.number_of_nodes(), 'g', label='0.5')

    model = SI_model(G, 0.99, mode = "uniform")
    model.run()
    hist = np.asarray(model.hist)
    plt.plot(hist[:,0], hist[:,1]/G.number_of_nodes(), 'b')
    plt.plot(hist[:,0], hist[:,2]/G.number_of_nodes(), 'b', label='uniform')

    model = SI_model(G, 0.99, mode = "degree")
    model.run()
    hist = np.asarray(model.hist)
    plt.plot(hist[:,0], hist[:,1]/G.number_of_nodes(), 'orange')
    plt.plot(hist[:,0], hist[:,2]/G.number_of_nodes(), 'orange', label='degree')
    plt.xlabel("Iteration")
    plt.ylabel("percentage(%)")
    plt.legend(loc="lower right")
    plt.savefig('5-99.png')
    

    # betas = np.linspace(0.05, 1.0, 20)
    # uniform = [] 
    # degree = []
    # plt.figure(figsize=(12,9))
    # for b in betas :
    #     model = SI_model(G, b, mode = "uniform")
    #     model.run()
    #     hist = np.asarray(model.hist)
    #     uniform.append(len(hist))
    # for b in betas :
    #     model = SI_model(G, b, mode = "degree")
    #     model.run()
    #     hist = np.asarray(model.hist)
    #     degree.append(len(hist))
    #     # plt.plot(hist[:,0], hist[:,1]/G.number_of_nodes(), 'r')
    # plt.plot(uniform, betas, label='uniform')
    # plt.plot(degree, betas, label='degree')
    # plt.xlabel("Iteration")
    # plt.ylabel("beta")
    # plt.legend(loc="lower right")
    # plt.savefig('5-b.png')