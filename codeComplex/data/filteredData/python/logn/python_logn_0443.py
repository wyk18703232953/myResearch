def main(n):
    """
    按原逻辑构造测试数据并执行。
    这里约定：
    - 构造 t = n 组测试
    - 对于第 i 组：令 n_i = i+1
      * 若 n_i > 31: 令 k_i = 1（保证直接 YES 分支）
      * 否则：取 k_i = min( (4**n_i - 1)//3, i+1 )
    """

    t = n  # 测试组数
    for case_id in range(t):
        ni = case_id + 1  # 让 n 从 1,2,...,n 变化

        if ni > 31:
            # 任意正 k 都会直接走 YES 分支
            ki = 1
        else:
            limit = (4**ni - 1) // 3
            # 取一个不太极端的 k，尽量在可行范围内
            ki = min(limit, case_id + 1)
            if ki <= 0:
                ki = 1

        n_val = ni
        k_val = ki

        # 以下是原始逻辑，仅将 input/print 改成使用 n_val, k_val
        n = n_val
        k = k_val

        if n > 31:
            print("YES", n - 1)
            continue
        else:
            if k > (4**n - 1) // 3:
                print("NO")
                continue

        l = (4**n - 1) // 3
        i = 1
        j = 0
        k1 = k
        while i <= n:
            k -= (2**i - 1)
            j = i
            if k < 0:
                j = j - 1
                k += (2**i - 1)
                break
            i += 1
        k2 = k1 - k
        k3 = (2**(j + 1) - 1) * ((4**(n - j) - 1) // 3)

        if l - k2 - k3 >= k:
            print("YES", n - i + 1)
        else:
            print("NO")


# 示例调用
if __name__ == "__main__":
    main(5)