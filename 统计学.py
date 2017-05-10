import math
from collections import Counter
from matplotlib import pyplot as plt

num_friends = [100, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6,
               6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]


def make_histogram(plt, x, y, **kw):
    plt.bar(x, y)
    plt.axis([min(x)-2, max(x), min(y), max(y)*1.2])
    if kw.get('title'):
        plt.title(kw.get('title'))
    if kw.get('xlabel'):
        plt.xlabel(kw.get('xlabel'))
    if kw.get('ylabel'):
        plt.ylabel(kw.get('ylabel'))
    plt.show()

def make_friend_histogram(plt):
    friend_counts = Counter(num_friends)
    # x-axis
    xs = range(101)
    # y-axis
    ys = [friend_counts[x] for x in xs]

    plt.bar(xs, ys)
    plt.axis([0, 101, 0, 25])
    plt.title('Histogram of friend counts')
    plt.xlabel('# of friend')
    plt.ylabel('# of people')
    plt.show()


def mean(x):
    '''返回平均值'''
    return sum(x) / len(x)


def median(x):
    '''返回中位数'''
    num = len(x)
    sorted_x = sorted(x)
    midpoint = num // 2

    if num % 2 == 1:
        return sorted_x[midpoint]
    else:
        return (sorted_x[midpoint] + sorted_x[midpoint - 1]) / 2


def quantile(x, p):
    '''返回分位数(表示少于数据中特定百分比的一个值'''
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def mode(x):
    '''返回众数'''
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


def data_range(x):
    '''返回极差'''
    return max(x) - min(x)


def de_mean(x):
    '''返回x减去它的平均值'''
    x_mean = mean(x)
    return [x_i - x_mean for x_i in x]


def variance(x):
    '''返回x的方差'''
    num = len(x)
    # 偏差
    deviations = de_mean(x)
    return sum([value * value for value in deviations]) / (num - 1)


def standard_deviation(x):
    '''返回标准差'''
    return math.sqrt(variance(x))


# 一种更加稳健的方案是计算 75% 的分位数和 25% 的分位数之差
def interquartile_range(x):
    '''计算 75% 的分位数和 25% 的分位数之差'''
    return quantile(x, 0.75) - quantile(x, 0.25)


def covariance(x, y):
    '''返回x和y的协方差'''
    num = len(x)
    deviations_x = de_mean(x)
    deviations_y = de_mean(y)
    # 点乘
    return sum([v * w for v, w in zip(deviations_x, deviations_y)]) / (num - 1)

# 它的单位是输入单位的乘积（即朋友 - 分钟 - 每天），
# 难于理解。（“朋友 - 分钟 - 每天”是什么鬼？）
# 因此，相关是更常受到重视的概念，它是由协方差除以两个变量的标准差
# 相关系数没有单位，它的取值在 -1（完全反相关）和 1（完全相关）之间。
# 相关值 0.25 代表一个相对较弱的正相关
def correlation(x, y):
    '''返回x和y的相关系数'''
    stddev_x = standard_deviation(x)
    stddev_y = standard_deviation(y)
    if stddev_x > 0 and stddev_y > 0:
        return covariance(x, y) / stddev_x / stddev_y
    else:
        return 0


# 进行随机试验是证实因果关系的可靠性的一个好方法。
# 你可以先将一组具有类似的统计数据的用户随机分为两组，
# 再对其中一组施加稍微不同的影响因素，然后你会发现，
# 不同的因素会导致不同的结果。



if __name__ == '__main__':
    make_friend_histogram(plt)
    make_histogram(plt, num_friends, 
    daily_minutes,title='plt', xlabel='friends',ylabel='233')

    num_points = len(num_friends)       # 204
    largest_value = max(num_friends)    # 100
    smallest_value = min(num_friends)   # 1

    print(num_points, largest_value, smallest_value)
    print('mean', mean(num_friends))
    print('median', median(num_friends))
    print('quantile', quantile(num_friends, 0.1))
    print('mode', mode(num_friends))
    print('data_range', data_range(num_friends))
    print('variance', variance(num_friends))
    print('standard_deviation', standard_deviation(num_friends))
    print('interquartile_range', interquartile_range(num_friends))
    print('covariance', covariance(num_friends, daily_minutes))
    print('correlation', correlation(num_friends, daily_minutes))
