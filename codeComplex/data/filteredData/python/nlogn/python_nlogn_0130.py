import random

def main(n):
    # 根据 n 生成测试数据
    # 假设：
    # - m 取为 n 的 1.5 倍上下浮动一些（避免总是无解或太易解）
    # - k 为 1~10 之间的随机整数
    # - arr 为长度 n 的正整数数组，元素范围 1~20
    m = max(1, int(1.5 * n + random.randint(-n // 2, n // 2)))
    k = random.randint(1, 10)
    arr = [random.randint(1, 20) for _ in range(n)]

    # 按原逻辑处理
    arr.sort()
    arr = arr + [k]
    ans = 0
    s = 0
    # 原代码的 while 条件为 ans < n + 1（因为 ans 从 0 起）
    while ans < n + 1:
        s += arr[-ans-1]
        if s >= m:
            break
        ans += 1
        s -= 1

    if s >= m:
        print(ans)
    else:
        print("-1")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)