import bisect

def core_logic(k):
    xzy = [10, 190, 2890, 38890, 488890, 5888890, 68888890, 788888890, 8888888890, 98888888890, 1088888888890, 11888888888890]
    digits = bisect.bisect_left(xzy, k)
    if k == 10:
        return 1
    elif k > 10:
        apu = k - xzy[digits - 1]
        modulo = apu % (digits + 1)
        dlj = apu // (digits + 1)
        output = 10 ** (digits) + dlj
        list1 = [i for i in str(output)]
        return list1[modulo]

    else:
        return k

def main(n):
    # 将 n 视为要测试的 k 的最大规模，依次从 1 到 n 调用核心逻辑
    results = []
    for k in range(1, n + 1):
        results.append(str(core_logic(k)))
    # 输出所有结果，以便在时间复杂度实验中有确定的输出行为
    # print("\n".join(results))
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 以进行规模化实验
    main(1000)