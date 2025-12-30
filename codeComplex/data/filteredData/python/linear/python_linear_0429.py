import random

def main(n: int):
    # 生成测试数据：n 个参赛者，每个参赛者有随机科目数与成绩
    # 为保证 Thomas 是第 1 个，his_scores 单独生成
    num_subjects_thomas = random.randint(1, 5)
    his_scores = [random.randint(0, 100) for _ in range(num_subjects_thomas)]
    S = [sum(his_scores)]

    # 其余 n-1 个参赛者
    for _ in range(n - 1):
        num_subjects = random.randint(1, 5)
        scores = [random.randint(0, 100) for _ in range(num_subjects)]
        S.append(sum(scores))

    # 以下为原逻辑
    if S[0] == max(S):
        print("1")
        return

    thomas = S[0]
    rank = 1
    S.sort(reverse=True)
    for total in S:
        if total == thomas:
            print(rank)
            return
        else:
            rank += 1

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)