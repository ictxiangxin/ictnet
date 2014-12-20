__author__ = 'ict'

from graph import Graph
from utils import random_number

# read original data
g = Graph("../data/friend.txt")

# load data
g.read()

# create random node number file
random_number(g, "../data/friend-new.txt")