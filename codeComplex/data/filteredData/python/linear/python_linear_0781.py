from collections import defaultdict as dd

def main(n):
    # 生成确定性输入数组 A，长度为 n
    # 这里构造一个简单的递增序列，带一点确定性变化
    A = [(i // 2) for i in range(n)]
    # 保持原逻辑中重新计算 n 的行为
    n = len(A)

    C = dd(int)
    for a in A:
        C[a] += 1

    thedup = None
    ndup = 0
    screwed = False
    for c in C:
        if C[c] > 2:
            screwed = True
        elif C[c] == 2:
            if c == 0:
                screwed = True
            thedup = c
            ndup += 1

    if screwed or ndup > 1:
        print('cslnb')
    else:
        if ndup == 1:
            if C[thedup - 1] != 0:
                print('cslnb')
                return

        target = sum(range(n))
        cur = sum(A)
        togo = cur - target

        if togo % 2 == 0:
            print('cslnb')
        else:
            print('sjfnb')


if __name__ == "__main__":
    main(10)