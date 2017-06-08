# 我们用 P(E ) 来标记“事件 E 的概率”
# 如果事件 E 与事件 F 独立，那么定义式如下：
# P(E, F)=P(E)P(F)
# 如果两者不一定独立（并且 F 的概率不为零），那么 E 关于 F 的条件概率式如下：
# P(E|F)=P(E, F)/P(F)
# 条件概率可以理解为，已知 F 发生，E 会发生的概率。
# 更常用的公式是上式的变形：
# P(E, F)=P(E|F)P(F)
# 如果 E 和 F 独立，则上式应该表示为：
# P(E|F)=P(E)
# 这个数学公式意味着，F 是否发生并不会影响 E 是否发生的概率。

# 如果我们假设：
# (1) 每个孩子是男孩和是女孩的概率相同
# (2) 第二个孩子的性别概率与第一个孩子的性别概率独立
# 那么，事件“没有女孩”的概率是 1/4，事件“一个男孩，一个女孩”的概率为 1/2，事件“两个女孩”的概率为 1/4。
# 现在，我们的问题是，事件 B“两个孩子都是女孩”关于事件 G“大孩子是女孩”的条件概率是多少？用条件概率的定义式进行计算如下：
# P(B|G)=P(B,G)/P(G)=P(B)/P(G)=1/2
# 事件 B 与 G 的交集（“两个孩子都是女孩并且大孩子是女孩”）刚好是事件 B 本身。（一旦你知道两个孩子都是女孩，那大孩子必然是女孩。）
# 这个结果大致上符合你的直觉。
# 我们接着再问，事件“两个孩子都是女孩”关于事件“至少一个孩子是女孩”（L）的条件概率是多少？出乎意料的是，结果异于前问。
# 与前问相同的是，事件 B 和事件 L 的交集（“两个孩子都是女孩，并且至少一个孩子是女孩”）刚好是事件 B。这意味着：
# P(B|L)=P(B,L)/P(L)=P(B)/P(L)=1/3
# 为什么会有这样的结果？如果你已知至少一个孩子是女孩，那么这个家庭有一个男孩和一个女孩的概率是有两个女孩的两倍。


import random
import math
from collections import Counter
from matplotlib import pyplot as plt


def random_kid():
    return random.choice(['boy', 'girl'])


both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0.1)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == 'girl':
        older_girl += 1
    if older == 'girl' and younger == 'girl':
        both_girls += 1
    if older == 'girl' or younger == 'girl':
        either_girl += 1

# 贝叶斯定理
# P(E|F)=P(E,F)/P(F)=P(F|E)P(E)/P(F)

# probability distribution function


# 均匀分布的密度函数
def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

# 正态分布 它是典型的钟型曲线形态分布函数，可以完全由两个参数决定：
# 均值 μ（mu）和标准差 σ（sigma）


def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(math.pi * 2)
    exp = math.exp(-(x - mu)**2 / 2 / sigma**2)
    return exp / (sqrt_two_pi * sigma)


def test_normal_pdf():
    xs = [x / 10 for x in range(-50, 50)]
    plt.plot(xs, [normal_pdf(x, sigma=1)
                  for x in xs], '-', label='mu=0, sigma=1')
    plt.plot(xs, [normal_pdf(x, sigma=2)
                  for x in xs], '--', label='mu=0, sigma=2')
    plt.plot(xs, [normal_pdf(x, sigma=0.5)
                  for x in xs], ':', label='mu=0,sigma=0.5')
    plt.plot(xs, [normal_pdf(x, mu=-1)
                  for x in xs], '-.', label='mu=-1, sigma=1')
    plt.legend()
    plt.title('多个正态分布的概率密度函数')
    plt.show()


# 如果 Z 是服从标准正态分布的随机变量，则有如下转换式：
# X=σZ+μ
# 其中 X 也是正态分布，但均值是 μ，标准差是σ
# 相反，如果 X 是均值为 μ 标准差为σ 的正态分布，那么：
# Z=(X-μ)/σ
# 是标准正态分布的随机变量。

# 标准正态分布的累积分布函数无法用“基本”的解析形式表示，
# 但在 Python 中可以用函数 math.erf 描述

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def test_normal_cdf():
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_cdf(x, sigma=1)
                  for x in xs], '-', label='mu=0,sigma=1')
    plt.plot(xs, [normal_cdf(x, sigma=2)
                  for x in xs], '--', label='mu=0,sigma=2')
    plt.plot(xs, [normal_cdf(x, sigma=0.5)
                  for x in xs], ':', label='mu=0,sigma=0.5')
    plt.plot(xs, [normal_cdf(x, mu=-1)
                  for x in xs], '-.', label='mu=-1,sigma=1')
    plt.legend(loc=4)  # 底部右边
    plt.title("多个正态分布的累积分布函数")
    plt.show()

# 以求出特定的概率的相应值


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    '''用二分查找查找特定概率的近似值'''
    # 如果是非标准正态分布，先转换
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    # normal_cdf(-10)非常接近0
    low_z, low_p = -10, 0
    # normal_cdf(10)非常接近1
    hi_z, hi_p = 10, 1
    while hi_z - low_z > tolerance:
        mid_z = (hi_z + low_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            # mid太低，查找更大的值
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # mid太高，查找更小的值
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z

# 中心极限定理 central limit theorem
# 一个定义为大量独立同分布的随机变量的均值的随机变量本身就是接近于正态分布的
# 如果 x1,…,xn 都是均值为 μ、标准差为σ 的随机变量，且 n 很大
# 那么 (x1+……+xn)/n 近似正态分布，且均值为 μ，标准差为 σ / n
# 等价于 ((x1+………+xn) - μn) / (σ*sqrt(n))，近似标准正态分布

# 伯努利实验


def bernoulli_trial(p):
    return 1 if random.random() < p else 0

# 二项式分布


def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))


def make_hist(n, p, num_points):
    data = [binomial(n, p) for _ in range(num_points)]
    # 用条形图绘制出实际的二项式样本
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()], 0.8, color='0.75')
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # 线形图绘制正态近似
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) -
          normal_cdf(i + 0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    plt.title('二项分布与正态近似')
    plt.show()


if __name__ == '__main__':
    print('P(both | older):', both_girls / older_girl)
    print('P(both | either):', both_girls / either_girl)
    # test_normal_pdf()
    # test_normal_cdf()
    print(inverse_normal_cdf(0.8438, tolerance=0.001))
    make_hist(100, 0.75, 10000)
