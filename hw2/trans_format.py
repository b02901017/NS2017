
import sys
import numpy as np
import networkx as nx 
import csv
def readfile(filename): 
    f = open(filename, 'r')
    mat = [] 
    while True :
        line = f.readline()
        if len(line) == 0:
            break
        results = line[:len(line)-1].split(" ")
        mat.append(results)
    f.close()
    return mat
def writefile(filename, datas): 
    f = open(filename, 'w')
    trigger = False

    for data in datas:
        if data[0].startswith('*edges'):
            trigger = True
            f.write("%s\n" % '*Arcs')
            continue
        if trigger:
            f.write("%s %s %s\n" % (data[0],data[1],data[2]))
        else :
            f.write("%s \"%s\"\n" % (data[0],data[1]))
    f.close()
def reformGML():
    f1 = open(sys.argv[1], 'r')
    f2 = open(sys.argv[2],"w")
    mat = [] 
    while True :
        line = f1.readline()
        if len(line) == 0:
            break
        if line.startswith('['):
            continue
        if line.startswith('  ['):
            continue
        if line.startswith('  node'):
            line = '  node [\n'
        if line.startswith('  edge'):
            line = '  edge [\n'
        if line.startswith('graph'):
            line = 'graph [\n'
        f2.write(line)
    f1.close()


def GMLtoNET():
    G = nx.read_gml(sys.argv[1])
    # myedge = readfile(sys.argv[1]) 
    # G = nx.Graph()                                        
    # for i in range (len(myedge)):                                                                 
    #     G.add_edge(myedge[i][0],myedge[i][1])  
    nx.write_pajek(G,sys.argv[1][:len(sys.argv[1])-3]+"net")

    data = readfile(sys.argv[1][:len(sys.argv[1])-3]+"net") 
    writefile(sys.argv[1][:len(sys.argv[1])-3]+"net",data)
def NETplusCOM():
    G = nx.read_gml(sys.argv[1])
    # myedge = readfile(sys.argv[1]) 
    # G = nx.Graph()                                        
    # for i in range (len(myedge)):                                                                 
    #     G.add_edge(myedge[i][0],myedge[i][1])  
    nx.write_pajek(G,sys.argv[1][:len(sys.argv[1])-3]+"net")
    graph = readfile(sys.argv[1][:len(sys.argv[1])-3]+"net") 
    community = readfile(sys.argv[1][:len(sys.argv[1])-4]+"_comm_comboC++.txt") 
    f = open(sys.argv[1][:len(sys.argv[1])-4]+"_combo.txt","w")
    i = 0
    for com in community:
        trigger = 0
        for j in range (1,len(graph[i+1])):
            if graph[i+1][j].startswith("\""):
                f.write("%s " % graph[i+1][j][1:])
                trigger = 1
                continue
            if graph[i+1][j].endswith("\""):
                f.write("%s" % graph[i+1][j][:len(graph[i+1][j])-1])
                break
            if trigger == 1 :
                f.write("%s " % graph[i+1][j])
            if trigger == 0:
                f.write("%s" % graph[i+1][j])
                break
        f.write(",%s\n" % com[0])
        i+=1
    
def seperatorcorrect():
    f = open(sys.argv[1], 'w')
    with open(sys.argv[2]) as file :
        spamreader = csv.reader(file)
        for row in spamreader:
            f.write("\"%s,%s\",%s\n" % (row[0],row[1],row[2]))
    
if __name__ == "__main__" :

    seperatorcorrect()