# 示例数组
arr = [1, 2, 3, 2, 1, 3, 4, 2, 1]

# 创建空字典用于统计频率
frequency = {}

# 遍历数组，统计频率
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# 按值进行降序排序
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print(arr)
# 打印出现次数最多的两个元素
for num, count in sorted_frequency[:2]:
    print("元素 %d 出现次数最多，出现次数为 %d 次" % (num, count))