from collections import Counter

def main(n):
    # n 表示字符串长度，同时设定 k 的规模
    # 这里令 k 在 [1, 26] 内，与 n 形成确定性关系
    k = max(1, min(26, n % 26 + 1))

    # 构造一个确定性的只含大写字母的字符串 s，长度为 n
    # 使用简单算术生成 A-Z 循环序列
    s = ''.join(chr(ord('A') + (i % 26)) for i in range(n))

    c = Counter(s)
    ans = min(c[chr(ord('A') + i)] for i in range(k))
    result = k * ans
    print(result)
    return result

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小
    main(1000)