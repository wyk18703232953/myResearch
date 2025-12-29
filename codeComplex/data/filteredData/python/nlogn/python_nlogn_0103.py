import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里生成一个长度为 n 的随机整数数组，元素范围在 1~10^9
    l = [random.randint(1, 10**9) for _ in range(n)]

    # 原逻辑开始
    l1 = sorted(l)
    c = 0
    for i in range(n):
        if l[i] != l1[i]:
            c += 1
    if c <= 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main，规模可自行修改
    main(5)