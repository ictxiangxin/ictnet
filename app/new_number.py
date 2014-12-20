__author__ = 'ict'

from graph import Graph
from utils import random_number

g = Graph("../data/friend.txt")
g.read()
random_number(g, "../data/friend-new.txt")