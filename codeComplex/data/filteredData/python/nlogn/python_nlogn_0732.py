import random

def iskoutsu(arr):
    return len(set(arr)) == 1

def isshuntsu(arr):
    nos = [int(ele[0]) for ele in arr]
    nos.sort()
    return (
        nos[0] + 1 == nos[1]
        and nos[1] + 1 == nos[2]
        and len(set([ele[1] for ele in arr])) == 1
    )

def generate_test_data(n):
    # 牌面 1-9，花色用 a,b,c 三种示例
    suits = ['a', 'b', 'c']
    tiles = [str(num) + suit for num in range(1, 10) for suit in suits]
    # 原逻辑是3张牌，若 n != 3，仍随机取3张，只是规模参数 n 仅控制随机种子或生成次数等
    random.seed(n)
    return random.sample(tiles, 3)

def main(n):
    arr = generate_test_data(n)

    if isshuntsu(arr) or iskoutsu(arr):
        print(0)
        return

    # to make koutsu
    total1 = 0
    if len(set(arr)) == 3:
        total1 = 2
    elif len(set(arr)) == 2:
        total1 = 1

    # to make shuntsu
    total2 = 2
    for ele in arr:
        no, suite = int(ele[0]), ele[1]

        if no + 2 <= 9:
            required = [str(no + 1) + suite, str(no + 2) + suite]
            curr = int(required[0] not in arr) + int(required[1] not in arr)
            total2 = min(total2, curr)

        if no + 1 <= 9 and no - 1 >= 0:
            required = [str(no - 1) + suite, str(no + 1) + suite]
            curr = int(required[0] not in arr) + int(required[1] not in arr)
            total2 = min(total2, curr)

        if no + 2 <= 9:
            required = [str(no - 1) + suite, str(no - 2) + suite]
            curr = int(required[0] not in arr) + int(required[1] not in arr)
            total2 = min(total2, curr)

    print(min(total1, total2))


if __name__ == "__main__":
    # 示例：调用 main，规模参数 n 可任意指定
    main(1)