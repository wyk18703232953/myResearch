import random
import string

def main(n: int):
    # 生成长度为 n 的测试字符串 s
    # 为确保存在重复子串，至少使用较小的字符集
    if n <= 1:
        s = "a" * n
    else:
        chars = string.ascii_lowercase[:5]  # 使用前 5 个小写字母
        s = ''.join(random.choice(chars) for _ in range(n))

    length = len(s)
    answer = []

    for i in range(length):
        for j in range(i + 1, length + 1):
            k = s[i:j]
            co = 0
            for u in range(length):
                if s[u:].startswith(k):
                    co += 1
            if co >= 2:
                answer.append(len(k))

    if len(set(s)) == length:
        print('0')
    else:
        print(max(answer))


if __name__ == "__main__":
    # 示例：规模 n 可在此修改或由外部调用 main(n)
    main(10)