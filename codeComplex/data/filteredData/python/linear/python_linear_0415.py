import random
import string

def main(n):
    # 1. 生成测试数据
    # 从 1~min(26,n) 之间选一个 k，保证有意义
    k = random.randint(1, min(26, max(1, n)))
    # 生成长度为 n 的小写字母串
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 2. 原逻辑
    a = [0] * 26
    for ch in s:
        a[ord(ch) - ord('a')] = 1

    ans = 0
    i = 0
    kk = k  # 保留原始 k 以便调试时查看
    while i < 26:
        if a[i] > 0:
            ans += i + 1
            k -= 1
            i += 1
            if k == 0:
                print(ans)
                break
        i += 1
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：规模设为 100
    main(100)