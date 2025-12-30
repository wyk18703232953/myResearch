import random
import string

def palindrome(s):
    i = 0
    j = len(s) - 1
    p = True
    while i <= j:
        if s[i] != s[j]:
            p = False
            break
        i += 1
        j -= 1
    return p

def main(n):
    # 生成长度为 n 的随机字符串，字符集为小写字母
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    ans = 0
    for i in range(len(s)):
        for j in range(len(s) - 1, i, -1):
            if not palindrome(s[i:j + 1]):
                ans = max(ans, len(s[i:j + 1]))
                break

    print(ans)

if __name__ == "__main__":
    # 示例：可在此处修改 n 的值进行测试
    main(10)