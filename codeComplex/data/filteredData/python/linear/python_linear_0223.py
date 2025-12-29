import random

def main(n: int) -> None:
    # 生成长度为 n 的随机 0/1 字符串作为测试数据 m
    m = ''.join(random.choice('01') for _ in range(n))
    s = list(m)

    if n == 1:
        ans = s[0]
    else:
        count = 0
        for i in range(n):
            if s[i] == '0':
                count += 1
        ans = '1'
        for _ in range(count):
            ans += '0'

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)