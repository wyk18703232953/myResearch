def find(A):
    from collections import defaultdict
    A = sorted(A)
    N = len(A)
    dic = defaultdict(int)
    for i in range(N):
        dic[A[i]] += 1

    count = set()
    for x in A:
        if dic[x] > 2:
            return "cslnb"
        if dic[x] == 2:
            count.add(x)
            y = x - 1
            if y in dic:
                return "cslnb"
    if len(count) > 1:
        return "cslnb"

    if 0 in count:
        return "cslnb"

    temp = 0
    for i in range(N):
        temp += A[i] - i
    if temp % 2 == 1:
        return "sjfnb"
    return "cslnb"


def main(n):
    # 输入规模含义：数组 A 的长度为 n
    # 确定性生成测试数据 A
    # 示例构造：A[i] = i // 2 形成一定重复但受控的多重集
    A = [i // 2 for i in range(n)]
    result = find(A)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，时间复杂度实验时可修改 n
    main(10)