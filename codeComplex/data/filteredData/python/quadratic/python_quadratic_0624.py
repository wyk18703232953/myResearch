import random

def main(n: int) -> int:
    # 生成测试数据：n 个正整数，范围可根据需要调整
    a = sorted(random.randint(1, 10 ** 6) for _ in range(n))

    ans = 0
    for i in range(n):
        f = 1
        for j in range(i):
            if a[i] % a[j] == 0:
                f = 0
                break
        ans += f
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例调用，可根据需要修改规模
    main(10)