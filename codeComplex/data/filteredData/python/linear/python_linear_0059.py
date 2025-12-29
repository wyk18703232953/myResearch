import random
import string


def main(n: int):
    # 生成测试数据：两个长度为 n 的小写字母串 s 和 t
    # 保证字符来自 'a' 到 'z'
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    t = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    p = [-1, -1]
    a = [[-1] * 26 for _ in range(26)]
    k = 0

    # 统计不相同的位置数
    for i in range(n):
        if t[i] != s[i]:
            k += 1

    # 优先寻找能一次交换修复2个不同位置的情况
    for i in range(n):
        if t[i] != s[i]:
            if a[ord(t[i]) - 97][ord(s[i]) - 97] != -1:
                print(k - 2)
                print(a[ord(t[i]) - 97][ord(s[i]) - 97] + 1, i + 1)
                return
            a[ord(s[i]) - 97][ord(t[i]) - 97] = i

    # 其次寻找能一次交换修复1个不同位置的情况
    for i in range(n):
        if t[i] != s[i]:
            for j in range(26):
                if a[j][ord(s[i]) - 97] != -1:
                    print(k - 1)
                    print(a[j][ord(s[i]) - 97] + 1, i + 1)
                    return
            a[ord(s[i]) - 97][ord(t[i]) - 97] = i

    # 否则无法通过一次交换减少差异
    print(k)
    print(-1, -1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)