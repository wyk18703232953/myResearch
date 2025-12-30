import random

def main(n):
    # 生成一个长度为 n 的随机糖果数组，每个元素在 [0, n] 范围内
    candies = [random.randint(0, n) for _ in range(n)]

    # 根据 candies 生成 l 和 r
    l = []
    r = []
    for i in range(n):
        left_greater = 0
        right_greater = 0
        for j in range(n):
            if j < i and candies[j] > candies[i]:
                left_greater += 1
            if j >= i and candies[j] > candies[i]:
                right_greater += 1
        l.append(left_greater)
        r.append(right_greater)

    # 按原逻辑从 l 和 r 还原 candies
    reconstructed = []
    for i in range(n):
        reconstructed.append(n - l[i] - r[i])

    left = []
    for i in range(n):
        guys = 0
        for j in range(i):
            if reconstructed[j] > reconstructed[i]:
                guys += 1
        left.append(guys)

    right = []
    for i in range(n):
        guys = 0
        for j in range(i, n):
            if reconstructed[j] > reconstructed[i]:
                guys += 1
        right.append(guys)

    if left == l and right == r:
        print("YES")
        candies_str = " ".join(str(x) for x in reconstructed)
        print(candies_str)
    else:
        print("NO")

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)