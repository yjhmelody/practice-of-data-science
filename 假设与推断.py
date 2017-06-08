import math
from matplotlib import pyplot as pyplot

# 正态分布的分布函数
def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# 正态分布拟合二项式随机变量
def normal_approximation_to_binomial(n, p):
    '''找到对应二项式分布变量(n,p)的mu和sigma'''
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma
    
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


# 正态cdf是一个变量在一个阈值以下的概率
normal_probability_below = normal_cdf 

# 如果它不在阈值以下，就在阈值以上
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

# 在lo和hi区间之内
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# 在lo和hi区间之外
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

def normal_upper_bound(p, mu=0, sigma=1):
    '''返回P(Z <= z)==p对应的z值'''
    return inverse_normal_cdf(p, mu, sigma)

def normal_lower_bound(p, mu=0, sigma=1):
    '''返回P(Z >= z)==p对应的z值'''
    return inverse_normal_cdf(1-p, mu, sigma)
    
def normal_two_sided_bounds(p, mu=0, sigma=1):
    '''返回包含特定p值对称边界'''
    tail_p = (1 - p) / 2
    
    upper_bound = normal_lower_bound(tail_p, mu, sigma)

    lower_boubd = normal_upper_bound(tail_p, mu, sigma)
    
    return lower_boubd, upper_bound

if __name__ == '__main__':    
    print(normal_probability_between(-5, 5))