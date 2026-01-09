def main(n):
    # 映射含义：
    # n: 字符串 b 的长度，字符串 a 的长度为 n 或 n+1（如果包含通配符 *）
    # 构造方式完全确定性，不依赖外部输入

    # 构造 b 为长度为 n 的小写字母序列（循环 'a' 到 'z'）
    b = ''.join(chr(ord('a') + (i % 26)) for i in range(n))

    # 构造 a：
    # 为了同时覆盖有 '*' 和无 '*' 两种情况：
    # 若 n 为偶数：构造包含 '*' 的模式
    # 若 n 为奇数：构造不包含 '*' 的完整字符串
    if n == 0:
        # 边界情况：n=0
        a = ""
        m = 0

    else:
        if n % 2 == 0:
            # 有通配符的情况：
            # a 形如 prefix + '*' + suffix
            # prefix 长度为 n//2，suffix 长度为 n//4
            # 如果 n 太小（比如 2），suffix 可能为 0 长度
            prefix_len = n // 2
            suffix_len = n // 4

            prefix = ''.join(chr(ord('a') + ((i * 3) % 26)) for i in range(prefix_len))
            suffix = ''.join(chr(ord('a') + ((i * 5 + 1) % 26)) for i in range(suffix_len))

            a = prefix + '*' + suffix
            m = len(a)

        else:
            # 无通配符的情况：a 与 b 相同长度
            a = ''.join(chr(ord('a') + ((i * 7 + 2) % 26)) for i in range(n))
            m = len(a)

    # 下面是原算法逻辑（去除所有输入依赖）
    flag = 0
    for c in a:
        if c == '*':
            flag = 1
    if flag == 1:
        a1, a2 = a.split('*')
        Len1 = len(a1)
        Len2 = len(a2)
        b1 = b[:Len1]
        b2 = ''
        if Len2:
            b2 = b[-Len2:]
        if a1 == b1 and a2 == b2 and Len1 + Len2 <= len(b):
            # print('YES')
            pass

        else:
            # print('NO')
            pass

    else:
        if a == b:
            # print('YES')
            pass

        else:
            # print('NO')
            pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 进行规模化实验
    main(10)