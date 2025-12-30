from random import randint

def main(n):
    # 生成测试数据：长度为 2*n 的数组，每个数字出现两次
    # 先构造配对数组，然后打乱顺序以形成随机测试
    values = [i for i in range(1, n + 1) for _ in range(2)]
    for i in range(2 * n - 1, 0, -1):
        j = randint(0, i)
        values[i], values[j] = values[j], values[i]

    a = values[:]  # 工作数组
    ans = 0
    for i in range(0, 2 * n, 2):
        if a[i] != a[i + 1]:
            for j in range(i + 1, 2 * n):
                if a[j] == a[i]:
                    # 通过相邻交换将 a[j] 移动到位置 i+1
                    for k in range(j, i + 1, -1):
                        a[k], a[k - 1] = a[k - 1], a[k]
                        ans += 1
                    break
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：调用 main(5) 进行简单测试
    main(5)