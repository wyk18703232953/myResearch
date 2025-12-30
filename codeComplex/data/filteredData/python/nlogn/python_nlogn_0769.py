import random

def main(n: int):
    # 生成测试数据：随机选择测试组数 c
    c = random.randint(1, 10)

    for _ in range(c):
        # 为当前测试组生成长度为 n 的数组 s，元素范围可自行调整
        s = [random.randint(1, 10**9) for _ in range(n)]
        s.sort()
        l = min(s[-1], s[-2])
        ans = min(l - 1, n - 2)
        print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 10，可根据需要修改
    main(10)