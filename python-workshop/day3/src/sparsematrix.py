from collections import defaultdict


class SparseMatrix(object):
    def __init__(self, n, m, default=0):
        self.n = n
        self.m = m
        self.mat = defaultdict(dict)
        self.default = default
