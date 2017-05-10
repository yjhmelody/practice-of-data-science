from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# 创建一幅线图，x轴是年份，y轴是gdp
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# 添加一个标题
plt.title("名义GDP")

# 给y轴加标记
plt.ylabel("十亿美元")
plt.show()

##############
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)
plt.xticks([i+0.5 for i, _ in enumerate(movies)], movies)

plt.ylabel('奥斯卡奖数量')
plt.title('我最喜爱的电影')

plt.show()

###############
from collections import Counter

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x for x in histogram.keys()], # 每个条形向左侧移动4个单位
        histogram.values(),                # 给每个条形设置正确的高度
        8)                                 # 每个条形的宽度设置为8

plt.axis([-5, 105, 0, 5])                  # x轴取值从-5到105
                                           # y轴取值0到5

plt.xticks([10 * i for i in range(11)])    # x轴标记为0，10，...，100
plt.xlabel("十分相")
plt.ylabel("学生数")
plt.title("考试分数分布图")
plt.show()

################
variance     = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error  = [x + y for x, y in zip(variance, bias_squared)]
xs = [ i for i, _ in enumerate(variance)]

# 可以多次调用plt.plot以便在同一图上显示多个序列
plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-', label='bias^2')
plt.plot(xs, total_error, 'b:', label='total error')

print(xs)

plt.legend(loc=9)
plt.xlabel('模型复杂度')
plt.title('偏差')

plt.show()

################
friends = [70,  65,  72,  63,  71,  64,  60,  64,  67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# 给点加标记
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),
                    xytext=(5,-5),  #轻微偏离
                    textcoords='offset points') 

plt.title('日分钟数与朋友数')
plt.xlabel('朋友数')
plt.ylabel('花在网站上的日分钟数')

plt.show()































