from itertools import combinations
import random

def main(n):
    # 根据 n 生成测试数据
    # 这里生成：
    #   - 题目数组 arr: n 个 [1, 100] 之间的整数
    #   - l, r: 和的下界与上界（根据 arr 和略微放宽范围）
    #   - x: 题目中“难度差”的最小值
    random.seed(0)  # 如需不同数据可去掉或修改种子
    arr = [random.randint(1, 100) for _ in range(n)]
    arr.sort()

    total_sum = sum(arr)
    # 保证 l <= r，范围覆盖适度
    l = total_sum // 4
    r = total_sum // 2
    if l > r:
        l, r = r, l
    # x 为最小差值，取数组范围的一部分
    x = max(1, (arr[-1] - arr[0]) // 3)

    def check(temp):
        if len(temp) < 2:
            return False
        s = sum(temp)
        if l <= s <= r and temp[-1] - temp[0] >= x:
            return True
        return False

    def brute(index, temp):
        nonlocal count
        if index == n:
            if check(temp):
                count += 1
        else:
            temp.append(arr[index])
            brute(index + 1, temp)
            temp.pop()
            brute(index + 1, temp)

    count = 0
    brute(0, [])
    print(count)


# 示例：调用 main(5)
if __name__ == "__main__":
    main(5)