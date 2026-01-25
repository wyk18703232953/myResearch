def judge(x):
    if x % 2 == 0:
        return 0
    else:
        return 1

def main(n):
    # 构造一个长度为 n 的整数列表 ls
    # 设计为：前面若干个数同奇偶性，只有一个“异类”，保证算法能工作
    if n < 3:
        n = 3

    ls = [i for i in range(1, n + 1)]

    # 保证前两个元素奇偶相同，第三个不同（方便触发分支）
    # 当 n>=3 时我们强行设置前三个值的奇偶模式
    ls[0] = 2  # 偶
    ls[1] = 4  # 偶
    ls[2] = 3  # 奇

    # 其余元素按确定性规则设置，可以让它们中再出现若干“异类”或保持一致
    # 这里保持从第4个开始与第一个元素同奇偶，以使第3个成为唯一区别点
    for i in range(3, n):
        ls[i] = 2 * (i + 1)

    # 原程序的核心逻辑
    if judge(ls[0]) == judge(ls[1]):
        for x in ls[2:]:
            if judge(x) != judge(ls[0]):
                print(ls.index(x) + 1)
                break
    else:
        if judge(ls[2]) == judge(ls[0]):
            print(2)
        elif judge(ls[2]) == judge(ls[1]):
            print(1)

if __name__ == "__main__":
    main(10)