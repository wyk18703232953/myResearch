import random

def main(n):
    # 生成规模为 n 的测试数据（范围可自行调整）
    a = [random.randint(1, 100) for _ in range(n)]

    # 原逻辑开始
    l = list(set(a))
    l.sort()
    if len(l) >= 2:
        print(l[1])
    else:
        print("NO")

if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    main(10)