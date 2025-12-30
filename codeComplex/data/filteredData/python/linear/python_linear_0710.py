import random

def main(n: int):
    # 根据 n 生成长度为 n 的字符串 s，字符为 '-' 或 '+'
    # 这里假设规模 n 即为字符串长度
    s = ''.join(random.choice('+-') for _ in range(n))

    t = 0
    mn = 0
    for ch in s:
        if ch == '-':
            t -= 1
        else:
            t += 1
        mn = min(mn, t)
    print(-mn + t)

if __name__ == "__main__":
    # 示例：可修改为任意规模
    main(10)