def main(n):
    rank = 1
    # 第一名的成绩，确定性构造：分数和为 3*n
    score = sum((i % 7 + 1) for i in range(3 * n))
    # 生成其余 n-1 个学生的成绩
    for i in range(n - 1):
        student = sum(((i + j) % 7 + 1) for j in range(3 * n))
        if student > score:
            rank += 1
    # print(rank)
    pass
if __name__ == "__main__":
    main(10)