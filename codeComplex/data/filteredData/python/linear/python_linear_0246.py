def main(n):
    # 确定性地从 n 生成 (n_orig, k)
    if n < 3:
        n_orig = 3
    else:
        n_orig = n

    # 设计一个确定性的 k，使得既能覆盖偶数也能覆盖奇数等多种情况
    if n_orig % 4 == 0:
        k = (n_orig // 2) * 2  # 偶数 k，触发第一分支
    elif n_orig % 4 == 1:
        k = max(1, (n_orig // 2) | 1)  # 奇数且较小，触发第二分支
    else:
        k = n_orig + 1  # 使 k > n-2，触发第三分支逻辑

    # 下面是原始算法逻辑（去掉 input）
    n_val = n_orig
    k_val = k

    if k_val % 2 == 0:
        s = "."
        s = s + "#" * (k_val // 2)
        s = s + "." * (n_val - len(s))
        print("YES")
        print("." * n_val)
        print(s)
        print(s)
        print("." * n_val)
    else:
        if k_val <= n_val - 2:
            a = "#" * k_val
            s = "." * ((n_val - k_val) // 2) + a + "." * ((n_val - k_val) // 2)
            print("YES")
            print("." * n_val)
            print(s)
            print("." * n_val)
            print("." * n_val)
        else:
            k_val = k_val - n_val + 3
            a = "#" * k_val
            s = "." * ((n_val - k_val) // 2) + a + "." * ((n_val - k_val) // 2)
            print("YES")
            print("." * n_val)
            print("." + "#" * (n_val - 2) + ".")
            s = list(s)
            s[n_val // 2] = "."
            s = "".join(s)
            print(s)
            print("." * n_val)


if __name__ == "__main__":
    main(10)