def print_armstrong_numbers(start, end):
    for num in range(start, end + 1):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            print(num)

# 水仙花数是指一个 n 位数，它的每个位上的数字的 n 次幂之和等于它本身。
# 打印范围内的水仙花数
start = 100
end = 999
print("水仙花数：")
print_armstrong_numbers(start, end)
