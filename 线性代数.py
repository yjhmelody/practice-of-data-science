# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 18:29:22 2017

@author: yjh46
"""
import math
from pprint import pprint as print

# 向量


def vector_add(v, w):
    '''向量加法'''
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    '''向量减法'''
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    '''一系列向量加法'''
    return (vector_add, vectors)
# from functools import partial
# vector_sum = partial(reduce, vector_add)

# print(vector_sum([[1,2],[3,4]]))


def scalar_mulitply(c, v):
    '''标量乘以向量'''
    return [c * v_i for v_i in v]


def dot(v, w):
    '''点乘'''
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    '''向量平方和'''
    return dot(v, v)


def magnitude(v):
    '''求向量长度'''
    math.sqrt(dot(v, v))


def distance(v, w):
    '''2个向量距离'''
    return magnitude(vector_subtract(v, w))

# 矩阵


def shape(A):
    '''返回矩阵的形状:行数列数'''
    return len(A), len(A[0]) if A else 0  # 第一行中元素的个数


def get_row(A, i):
    '''返回第i行'''
    return A[i]


def get_col(A, j):
    '''返回第j列'''
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
   whose (i,j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def is_diagonal(i, j):
    return 1 if i == j else 0


identity_matrix = make_matrix(5, 5, is_diagonal)

print(identity_matrix)
