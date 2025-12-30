import random

def main(n):
    # 1. 生成规模为 n 的测试数据：n 个非负整数
    #   可根据需要修改生成范围
    arr = [random.randint(0, 10**6) for _ in range(n)]

    arr.sort(reverse=True)

    d = {}
    for i in range(n):
        if arr[i] in d:
            d[arr[i]].append(i)
        else:
            d[arr[i]] = [i]

    cnt = 0
    vis = [-1] * n
    for i in range(n):
        s = bin(arr[i])[2:][::-1]
        l = len(s)
        x = 0
        for j in range(l):
            if s[j] == "0":
                x += (2 ** j)
        x += 1

        if x in d:
            if x == arr[i] and len(d[x]) == 1:
                if vis[i] == -1:
                    cnt += 1
            else:
                if vis[d[x][0]] == -1:
                    for j in d[x]:
                        vis[j] = 1
        else:
            if vis[i] == -1:
                cnt += 1
        vis[i] = 1

    print(cnt)


if __name__ == "__main__":
    # 示例：调用 main，规模自定
    main(10)