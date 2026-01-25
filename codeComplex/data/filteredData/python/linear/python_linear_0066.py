def main(n):
    # 生成确定性的 s 值
    s = n * 2
    ans = s

    # 生成 n 组确定性的 (f, t)
    # 让 f 和 t 随 i 变化，但保持完全确定性
    for i in range(n):
        f = i % (n + 1)  # 保证 f 不会太大
        t = (i * 3) % (2 * n + 3)  # 保证 t 有一定变化
        if t > (s - f):
            ans += t - (s - f)
            s += t - (s - f)

    return ans


if __name__ == "__main__":
    # 示例调用
    print(main(10))