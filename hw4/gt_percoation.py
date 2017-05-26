from graph_tool.all import * 
import numpy as np 
import matplotlib.pyplot as plt 


def sample_k(max):
    accept = False
    while not accept:
        k = np.random.randint(1,max+1)
        accept = np.random.random() < 1.0/k
    return k

if __name__ == "__main__" :
    g = collection.data["as-22july06"]
    v_list = [v for v in g.vertices()]
    vertices = sorted(v_list, key=lambda v: v.out_degree())
    print('load data')
    sizes, comp = vertex_percolation(g, vertices)

    print('degree')
    np.random.shuffle(vertices)
    sizes2, comp = vertex_percolation(g, vertices)
    
    print('uniform')
    ee, x = eigenvector(g)   
    e_list = list(x)
    e_list = list(map(lambda i: [v_list[i], e_list[i]], np.arange(len(e_list))))
    vertices = sorted(e_list, key=lambda v: v[1])
    vertices = list(map(lambda v: v[0], vertices))
    sizes3, comp = vertex_percolation(g, vertices)
    print('eigenvector')
    c = closeness(g)  
    c_list = list(c)
    c_list = list(map(lambda i: [v_list[i], c_list[i]], np.arange(len(c_list))))
    vertices = sorted(c_list, key=lambda v: v[1])
    vertices = list(map(lambda v: v[0], vertices))
    sizes4, comp = vertex_percolation(g, vertices)
    print('closeness')
    vp, ep = betweenness(g)
    b_list = list(vp)
    b_list = list(map(lambda i: [v_list[i], b_list[i]], np.arange(len(b_list))))
    vertices = sorted(b_list, key=lambda v: v[1])
    vertices = list(map(lambda v: v[0], vertices))
    sizes5, comp = vertex_percolation(g, vertices)
    print('betweenness')
    plt.figure(figsize=(12,9)) 
    plt.plot(np.arange(len(sizes2)), sizes2, label='uniform')
    plt.plot(np.arange(len(sizes)), sizes, label='degree')
    plt.plot(np.arange(len(sizes3)), sizes3, label='eigenvector')
    plt.plot(np.arange(len(sizes4)), sizes4, label='closeness')
    plt.plot(np.arange(len(sizes5)), sizes5, label='betweenness')
    plt.xlabel("Vertices remaining")
    plt.ylabel("Size of giant component")
    plt.legend(loc="lower right")
    plt.savefig('percolation.png') 
    plt.clf()
    # print(eigenlist)