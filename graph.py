__author__ = 'ict'

import pickle


class Graph:
    def __init__(self, filename=None, direct=False):
        self.__direct = direct
        self.__filename = filename
        self.__node = set()
        self.__link = {}

    def read(self):
        if self.__filename is None:
            raise Exception("Need filename")
        with open(self.__filename, "r") as fp:
            data = fp.read()
            if "\r\n" in data:
                data_list = data.split("\r\n")
            else:
                data_list = data.split("\n")
            for s in data_list:
                comment_index = s.find("#")
                if comment_index != -1:
                    s = s[: comment_index]
                if len(s) == 0:
                    continue
                s = s.replace(" ", "\t")
                node_tuple = s.split("\t")
                self.__node.add(int(node_tuple[0]))
                self.__node.add(int(node_tuple[1]))
                if int(node_tuple[0]) not in self.__link:
                    self.__link[int(node_tuple[0])] = {}
                self.__link[int(node_tuple[0])][int(node_tuple[1])] = 1
                if not self.__direct:
                    if int(node_tuple[1]) not in self.__link:
                        self.__link[int(node_tuple[1])] = {}
                    self.__link[int(node_tuple[1])][int(node_tuple[0])] = 1

    def add_node(self, node_id):
        self.__node.add(node_id)
        if node_id not in self.__link:
            self.__link[node_id] = {}

    def add_edge(self, node_a, node_b, value=1):
        self.add_node(node_a)
        self.add_node(node_b)
        self.__link[node_a][node_b] = value
        if not self.__direct:
            self.__link[node_b][node_a] = value

    def del_node(self, node_id):
        if node_id in self.__node:
            self.__node.remove(node_id)
            del self.__link[node_id]
            for _, link in self.__link.items():
                if node_id in link:
                    del link[node_id]

    def del_edge(self, node_a, node_b):
        if node_a in self.__link:
            if node_b in self.__link[node_a]:
                del self.__link[node_a]
        if not self.__direct:
            if node_a in self.__link[node_b]:
                del self.__link[node_b]

    def node(self, node_id):
        if node_id not in self.__node:
            return None
        return self.__link[node_id]

    def edge(self, node_a, node_b):
        if node_a not in self.__node:
            return None
        if node_b not in self.__link[node_a]:
            return None
        return self.__link[node_a][node_b]

    def all_nodes(self):
        return self.__node

    def all_edges(self):
        return self.__link


def save(graph, filename):
    with open(filename, "wb") as fp:
        pickle.dump(graph, fp)


def load(filename):
    with open(filename, "rb") as fp:
        return pickle.load(fp)