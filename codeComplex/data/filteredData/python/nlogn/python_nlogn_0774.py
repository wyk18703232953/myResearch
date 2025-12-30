import random

def main(n):
    # 1. 生成测试数据 a（长度为 n 的整数数组）
    # 数据范围可按需调整，这里取 [-10, 10]
    a = [random.randint(-10, 10) for _ in range(n)]

    # 原逻辑开始
    s = sorted(a)
    q = a.index(max(a))
    q1, q = min(len(a) - 1, q + 1), max(0, q - 1)
    for q2 in range(len(a) - 2, -1, -1):
        if a[q] == s[q2]:
            q = max(0, q - 1)
        elif a[q1] == s[q2]:
            q1 = min(len(a) - 1, q1 + 1)
        else:
            print("NO")
            break
    else:
        print("YES")


if __name__ == "__main__":
    # 示例调用：n 可根据需要修改
    main(10)