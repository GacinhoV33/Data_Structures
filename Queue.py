#!/usr/bin/python
# -*- coding: utf-8 -*-


class BaseList:
    def __init__(self, size=5):
        self.tab = realloc([], size)
        self.size = len(self.tab)
        self.save_idx = 0
        self.read_idx = 0

    def is_empty(self) -> bool:
        if self.save_idx == self.read_idx and not self.tab[self.save_idx]:
            return True
        else:
            return False

    def enqueue(self, obj):
        if self.save_idx == 0 and self.read_idx == 0:
            self.tab[self.save_idx] = obj
            self.save_idx += 1
        elif self.read_idx == self.save_idx:
            self.size = self.size * 2
            self.tab = realloc(self.tab, self.size)
            self.tab[self.save_idx] = obj
            self.save_idx += 1
        else:
            if self.save_idx == self.size:
                self.size *= 2
                self.tab = realloc(self.tab, self.size)
            self.tab[self.save_idx] = obj
            self.save_idx += 1

    def dequeue(self):
        if self.is_empty():
            return ValueError
        else:
            self.read_idx += 1
            if self.read_idx == self.save_idx:
                self.read_idx = 0
                return self.tab[self.read_idx]
            else:
                return self.tab[self.read_idx - 1]

    def peek(self):
        if self.tab[self.read_idx] and not self.is_empty():
            return self.tab[self.read_idx]
        else:
            return None

    def __str__(self):
        return str(self.tab)

    def print_queue(self):
        i = 0
        while self.tab[i]:
            print(self.tab[i])
            i += 1

    def print_tab(self):
        return print(self.tab)


def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]

