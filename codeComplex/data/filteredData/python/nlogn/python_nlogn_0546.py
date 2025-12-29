import random

def main(n):
    # 1. 生成测试数据：长度为 n 的整数数组 l
    #    这里生成 1~n 的随机排列，如果需要其他分布可以自行修改
    l = list(range(1, n + 1))
    random.shuffle(l)

    index = []
    ans = []
    for i in range(n):
        index.append(i + 1)
        ans.append(0)

    l1, index1 = zip(*sorted(zip(l, index), reverse=True))

    for i in range(n):
        k = 1
        flag = False
        # 向左搜索
        while (index1[i] - k * l1[i]) > 0:
            if l[index1[i] - k * l1[i] - 1] > l[index1[i] - 1]:
                if ans[index1[i] - k * l1[i] - 1] == "B":
                    ans[index1[i] - 1] = "A"
                    flag = True
                    break
            k += 1

        k = 1
        if flag is False:
            # 向右搜索
            while (index1[i] + k * l1[i]) <= n:
                if l[index1[i] + k * l1[i] - 1] > l[index1[i] - 1]:
                    if ans[index1[i] + k * l1[i] - 1] == "B":
                        ans[index1[i] - 1] = "A"
                        flag = True
                        break
                k += 1

        if flag is False:
            ans[index1[i] - 1] = "B"

    print(''.join(ans))


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(10)