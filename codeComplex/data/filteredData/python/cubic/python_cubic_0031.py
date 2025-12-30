import random
import string

def main(n: int):
    # 生成长度为 n 的随机小写字符串
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    
    k = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 2):
            x = s[i:j]
            for t in range(i + 1, len(s)):
                if x == s[t:t + j - i]:
                    k.append(j - i)
    print(max(k) if k else 0)

if __name__ == "__main__":
    # 示例：n 可以根据需要修改
    main(10)