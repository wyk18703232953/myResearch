import random

def main(n):
    # 生成测试数据：n为规模，这里随机生成 k，范围可根据需要调整
    # 保证 k 不为负且不过大
    k = random.randint(0, max(1, n * (n + 1) // 4))

    # 以下为原逻辑的无 input() 改写
    i = 1
    count = 0
    cursum = 0
    while count < n:
        if cursum < k:
            cursum += i
        else:
            break
        count += 1
        i += 1

    count += cursum - k

    if n == count:
        print(cursum - k)
    else:
        ans = cursum - k
        extra = 0
        while count < n:
            extra += i
            count += (i + 1)
            i += 1
        print(ans + extra)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自定义
    main(10)