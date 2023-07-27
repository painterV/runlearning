def generate_pascal_triangle(num_rows):
    triangle = []
    for i in range(num_rows):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = triangle[i - 1]
                value = prev_row[j - 1] + prev_row[j]
                row.append(value)
        triangle.append(row)
    return triangle

def print_pascal_triangle(triangle):
    print("打印杨辉三角")
    for row in triangle:
        print(' '.join(map(str, row)))

# 生成并打印杨辉三角形的前 10 行
num_rows = 10
triangle = generate_pascal_triangle(num_rows)
print_pascal_triangle(triangle)