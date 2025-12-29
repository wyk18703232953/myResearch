import random

def main(n: int):
    # 生成规模为 n 的测试数据：随机整数列表
    # 这里假设元素范围为 1 到 10^9
    l = [random.randint(1, 10**9) for _ in range(n)]

    s = list(set(l))
    s.sort()

    if len(s) > 1:
        ans = s[1]
    else:
        ans = 'NO'

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行修改
    main(10)