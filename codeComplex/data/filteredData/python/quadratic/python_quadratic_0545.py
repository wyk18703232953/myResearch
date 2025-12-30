import random

def main(n: int) -> int:
    # 生成测试数据：v 为 1~n 之间的随机整数
    v = random.randint(1, n)

    b = 0
    ans = 0
    sss = 0
    for i in range(1, n + 1):
        while b < v:
            if sss == n - 1:
                break
            sss += 1
            ans += i
            b += 1
        b -= 1
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的大小
    main(10)