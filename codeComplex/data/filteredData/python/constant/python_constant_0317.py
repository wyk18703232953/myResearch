import random

def even_sum(arr):
    temp_sum = 0
    for each in arr:
        if each % 2 == 0:
            temp_sum += each
    return temp_sum

def main(n):
    # 生成长度为 14 的 stones 数组，数值规模由 n 控制
    # 这里设定每个元素在 [0, n] 区间内随机生成
    stones = [random.randint(0, n) for _ in range(14)]

    initial_sum = even_sum(stones)

    for i in range(14):
        duplicate = list(stones)
        temp = stones[i]
        duplicate[i] = 0
        j = i

        for each in range(14):
            duplicate[each] += temp // 14

        temp = temp % 14
        while temp > 0:
            if j == 13:
                j = -1
            j += 1
            duplicate[j] += 1
            temp -= 1

        ts = even_sum(duplicate)
        if ts > initial_sum:
            initial_sum = ts

    print(initial_sum)

if __name__ == "__main__":
    # 示例：规模 n = 100
    main(100)