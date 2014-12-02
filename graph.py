__author__ = 'ict'

import pickle


class Graph:
    def __init__(self, filename=None, direct=False):
        self.direct = direct
        self.filename = filename
        self.node = set()
        self.link = {}

    def read(self):
        if self.filename is None:
            raise Exception("Need filename")
        with open(self.filename, "r") as fp:
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
                self.node.add(int(node_tuple[0]))
                self.node.add(int(node_tuple[1]))
                if int(node_tuple[0]) not in self.link:
                    self.link[int(node_tuple[0])] = {}
                self.link[int(node_tuple[0])][int(node_tuple[1])] = 1
                if not self.direct:
                    if int(node_tuple[1]) not in self.link:
                        self.link[int(node_tuple[1])] = {}
                    self.link[int(node_tuple[1])][int(node_tuple[0])] = 1


def save(graph, filename):
    with open(filename, "wb") as fp:
        pickle.dump(graph, fp)


def load(filename):
    with open(filename, "rb") as fp:
        return pickle.load(fp)