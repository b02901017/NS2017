import networkx as nx             
import matplotlib.pyplot as plt 
import sys
import numpy as np
import time
import csv
import time
import itertools
import operator
import similarity 


def readfile(filename): 
	f = open(filename, 'r')
	mat = [] 
	while True :
		line = f.readline()
		if len(line) == 0:
			break
		if line.startswith('#'):
			continue
		results = map(int, line.split('\t'))
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
	 

	# Alld = readattr('degrees.txt')
	
	# H1 = K.subgraph(Alld)


	# Bookd = readattr('degreesBook.txt')
	
	# H2 = K.subgraph(Bookd)



	DVDd = readattr('degreesDVD.txt')
	DVDd = dict(sorted(DVDd.items(), key=operator.itemgetter(1))[:])

	H3 = K.subgraph(DVDd)


	# Musicd = readattr('degreesMusic.txt')
	
	# H4 = K.subgraph(Musicd)
	s3 = similarity.simrank(H3)
	print(s3)
	# mat = nx.to_numpy_matrix(H9)
	# print(len(mat))
	writefile('DVDsim5.csv',s3)
