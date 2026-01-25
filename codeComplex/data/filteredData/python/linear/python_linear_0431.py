def main(n):
    # 生成确定性的成绩数据
    # 第一名学生的成绩
    score_list = [i % 101 for i in range(1, 6)]
    score = sum(score_list)

    rank = 1
    # 生成其余 n-1 名学生的成绩并计算名次
    for i in range(1, n):
        # 每个学生 5 门课，成绩确定性构造
        student_scores = [((i + j) * 7) % 101 for j in range(5)]
        student = sum(student_scores)
        if student > score:
            rank += 1

    print(rank)


if __name__ == "__main__":
    main(10)