import random

def main(n):
    # 生成规模为 n 的测试数据：正整数列表
    # 可按需修改生成规则
    a = [random.randint(1, 10 * n if n > 0 else 10) for _ in range(n)]

    a.sort()
    tot = 0
    d = {}
    for i in range(len(a)):
        if a[i] not in d:
            tot += 1
            for j in range(i + 1, len(a)):
                if a[j] % a[i] == 0:
                    d[a[j]] = 1
    print(tot)

if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用中可自行调整 n
    main(10)