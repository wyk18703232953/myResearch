import random

def main(n):
    # 生成长度为 n 的随机字符串，由 'H' 和 'T' 组成
    s = ''.join(random.choice('HT') for _ in range(n))

    h = s.count('H')
    s2 = s + s
    # 当没有 'H' 时，窗口长度为 0，代价为 0
    if h == 0:
        print(0)
        return

    ans = min(s2[i:i + h].count('T') for i in range(n))
    print(ans)


if __name__ == "__main__":
    # 示例：可自行修改 n 进行测试
    main(10)