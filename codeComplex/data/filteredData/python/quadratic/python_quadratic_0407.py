import random
import string

def prefix_func(s):
    slen, k = len(s), 0
    p = [0] * slen
    p[0] = 0
    for i in range(1, slen):
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p

def main(n):
    # 生成测试数据：
    # n 表示字符串长度，k 设为一个与 n 有关的重复次数
    k = max(1, n // 3)  # 保证 k >= 1
    # 生成一个随机字符串，字母大小写或数字均可
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    l = prefix_func(s)[-1]
    result = s + s[l:] * (k - 1)
    print(result)
    return result

if __name__ == "__main__":
    # 示例：规模 n = 10，可根据需要修改或在外部调用 main(n)
    main(10)