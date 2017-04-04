import copy
import sys
import networkx as nx
from collections import defaultdict

def simrank(G, c=0.9, max_iter=100, remove_neighbors=False, remove_self=False, dump_process=False):
  if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph:
    raise Exception("simrank() not defined for graphs with multiedges.")

  if G.is_directed():
    raise Exception("simrank() not defined for directed graphs.")

  sim_old = defaultdict(list)
  sim = defaultdict(list)
  for n in G.nodes():
    sim[n] = defaultdict(int)
    sim[n][n] = 1
    sim_old[n] = defaultdict(int)
    sim_old[n][n] = 0

  # calculate simrank
  for iter_ctr in range(max_iter):
    if _is_converge(sim, sim_old):
      break
    sim_old = copy.deepcopy(sim)
    for i, u in enumerate(G.nodes()):
      if dump_process:
        sys.stdout.write("\r%d : % d / %d" % (iter_ctr, i, G.number_of_nodes()))
      for v in G.nodes():
        if u == v:
          continue
        s_uv = 0.0
        for n_u in G.neighbors(u):
          for n_v in G.neighbors(v):
            s_uv += sim_old[n_u][n_v]
        sim[u][v] = (c * s_uv / (len(G.neighbors(u)) * len(G.neighbors(v)))) \
            if len(G.neighbors(u)) * len(G.neighbors(v)) > 0 else 0
    if dump_process:
      print ''

  if remove_self:
    for m in G.nodes():
      G[m][m] = 0

  if remove_neighbors:
    for m in G.nodes():
      for n in G.neighbors(m):
        sim[m][n] = 0

  return sim

def _is_converge(s1, s2, eps=1e-4):
  for i in s1.keys():
    for j in s1[i].keys():
      if abs(s1[i][j] - s2[i][j]) >= eps:
        return False
  return True