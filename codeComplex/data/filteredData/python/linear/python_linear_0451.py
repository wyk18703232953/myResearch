def main(n):
    # 这里将 n 直接映射为字符串长度
    # 为保证可扩展并覆盖多种情况，我们根据 n 构造 (n, m, s, t)
    # 保持算法逻辑不变，只是替换输入来源

    if n < 1:
        n = 1

    # 构造 m：让 m 在 n-1, n, n+1 三种情况之间 deterministically 变化
    if n % 3 == 0:
        m = n - 1 if n > 1 else 1
    elif n % 3 == 1:
        m = n

    else:
        m = n + 1

    # 构造 s：
    # 前半部分为字母序列，后半部分包含一个星号及变化部分
    # 这样可以覆盖无 '*' 和有 '*' 两种情况
    if n % 2 == 0:
        # 无 '*' 的情况：纯字母
        s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))

    else:
        # 有 '*' 的情况：在中间位置放一个 '*'
        mid = n // 2
        prefix = ''.join(chr(ord('a') + (i % 26)) for i in range(mid))
        suffix = ''.join(chr(ord('a') + ((i + 1) % 26)) for i in range(n - mid - 1))
        s = prefix + '*' + suffix

    # 构造 t：
    # 基于 s 做可控变形，使得有时匹配，有时不匹配
    if n % 4 == 0:
        # 让 t 与 s 完全相同
        t = s
    elif n % 4 == 1:
        # 在末尾添加一个字符（影响 m 与长度关系）
        base = ''.join(chr(ord('b') + (i % 26)) for i in range(max(n, m)))
        t = base[:m]
    elif n % 4 == 2:
        # 在头部做一个小变动
        if n > 1:
            t = chr((ord(s[0]) - ord('a') + 1) % 26 + ord('a')) + s[1:]

        else:
            t = s

    else:
        # 按照 m 的长度构造不同的字符串，但与 s 有一定前后缀关系
        base = ''.join(chr(ord('c') + (i % 26)) for i in range(max(n, m)))
        t = base[:m]

    # 以下为原始算法逻辑（仅将 input 替换为已构造的 n,m,s,t）
    if n - 1 > m:
        # print('NO')
        pass

    else:
        try:
            a = s.index('*')
        except ValueError:
            a = -1
        if a == -1:
            if s == t:
                # print('YES')
                pass

            else:
                # print('NO')
                pass

        else:
            for i in range(a):
                if i >= len(t) or s[i] != t[i]:
                    # print('NO')
                    pass
                    return
            i = 1
            # 防止负索引越界: 根据 m 和 n 当前约束按原逻辑循环
            while m - i >= a and n - i > a:
                if m - i < 0 or n - i < 0:
                    # print('NO')
                    pass
                    return
                if s[n - i] != t[m - i]:
                    # print('NO')
                    pass
                    return
                i += 1
            # print('YES')
            pass
if __name__ == "__main__":
    # 示例调用：可更改 n 来做规模实验
    main(10)