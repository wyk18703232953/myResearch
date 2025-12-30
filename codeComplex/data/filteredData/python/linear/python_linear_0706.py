import random

def main(n: int):
    # 根据规模 n 生成长度为 n 的只含 '+' 和 '-' 的随机字符串
    s = ''.join(random.choice(['+', '-']) for _ in range(n))

    ans = 0
    for ch in s:
        if ch == '+':
            ans += 1
        else:
            ans -= 1
        if ans < 0:
            ans = 0
    print(ans)


if __name__ == "__main__":
    # 示例：可修改下面的 n 来测试不同规模
    main(10)