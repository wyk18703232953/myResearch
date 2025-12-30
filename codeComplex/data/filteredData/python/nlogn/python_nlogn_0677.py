import random

def main(n):
    # 生成测试数据
    # n: 男生人数
    # m: 女生人数，设为与 n 同量级，这里取 m = n 或至少 1
    m = max(1, n)
    # 生成男生值：1~100 的随机整数
    boys_out = sorted([random.randint(1, 100) for _ in range(n)], reverse=True)
    # 生成女生值：保证 >= max(boys_out)，否则原逻辑会直接输出 -1 退出
    max_boy = max(boys_out) if boys_out else 0
    girls_in = sorted([random.randint(max_boy, max_boy + 100) for _ in range(m)])

    # 原始逻辑
    if n == 0:
        print(-1)
        return

    ans = 0
    for boy in boys_out:
        ans += boy * m

    count = 0
    i = 0
    for girl in girls_in:
        if girl < max_boy:
            print(-1)
            return

        if girl > max_boy:
            if count == m - 1:
                count = 0
                i += 1
            if i >= n:
                print(-1)
                return
            ans += girl - boys_out[i]
            count += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(5)