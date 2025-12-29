import random

def main(n):
    # 生成测试数据：n 个学生，每人 3 门课的分数，0~100 随机
    # 第一个学生作为目标学生
    subjects = 3
    scores = [
        [random.randint(0, 100) for _ in range(subjects)]
        for _ in range(n)
    ]

    rank = 1
    score = sum(scores[0])
    for i in range(1, n):
        student = sum(scores[i])
        if student > score:
            rank += 1
    print(rank)


if __name__ == "__main__":
    # 示例：n = 5
    main(5)