# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 11:10:19 2017

@author: yjh46
"""

from functools import partial
from matplotlib import pyplot as plt

# 我们常常需要最大化（或最小化）这个函数。这意味着我们需要找出能计算出最大
#（或最小）可能值的输入 v

def sum_of_squares(v):
    '''计算元素的平方和'''
    return sum(v_i ** 2 for v_i in v)

# 梯度（在微积分里，这表示偏导数向量）给出了输入值的方向，
# 在这个方向上，函数增长得最快
# 相应地，最大化函数的算法首先从一个随机初始点开始，计算梯度，在梯度方向（这是使
# 函数增长最快的一个方向）上跨越一小步，再从一个新的初始点开始重复这个过程。同
# 样，你也可以在相反方向上逐步最小化函数

def difference_quotient(f, x, h):
    '''f是单变量函数，在x点上的导数，其中h趋向于0'''
    return (f(x + h) - f(x)) / h
def plot_estimated_derivative():    
    def square (x):
        return x * x
    
    def derivative(x):
        return 2 * x
    
    derivative_estimate = lambda x: difference_quotient(square, x, h=0.00001)
    
    x = range(-10, 10)
    plt.title('精确的倒数值和估计值')
    plt.plot(x, map(derivative, x), 'rx', label='Actual')   # x
    plt.plot(x, map(derivative_estimate, x), 'b+', label='Estimate')    #+
    # plt.legend(loc=9)
    plt.show()















