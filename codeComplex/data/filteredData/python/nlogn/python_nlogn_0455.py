import random

def main(n):
    # 生成测试数据
    # 长度为 n 的数组，元素范围可自行调整
    length = n
    numList = [random.randint(1, 10) for _ in range(length)]
    # 在数组中随机选择一个位置作为 targetnumber 的位置
    pos = random.randint(0, length - 1)
    targetnumber = numList[pos]

    # 原逻辑开始
    pos_r = pos + 1
    rem = 0
    right = {0: 1}
    left = {0: 1}

    # 向右累积
    while pos_r <= length - 1:
        if numList[pos_r] > targetnumber:
            rem += 1
        else:
            rem -= 1
        if rem not in right:
            right[rem] = 1
        else:
            right[rem] += 1
        pos_r += 1

    # 向左累积
    pos_l = pos - 1
    rem = 0
    while pos_l >= 0:
        if numList[pos_l] > targetnumber:
            rem += 1
        else:
            rem -= 1
        if rem not in left:
            left[rem] = 1
        else:
            left[rem] += 1
        pos_l -= 1

    ans = 0
    for number_l in left:
        if -number_l in right:
            ans += left[number_l] * right[-number_l]
        if 1 - number_l in right:
            ans += left[number_l] * right[1 - number_l]

    print("numList:", numList)
    print("targetnumber:", targetnumber)
    print("answer:", ans)


if __name__ == "__main__":
    main(10)