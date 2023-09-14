import random

# 生成学生成绩表
def generate_grades(num_students):
    grades = []
    for i in range(num_students):
        student_id = i + 1
        math_grade = random.randint(50, 100)
        english_grade = random.randint(50, 100)
        chinese_grade = random.randint(50, 100)
        python_grade = random.randint(50, 100)
        grades.append((student_id, math_grade, english_grade, chinese_grade, python_grade))
    return grades

# 将成绩表写入文本文件
def write_grades_to_file(grades, filename):
    with open(filename, "w") as file:
        file.write('学号,数学,英语,语文,python\n')
        for grade in grades:
            line = ",".join(str(x) for x in grade) + "\n"
            file.write(line)

# 主函数
if __name__ == "__main__":
    num_students = 200
    grades = generate_grades(num_students)
    write_grades_to_file(grades, "grades.txt")
