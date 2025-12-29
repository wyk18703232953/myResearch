import random

def main(n: int):
    # 1. 生成测试数据：n 个非负整数石子堆
    # 这里生成范围 [0, 10^9] 内的随机数，可按需要调整
    stones = [random.randint(0, 10**9) for _ in range(n)]
    stones.sort()

    # 2. 原逻辑
    if n == 1:
        if stones[0] % 2 == 0:
            print('cslnb')
        else:
            print('sjfnb')
        return

    chilly = -1
    chill = 2
    prev = stones[0]

    for x in stones[1:]:
        if x == prev:
            chill -= 1
            chilly = x
        else:
            prev = x

    s = sum(stones)

    if n % 4 == 0 or n % 4 == 1:
        s += 1

    if chill <= 0 or stones.count(0) > 1:
        print('cslnb')
    elif chill == 1 and chilly - 1 in stones:
        print('cslnb')
    elif s % 2 == 1:
        print('cslnb')
    else:
        print('sjfnb')


# 示例：手动调用 main
if __name__ == "__main__":
    main(5)