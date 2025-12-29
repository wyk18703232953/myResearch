import random

def main(n: int) -> None:
    # 根据 n 生成测试数据
    # 为保证逻辑正常运行，需要 s >= 0
    # 这里令 s 在 [0, n*(n+1)//2] 范围内随机生成
    s = random.randint(0, n * (n + 1) // 2)

    ans = 0
    cur_n = n
    cur_s = s

    while cur_s > 0 and cur_n > 0:
        a = cur_s // cur_n
        cur_s -= cur_n * a
        ans += a
        cur_n -= 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)