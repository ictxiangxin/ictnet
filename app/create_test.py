__author__ = 'ict'

from graph import Graph
from utils import separate_edge_rate

g = Graph("../data/friend.txt")
g.read()
sep = separate_edge_rate(g, 0.1)
with open("../data/test.txt", "w") as fp:
    for e in sep:
        fp.write("%s\t%s\n" % (e[0], e[1]))
g.write("../data/train.txt")