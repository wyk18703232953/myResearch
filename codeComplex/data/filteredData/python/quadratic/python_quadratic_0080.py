from heapq import heappush, heappop

MSIZE = 1 << 8

def GetVal(s):
    ans = 0
    for i in range(8):
        if s[i] == '1':
            ans = ans + (1 << i)
    return ans

def GetNot(s):
    return MSIZE - 1 - s

xVal = GetVal('00001111')
yVal = GetVal('00110011')
zVal = GetVal('01010101')

# 0 - |
# 1 - &
# 2 - !
# 3 - ()

def Dijkstra():
    depth = [['Z' * 585 for _ in range(4)] for _ in range(MSIZE)]
    depth[xVal][3] = 'x'
    depth[yVal][3] = 'y'
    depth[zVal][3] = 'z'

    pq = []
    def push(kek):
        heappush(pq, kek)
    def pop():
        return heappop(pq)

    push([1, xVal, 3])
    push([1, yVal, 3])
    push([1, zVal, 3])

    while len(pq) > 0:
        l, i, j = pop()
        if len(depth[i][j]) < l:
            continue

        for x in range(MSIZE):
            for y in range(4):
                nxt1 = depth[i][j] + '|' + depth[x][y]
                nxt2 = depth[x][y] + '|' + depth[i][j]
                nxt = min(nxt1, nxt2)
                val = (i | x)
                if len(depth[val][0]) == len(nxt) and depth[val][0] > nxt:
                    depth[val][0] = nxt
                    push([len(nxt), val, 0])
                elif len(depth[val][0]) > len(nxt):
                    depth[val][0] = nxt
                    push([len(nxt), val, 0])

        if j > 0:
            for x in range(MSIZE):
                for y in range(1, 4):
                    nxt1 = depth[i][j] + '&' + depth[x][y]
                    nxt2 = depth[x][y] + '&' + depth[i][j]
                    nxt = min(nxt1, nxt2)
                    val = (i & x)
                    if len(depth[val][1]) == len(nxt) and depth[val][1] > nxt:
                        depth[val][1] = nxt
                        push([len(nxt), val, 1])
                    elif len(depth[val][1]) > len(nxt):
                        depth[val][1] = nxt
                        push([len(nxt), val, 1])

        if j > 2:
            val = GetNot(i)
            nxt = '!' + depth[i][j]
            if len(depth[val][2]) == len(nxt) and depth[val][2] > nxt:
                depth[val][2] = nxt
                push([len(nxt), val, 2])
            elif len(depth[val][2]) > len(nxt):
                depth[val][2] = nxt
                push([len(nxt), val, 2])

        nxt = '(' + depth[i][j] + ')'
        val = i
        if len(depth[val][3]) == len(nxt) and depth[val][3] > nxt:
            depth[val][3] = nxt
            push([len(nxt), val, 3])
        elif len(depth[val][3]) > len(nxt):
            depth[val][3] = nxt
            push([len(nxt), val, 3])

    answer = []
    for i in range(MSIZE):
        ans = 'Z' * 585
        for j in range(4):
            if len(ans) > len(depth[i][j]):
                ans = depth[i][j]
            elif len(ans) == len(depth[i][j]) and ans > depth[i][j]:
                ans = depth[i][j]
        answer.append(ans)
    return answer

def main(n):
    # 预先跑一次 Dijkstra，保持核心算法不变
    kek = Dijkstra()

    # 将 n 解释为查询数量 q，生成 q 个确定性的 8 位二进制字符串
    # 第 i 个查询对应整数 i % 256 的 8 位二进制形式
    q = n
    results = []
    for i in range(q):
        v = i % 256
        bits = ''.join('1' if (v >> j) & 1 else '0' for j in range(8))
        results.append(kek[GetVal(bits)])

    # 为了实验时有可观测输出，这里打印所有结果行
    for s in results:
        print(s)

if __name__ == "__main__":
    # 示例：输入规模 n = 5
    main(5)