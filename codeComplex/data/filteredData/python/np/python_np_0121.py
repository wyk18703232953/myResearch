def main(n):
    buck = [[0, 0] for _ in range(2201)]
    m = n
    # 生成确定性的输入序列：第 i 个元素为 i + 1
    inputs = [i + 1 for i in range(m)]

    outputs = []
    for i in range(m):
        a = inputs[i]
        ok = True
        br = 0
        for j in range(2200, -1, -1):
            if a & (1 << j):
                if buck[j][0]:
                    a ^= buck[j][0]
                    br ^= buck[j][1]
                else:
                    ok = False
                    buck[j][0] = a
                    buck[j][1] = br | (1 << i)
                    break
        if not ok:
            outputs.append("0")
        else:
            lst = []
            for j in range(2201):
                if br & (1 << j):
                    lst.append(j)
            line = [str(len(lst))] + [str(x) for x in lst]
            outputs.append(" ".join(line))
    # 返回所有行，便于外部实验时统计耗时而不必真正打印
    return outputs


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小做实验
    res = main(10)
    for line in res:
        print(line)