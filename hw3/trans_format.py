import sys
def readfile(): 
    f = open(sys.argv[1], 'r')
    data = [] 
    while True :
        line = f.readline()
        if len(line) == 0:
            break
        data.append( line.split("	"))
    f.close()
    return data
def writefile(data): 
    f = open(sys.argv[2], 'w')
    for row in data:
        f.write("{0} {1}\n".format(row[0],row[1]))
    f.close()

if __name__ == "__main__" :
    data = readfile()
    data = list(map(lambda row: row[:2], data))
    writefile(data)