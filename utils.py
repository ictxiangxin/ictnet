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


def random_number(graph, out_file):
    with open(out_file, "w") as ofp:
        number = list(range(len(graph.all_nodes())))
        nodes = graph.all_nodes()
        mapping = {}
        for node in nodes:
            n = random.randint(0, len(number) - 1)
            mapping[node] = number[n]
            del number[n]
        edges = graph.all_edges()
        after = []
        for a, link in edges.items():
            for b in link:
                after.append("%s\t%s\n" % (mapping[a], mapping[b]))
        while len(after) != 0:
            n = random.randint(0, len(after) - 1)
            ofp.write(after[n])
            del after[n]


def separate_edge_rate(graph, edge_rate):
    if not 0 < edge_rate < 1:
        return set()
    edge_sum = int(graph.sum_edges() * edge_rate)
    if not graph.direct_graph():
        edge_sum /= 2
    return separate_edge_sum(graph, edge_sum)


def evaluate(test, result, quiet=False):
    test_copy = result.copy()
    for node_tuple in test_copy:
        result.add((node_tuple[1], node_tuple[0]))
    hit_sum = len(test & result)
    precision = hit_sum / len(result)
    recall = hit_sum / len(test)
    if precision + recall == 0:
        f1 = 0
    else:
        f1 = 2 * precision * recall / (precision + recall)
    if not quiet:
        print("Hit Sum: %d" % hit_sum)
        print("Precision: %f" % precision)
        print("Recall: %f" % recall)
        print("F1: %f" % f1)
    rst = {"Hit Sum": hit_sum, "Precision": precision, "Recall": recall, "F1": f1}
    return rst