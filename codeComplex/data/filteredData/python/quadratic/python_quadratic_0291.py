import random

def main(n: int) -> int:
    # 生成测试数据：长度为 2*n 的数组，每个数出现两次并打乱顺序
    ar = []
    for x in range(1, n + 1):
        ar.extend([x, x])
    random.shuffle(ar)

    ans = 0
    # 原逻辑：在长度为 2*n 的数组上操作
    for i in range(2 * n):
        for j in range(i + 1, 2 * n):
            if ar[i] == ar[j]:
                while j != i + 1:
                    ar[j], ar[j - 1] = ar[j - 1], ar[j]
                    j -= 1
                    ans += 1
                break
    return ans

if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    print(main(5))