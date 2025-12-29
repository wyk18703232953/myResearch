import random
import string

def main(n: int):
    # 生成长度为 n 的随机01串
    a = [random.choice('01') for _ in range(n)]
    b = [random.choice('01') for _ in range(n)]

    ans = 0
    i = 0
    while i < n:
        if a[i] != b[i]:
            ans += 1
            if i < n - 1 and a[i] == b[i + 1] and b[i] == a[i + 1]:
                i += 1
        i += 1

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)