import random

def main(n):
    # 这里的 n 表示测试组数
    # 根据 n 自动生成测试数据并执行原逻辑
    for _ in range(n):
        # 随机生成 p（数组长度），保证 p >= 2
        p = random.randint(2, 20)
        # 随机生成数组 a，长度为 p，元素为 1~100 的整数
        a = [random.randint(1, 100) for _ in range(p)]

        # 原逻辑开始
        a_sorted = sorted(a)
        if p == 2:
            print(0)
            continue
        k = a_sorted[-2] - 1
        print(min(k, p - 2))

if __name__ == "__main__":
    # 示例：运行 5 组测试
    main(5)