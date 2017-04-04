import networkx as nx             
import matplotlib.pyplot as plt 
import sys
import numpy as np
import time
import csv
import time
import itertools
import operator
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


def readattr(filename):
	f = open(filename, 'r')
	mat = {}
	while True :
		line = f.readline()
		if len(line) == 0:
			break
		results = line.split(",")
		mat[int(results[0])] = float(results[1])
	f.close()
	return mat

if __name__ == "__main__" :


	myedge = readfile(sys.argv[1])

	K = nx.Graph()                                        
	for i in range (len(myedge)):                                                                 
		K.add_edge(myedge[i][0],myedge[i][1])   
	 

	Alld = readattr('degrees.txt')
	Alld = dict(sorted(Alld.items(), key=operator.itemgetter(1))[len(Alld)-5000:])
	H1 = K.subgraph(Alld)
	nx.draw_spring(H1,nodelist=Alld.keys(), node_size=[1*v/np.mean(Alld.values()) for v in Alld.values()])
	plt.savefig('degreeAll.png')
	plt.clf()
	

	Bookd = readattr('degreesBook.txt')
	Bookd = dict(sorted(Bookd.items(), key=operator.itemgetter(1))[len(Bookd)-5000:])
	H2 = K.subgraph(Bookd)
	nx.draw_spring(H2,nodelist=Bookd.keys(), node_size=[1*v/np.mean(Bookd.values()) for v in Bookd.values()])
	plt.savefig('degreeBook.png')
	plt.clf()

	DVD = readcat('DVD.csv')
	DVDb = readattr('betweennessDVD.txt')
	DVDd = readattr('degreesDVD.txt')
	DVDc = readattr('closenessDVD.txt')
	DVDe = readattr('eigenvectorDVD.txt')
	DVDb = dict(sorted(DVDb.items(), key=operator.itemgetter(1))[len(DVDb)-5000:])
	DVDc = dict(sorted(DVDc.items(), key=operator.itemgetter(1))[len(DVDc)-5000:])
	DVDd = dict(sorted(DVDd.items(), key=operator.itemgetter(1))[len(DVDd)-5000:])
	DVDe = dict(sorted(DVDe.items(), key=operator.itemgetter(1))[len(DVDe)-5000:])

	H3 = K.subgraph(DVDb)
	nx.draw_spring(H3,nodelist=DVDb.keys(), node_size=[1*v/np.mean(DVDb.values()) for v in DVDb.values()])
	plt.savefig('betweennessDVD.png')
	plt.clf()
	H4 = K.subgraph(DVDd)
	nx.draw_spring(H4,nodelist=DVDd.keys(), node_size=[1*v/np.mean(DVDd.values()) for v in DVDd.values()])
	plt.savefig('degreeDVD.png')
	plt.clf()
	H5 = K.subgraph(DVDc)
	nx.draw_spring(H5,nodelist=DVDc.keys(), node_size=[1*v/np.mean(DVDc.values()) for v in DVDc.values()])
	plt.savefig('closenessDVD3.png')
	plt.clf()
	H6 = K.subgraph(DVDe)
	nx.draw_spring(H6,nodelist=DVDe.keys(), node_size=[1*v/np.mean(DVDe.values()) for v in DVDe.values()])
	plt.savefig('eigenvectorDVD.png')
	plt.clf()



	Music = readcat('Music.csv') 
	Musicb = readattr('betweennessMusic.txt')
	Musicc = readattr('closenessMusic.txt')	
	Musicd = readattr('degreesMusic.txt')
	Musice = readattr('eigenvectorMusic.txt')
	Musicb = dict(sorted(Musicb.items(), key=operator.itemgetter(1))[len(Musicb)-5000:])
	Musicc = dict(sorted(Musicc.items(), key=operator.itemgetter(1))[len(Musicc)-5000:])
	Musicd = dict(sorted(Musicd.items(), key=operator.itemgetter(1))[len(Musicd)-5000:])
	Musice = dict(sorted(Musice.items(), key=operator.itemgetter(1))[len(Musice)-5000:])
	H7 = K.subgraph(Musicb)
	nx.draw_spring(H7,nodelist=Musicb.keys(), node_size=[1*v/np.mean(Musicb.values()) for v in Musicb.values()])
	plt.savefig('betweennessMusic.png')
	plt.clf()
	H8 = K.subgraph(Musicd)
	nx.draw_spring(H8,nodelist=Musicd.keys(), node_size=[1*v/np.mean(Musicd.values()) for v in Musicd.values()])
	plt.savefig('degreeMusic.png')
	plt.clf()
	H9 = K.subgraph(Musicc)
	nx.draw_spring(H9,nodelist=Musicc.keys(), node_size=[1*v/np.mean(Musicc.values()) for v in Musicc.values()])
	plt.savefig('closenessMusic.png')
	plt.clf()
	H10 = K.subgraph(Musice)
	nx.draw_spring(H10,nodelist=Musice.keys(), node_size=[1*v/np.mean(Musice.values()) for v in Musice.values()])
	plt.savefig('eigenvectorMusic.png')
	plt.clf()




