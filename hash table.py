#!/usr/bin/python
# -*- coding: utf-8 -*-


class ListEl:

    def __init__(self, value, key):
        self.value = value
        self.key = key


class MixedList:

    def __init__(self, size: int, c1=1, c2=0):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.tab = [None for i in range(self.size)]
        self.flag_tab = [None for i in range(self.size)]

    def search(self, key):
        idx = self.fun_hash(self.translate(key))
        if self.tab[idx]:
            if self.tab[idx].key != key:
                idx = self.solve_collision(idx, key)
                return self.tab[idx]
            else:
                return self.tab[idx]

    def insert(self, elem):
        idx = self.fun_hash(self.translate(elem.key))

        if not self.tab[idx]:
            self.tab[idx] = elem
        elif self.tab[idx].key == elem.key:
            self.tab[idx] = elem
        else:
            flag = idx
            i = 0
            while self.tab[idx]:
                i += 1
                idx = (idx + self.c1 * i + self.c2 * i * i) % self.size  #here change to algorith c1 and so on
                if idx == self.size:
                    idx = 0
                if idx == flag:
                    return print("List is full")
            self.tab[idx] = elem

    def fun_hash(self, key):
        data_idx = key % self.size
        return data_idx

    def solve_collision(self, data_idx, key):
        i = 0
        if not self.tab[data_idx] and not self.flag_tab[data_idx]:
            raise ValueError("No element with this key")
        while self.tab[data_idx].key != key or self.flag_tab[data_idx]:
            i += 1
            data_idx = (data_idx + self.c1 * i + self.c2 * i * i) % self.size
            if i > self.size:
                raise ValueError("No element with this key")
        return data_idx

    def translate(self, data):
        data = str(data)
        sum_data = 0
        for el in data:
            sum_data += ord(el)
        return sum_data

    def remove(self, key):
        idx = self.fun_hash(self.translate(key))
        if self.tab[idx]:
            if self.tab[idx].key == key:
                self.tab[idx] = None
                self.flag_tab[idx] = 1

        elif not self.tab[idx] and self.flag_tab[idx]:
            idx = self.solve_collision(idx, key)
            self.tab[idx] = None
            self.flag_tab[idx] = 1
        else:
            raise ValueError("No Element with this key")

    def __str__(self):
        return str([":".join((str(el.value), str(el.key))) for el in self.tab if el])
