import math
from collections import Counter
from collections import defaultdict
# • 如果所有数据都有相同的标签，那么创建一个预测最终结果即为该标签所示的叶节点，
# 然后停止。
# • 如果属性列表是空的（即已经没有更多的问题可提问了），就创建一个预测结果为最常
# 见的标签的叶节点，然后停止。
# • 否则，尝试用每个属性对数据进行划分。
# • 选择具有最低划分熵的那次划分的结果。
# • 根据选定的属性添加一个决策节点。
# • 针对划分得到的每个子集，利用剩余属性重复上述过程。

def entropy(class_probabilities):
    '''给定数据集各个类别所占比例，返回熵'''
    return sum(-p * math.log(p, 2) for p in class_probabilities if p != 0)


def class_probabilities(labels):
    '''给定标签组，返回相应数据集所占比例'''
    total_count = len(labels)
    return [count / total_count for count in Counter(labels).values()]


def data_entropy(labeled_data):
    '''给定数据集，返回数据集的熵'''
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)


def partition_entropy(subsets):
    '''"find the entropy from this partition of data into subsets
 subsets is a list of lists of labeled data'''
    total_count = sum(len(subsets) for subset in subsets)
    return sum(data_entropy(subset) * len(subset) / total_count for subset in subsets)


inputs = [
    ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'no'}, False),
    ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'yes'}, False),
    ({'level': 'Mid', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'R', 'tweets': 'yes', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'R', 'tweets': 'yes', 'phd': 'yes'}, False),
    ({'level': 'Mid', 'lang': 'R', 'tweets': 'yes', 'phd': 'yes'}, True),
    ({'level': 'Senior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, False),
    ({'level': 'Senior', 'lang': 'R', 'tweets': 'yes', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'Python', 'tweets': 'yes', 'phd': 'no'}, True),
    ({'level': 'Senior', 'lang': 'Python', 'tweets': 'yes', 'phd': 'yes'}, True),
    ({'level': 'Mid', 'lang': 'Python', 'tweets': 'no', 'phd': 'yes'}, True),
    ({'level': 'Mid', 'lang': 'Java', 'tweets': 'yes', 'phd': 'no'}, True),
    ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'yes'}, False)
]

def partition_by(inputs, attribute):
    '''每个输入数据是(attribute_dict, label)
    返回一个dict: attribute_value -> inputs'''
    groups = defaultdict(list)
    for input in inputs:
        key = input[0][attribute]   # 得到特定属性的值
        groups[key].append(input)   # 然后把这个输入加到正确的列表中
    return groups

def partition_entropy_by(inputs, attribute):
    '''计算给定部分对应的熵'''
    partitions = partition_by(inputs, attribute)
    return partition_entropy(partitions.values())


if __name__ == '__main__':
    for key in ['level','lang','tweets','phd']:
        print(key, partition_entropy_by(inputs, key))











