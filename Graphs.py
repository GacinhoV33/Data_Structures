#!/usr/bin/python
# -*- coding: utf-8 -*-


class Object:
    def __init__(self, data, key):
        self.data = data
        self.key = key

    def __repr__(self):
        return str((self.data, self.key))


class MatrixNeighbourGraph:

    def __init__(self):
        self.vertex_list = list()
        self.matrix = list()

    def insertVertex(self, data, key):
        self.vertex_list.append(Object(data, key))
        for lst in self.matrix:
            lst.append(0)
        self.matrix.append([0] * self.order())

    def insertEdge(self, key1, key2):
        i = None
        j = None
        for k in range(self.order()):
            if self.vertex_list[k].key == key1:
                i = k
            if self.vertex_list[k].key == key2:
                j = k
        if i is None or j is None:
            raise ValueError("Wrong keys")
        else:
            self.matrix[i][j] = 1
            self.matrix[j][i] = 1

    def deleteVertex(self, key):
        if key in [i.key for i in self.vertex_list]:
            pos = 0
            for i in range(self.order()):
                if self.vertex_list[i].key == key:
                    pos = i

            self.vertex_list.pop(pos)
            self.matrix.pop(pos)
            for lst in self.matrix:
                lst.pop(pos)
        else:
            raise ValueError("Wrong Key")

    def deleteEdge(self, key1, key2):
        i = None
        j = None
        for k in range(self.order()):
            if self.vertex_list[k].key == key1:
                i = k
            if self.vertex_list[k].key == key2:
                j = k
        if i is not None and j is not None:
            self.matrix[i][j] = 0
            self.matrix[j][i] = 0
        else:
            ValueError("There's no edge familiar with these two keys")

    def getVertexIdx(self, key):
        for i in range(self.order()):
            if self.vertex_list[i].key == key:
                return i
        return None

    def getVertex(self, key):
        if self.getVertexIdx(key):
            return self.vertex_list[self.getVertexIdx(key)]
        else:
            raise ValueError("There is no vertex associated with this key")

    def size(self):
        sum_size = 0
        for el in self.matrix:
            for el2 in el:
                sum_size += el2
        return int(sum_size / 2)

    def order(self):
        return len(self.vertex_list)

    def print_graph(self):
        print("Neighbour matrix:", self.matrix)
        print("Vertexes: ", self.vertex_list)

    def edges(self):
        edges_list = list()
        for i in range(self.order()):
            for j in range(self.order()):
                if self.matrix[i][j] == 1:
                    edges_list.append([self.vertex_list[i].key, self.vertex_list[j].key])
        return edges_list


class NeighbourListGraph:
    def __init__(self):
        self.neighbour_list = []
        self.vertex_list = []

    def insertVertex(self, data, key):
        if key not in [obj.key for obj in self.vertex_list]:
            self.vertex_list.append(Object(data, key))
        else:
            print("WRong")

    def insertEdge(self, key1, key2):
        if key1 in [obj.key for obj in self.vertex_list] and key2 in [obj.key for obj in self.vertex_list]:
            if (key1, key2) not in self.neighbour_list:
                self.neighbour_list.append((key1, key2))
                self.neighbour_list.append((key2, key1))

    def getVertexIdx(self, key):
        for i in range(self.order()):
            if self.vertex_list[i].key == key:
                return i
        return None

    def getVertex(self, key):
        vert_idx = self.getVertexIdx(key)
        if vert_idx:
            return self.vertex_list[vert_idx]
        else:
            raise ValueError("No Vertex associated with this key!")

    def deleteVertex(self, key):
        vert_idx = self.getVertexIdx(key)
        if vert_idx:
            self.vertex_list.pop(vert_idx)
        else:
            raise ValueError("No Vertex associated with this key!")
        del_list = list()
        for i in range(self.order()):
            if key in self.neighbour_list[i]:
                del_list.append(i)
        counter = 0
        for el in del_list:
            self.neighbour_list.pop(el - counter)
            counter += 1

    def deleteEdge(self, key1, key2):
        i_del = list()
        for i in range(self.size()):
            if self.neighbour_list[i] == (key1, key2) or self.neighbour_list[i] == (key2, key1):
                i_del.append(i)
        if len(i_del) > 0:
            self.neighbour_list.pop(i_del[0])
            self.neighbour_list.pop(i_del[1] - 1)
        else:
            raise ValueError("There's no edges associated with these keys")

    def print_graph(self):
        print("Neighbour matrix:", self.neighbour_list)
        print("Vertexes: ", self.vertex_list)

    def order(self):
        return len(self.neighbour_list)

    def size(self):
        return len(self.neighbour_list)

    def edges(self):
        return [(k[0], k[1]) for k in self.neighbour_list]



