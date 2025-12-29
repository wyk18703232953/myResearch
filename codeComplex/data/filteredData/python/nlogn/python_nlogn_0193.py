import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数序列
    # 这里生成 [-10^6, 10^6] 范围的随机整数，可按需要自行修改
    arr = [random.randint(-10**6, 10**6) for _ in range(n)]

    a = {}
    ans = 0
    s = 0
    i = 0
    for t in arr:
        s += t
        a[t] = a.get(t, 0) + 1

        cnt_t = a.get(t, 0)
        cnt_t_minus = a.get(t - 1, 0)
        cnt_t_plus = a.get(t + 1, 0)

        ans += (i - cnt_t - cnt_t_minus - cnt_t_plus + 1) * t - (
            s - cnt_t * t - cnt_t_minus * (t - 1) - cnt_t_plus * (t + 1)
        )
        i += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)