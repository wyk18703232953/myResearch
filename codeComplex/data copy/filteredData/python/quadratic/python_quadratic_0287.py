def main(n):
    # n 作为列表长度，生成一个确定性的整数列表
    # 构造思路：长度为 n，元素为 i % 5，制造适量重复以触发算法逻辑
    l = [i % 5 for i in range(n)]
    i = 0
    ans = 0
    while i < len(l) - 1:
        if l[i] == l[i + 1]:
            i = i + 1
            continue

        j = i + 1
        ind = -1
        while j < len(l):
            if l[j] == l[i]:
                ind = j
                break
            j = j + 1

        while ind > i + 1:
            l[ind], l[ind - 1] = l[ind - 1], l[ind]
            ans += 1
            ind -= 1

        i += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)