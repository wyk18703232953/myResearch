def main(n):
    # 1) 构造 n, m
    # 保证 m 在 [1, 2n] 且 m >= 1
    if n < 1:
        n = 1
    m = n * 2

    # 2) 构造模式串 s（带或不带 *），长度为 n
    # 结构：前半一段 a，若 n>=3，在中间放一个 *，后面一段 b
    # 每个字符由 (i % 3) 决定，确保完全确定性
    if n == 1:
        # 单字符模式：在 'a' 和 '*' 之间切换
        s = 'a' if (n % 2 == 0) else '*'
    else:
        chars = ['a', 'b', 'c']
        pre_len = n // 2
        suf_len = n - pre_len - 1 if n >= 3 else 0  # 预留 1 位给 '*'
        prefix = ''.join(chars[i % 3] for i in range(pre_len))
        suffix = ''.join(chars[(i + 1) % 3] for i in range(suf_len))
        if n >= 3:
            s = prefix + '*' + suffix
        else:
            # n == 2 时构造无 '*' 的模式
            s = ''.join(chars[i % 3] for i in range(n))

    # 3) 构造目标串 t，长度为 m
    # 用另一种确定性规则生成
    chars2 = ['x', 'y', 'z']
    t = ''.join(chars2[(i + n) % 3] for i in range(m))

    # 为了让程序在不同 n 下既可能 YES 也可能 NO，
    # 我们对部分 n 做微调使其匹配成功
    # 下面的调整对算法逻辑无影响，只改变输入数据
    if '*' not in s:
        # 当没有 * 时，偶数 n 时让 s == t[:n]，奇数 n 保持不匹配
        if n % 2 == 0:
            t = s
    else:
        # 有 * 的情况，针对某些 n 调整 t 使其匹配
        if n % 3 == 0:
            s_list = list(s)
            ind = s_list.index('*')
            prefix = ''.join(s_list[:ind])
            suffix = ''.join(s_list[ind + 1:])
            # 构造满足条件的 t：前 ind 位为 prefix，后 len(suffix) 位为 suffix
            # 中间填 'x'
            middle_len = m - ind - len(suffix)
            if middle_len < 0:
                middle_len = 0
            t = prefix + ('x' * middle_len) + suffix
        elif n == 1 and s == '*':
            # 已经必然 YES，不需要调整
            pass

    # 4) 保持原有逻辑，移除所有输入依赖，改用已经构造好的 n, m, s, t
    if '*' not in s:
        if s == t:
            print('YES')
        else:
            print('NO')
    elif n > m + 1:
        print('NO')
    elif n == 1 and s == '*':
        print('YES')
    else:
        s_list = list(s)
        t_list = list(t)
        if s_list[0] == '*':
            if s_list[1:] == t_list[-(len(s_list[1:])):]:
                print('YES')
            else:
                print('NO')
        elif s_list[-1] == '*':
            if s_list[:n - 1] == t_list[:n - 1]:
                print('YES')
            else:
                print('NO')
        else:
            ind = s_list.index('*')
            if s_list[:ind] == t_list[:ind] and s_list[ind + 1:] == t_list[-len(s_list[ind + 1:]):]:
                print('YES')
            else:
                print('NO')


if __name__ == "__main__":
    # 示例：运行若干规模，以便做时间复杂度实验时手动修改
    for size in [1, 2, 3, 5, 10]:
        main(size)