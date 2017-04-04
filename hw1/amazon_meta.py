
import sys
import numpy as np
import time
import csv

def readfile(filename): 
	f = open(filename, 'r')
	mat = [] 
	while True :
		line = f.readline()

		if len(line) == 0:
			break
		elif line.startswith('Id'):
			mat.append(line)
		elif line.startswith('  group'):
			mat.append(line[2:])
		else :
			continue
	f.close()
	return mat


def writefile( data): 
	# Book = open('Book.csv', 'w')
	# Music = open('Music.csv', 'w')
	# DVD = open('DVD.csv', 'w')
	f = open('meta.csv', 'w')
	for i in range(1,len(data)-1,2):
		if not (data[i+1].startswith('group')):
			i -= 1
		else :
			data[i] = data[i][6:len(data[i])-2]
			data[i+1] = data[i+1][7:len(data[i+1])-2]
			# if (data[i+1] == 'Book'):
			# 	Book.write("%s,%s\n" % (data[i],data[i+1]))
			# if (data[i+1] == 'Music'):
			# 	Music.write("%s,%s\n" % (data[i],data[i+1]))
			# if (data[i+1] == 'DVD'):
			# 	DVD.write("%s,%s\n" % (data[i],data[i+1]))
			f.write("%s,%s\n" % (data[i],data[i+1]))
	
	# Music.close()
	# DVD.close()
	# Book.close()
	f.close()



if __name__ == "__main__" :

	result = [] 
	result = readfile(sys.argv[1]) 

	writefile(result)


	