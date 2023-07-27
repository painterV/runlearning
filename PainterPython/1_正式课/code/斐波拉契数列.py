def fibonacci(n):
    sequence = [0, 1]  # 前两个数为0和1
    for i in range(2, n):
        next_num = sequence[i - 1] + sequence[i - 2]  # 计算下一个数
        sequence.append(next_num)
    return sequence

# 输入要计算的斐波那契数列长度
n = int(input("请输入要计算的斐波那契数列长度："))

# 调用函数计算斐波那契数列
fib_seq = fibonacci(n)

# 打印斐波那契数列
print("斐波那契数列：")
print(fib_seq)