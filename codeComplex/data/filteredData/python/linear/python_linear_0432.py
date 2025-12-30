import random

def main(n: int):
    # 生成测试数据：n 个学生，每人随机 3 门课成绩（0~100）
    # 默认第一个学生为“目标学生”
    num_subjects = 3
    scores = [
        [random.randint(0, 100) for _ in range(num_subjects)]
        for _ in range(n)
    ]

    # 计算目标学生总分
    target_score = sum(scores[0])
    rank = 1

    # 统计有多少学生总分严格大于目标学生
    for i in range(1, n):
        student_score = sum(scores[i])
        if student_score > target_score:
            rank += 1

    print(rank)


if __name__ == "__main__":
    # 示例：n=5，可根据需要修改或在其他模块中调用 main(n)
    main(5)