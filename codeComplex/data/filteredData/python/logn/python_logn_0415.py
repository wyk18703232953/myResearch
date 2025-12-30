def main(n):
    # 预处理 lst 序列
    lst = [0, 1]
    now = 1
    while now <= 1e25:
        now = now * 4 + 1
        lst.append(now)

    # 根据规模 n 生成测试数据：
    # 这里示例生成 t = n 个测试，用一些可覆盖多种情况的 (n_i, k_i)
    # 可按需求调整生成策略
    tests = []
    for i in range(1, n + 1):
        # n_i 在 1~40 之间循环（包含边界与大于34的情况）
        ni = (i % 40) + 1
        # k_i 取一个随 ni 变化的值，使得既有小也有大
        ki = (1 << (min(ni, 30))) - 1  # 不会溢出，同时足够大
        tests.append((ni, ki))

    # 模拟原逻辑
    for ni, k in tests:
        if ni >= 34:
            print("YES " + str(ni - 1))
            continue

        sek = 0
        ambil = 1
        nyak = 0
        cnt = 0
        sudah = False

        while sek < ni:
            cnt = cnt + (1 << (sek + 1)) - 1
            if cnt > k:
                print("NO")
                sudah = True
                break

            next_ambil = (ambil + 1) * 2 - 1
            sisa = 4 * ambil - next_ambil
            ambil = next_ambil

            sek += 1
            nyak = nyak + sisa * lst[ni - sek]
            if (nyak + cnt) >= k:
                print("YES " + str(ni - sek))
                sudah = True
                break

        if not sudah:
            print("NO")


if __name__ == "__main__":
    # 示例调用：规模 n=5
    main(5)