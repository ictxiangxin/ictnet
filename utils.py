__author__ = 'ict'

import random


def separate_edge_sum(graph, edge_sum):
    sep_edge = set()
    forbidden = set()
    while True:
        if not graph.direct_graph():
            if len(sep_edge) / 2 == edge_sum:
                break
        else:
            if len(sep_edge) == edge_sum:
                break
        node_a_list = list(graph.all_nodes() - forbidden)
        if len(node_a_list) == 0:
            break
        node_a = random.choice(node_a_list)
        if len(graph.node(node_a)) == 1:
            forbidden.add(node_a)
            continue
        node_b_list = list(set(graph.node(node_a)) - forbidden)
        if len(node_b_list) == 0:
            forbidden.add(node_a)
            continue
        node_b = random.choice(node_b_list)
        if len(graph.node(node_b)) == 1:
            forbidden.add(node_b)
            continue
        sep_edge.add((node_a, node_b))
        if not graph.direct_graph():
            sep_edge.add((node_b, node_a))
        graph.del_edge(node_a, node_b)
    return sep_edge


def separate_edge_rate(graph, edge_rate):
    if not 0 < edge_rate < 1:
        return set()
    edge_sum = int(graph.sum_edges() * edge_rate)
    if not graph.direct_graph():
        edge_sum /= 2
    return separate_edge_sum(graph, edge_sum)


def evaluate(sep_set, test):
    for node_tuple in test:
        test.add((node_tuple[1], node_tuple[0]))
    p = len(sep_set and test) / len(test)
    r = len(sep_set and test) / len(sep_set)
    if p + r == 0:
        return 0
    return 2 * p * r / (p + r)