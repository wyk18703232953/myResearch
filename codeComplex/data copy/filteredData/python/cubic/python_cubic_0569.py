from collections import Counter

def main(n):
    # 输入规模定义：
    # 构造两个字符串 a, b，长度分别为 n 和 n（或 n-1 以覆盖 len(a) < len(b) 分支）
    # 为了既能覆盖两种情况：当 n 为偶数时令 len(a) < len(b)，当 n 为奇数时令 len(a) >= len(b)

    if n <= 0:
        return

    # 构造字符串 a, b，使用确定性的模式
    # 字符集使用小写字母 'a' 到 'z'
    letters = [chr(ord('a') + (i % 26)) for i in range(max(1, n))]

    if n % 2 == 0:
        # 偶数：len(a) < len(b)
        a_len = max(1, n - 1)
        b_len = n

    else:
        # 奇数：len(a) >= len(b)
        a_len = n
        b_len = max(1, n - 1)

    a = ''.join(letters[i % len(letters)] for i in range(a_len))
    b = ''.join(letters[(i * 2) % len(letters)] for i in range(b_len))

    if len(a) < len(b):
        # print(''.join(sorted(a)[::-1]))
        pass
        return

    cnt = Counter(a)
    n_local = len(a)

    def f(i=0, check=False):
        if i == n_local:
            return []
        for j in sorted(cnt)[::-1]:
            if (check or j <= b[i]) and cnt[j]:
                cnt[j] -= 1
                res = f(i + 1, check or j < b[i])
                if len(res) + i + 1 == n_local:
                    res.append(j)
                    return res
                cnt[j] += 1
        return []

    # print(''.join(f()[::-1]))
    pass
if __name__ == "__main__":
    main(10)