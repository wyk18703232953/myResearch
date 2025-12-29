import random

def main(n: int):
    # 生成规模为 n 的测试数据（整数列表），数值范围可根据需要调整
    l = [random.randint(1, 1000000) for _ in range(n)]

    # 原逻辑开始
    l = set(l)
    l = list(l)

    if len(l) <= 1:
        print("NO")
        return

    l.sort()
    print(l[1])


if __name__ == "__main__":
    # 示例：可在此处修改 n 以运行不同规模测试
    main(5)