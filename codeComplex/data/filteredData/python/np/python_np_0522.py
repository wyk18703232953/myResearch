def main(n):
    from collections import deque

    # 映射 n 为原程序中的 n 和 k，并构造字符串 s
    # 这里设定：k 固定为 3，字符串长度为 n
    # 字符构造规则是完全确定性的：
    # s[i] = '?' if i % 5 == 0 else chr(ord('a') + (i % 3))
    k = 3
    if n < k:
        # 保证规模有意义
        n_local = k
    else:
        n_local = n
    s = bytearray()
    for i in range(n_local):
        if i % 5 == 0:
            s.append(ord('?'))
        else:
            s.append(ord('a') + (i % k))

    inf = 2147483647

    def judge(needed):
        minstate = [inf] * (1 << k)
        minstate[0] = 0
        effect = [[inf] * (n_local + 1) for _ in range(k)]

        for j in range(k):
            accu = 0
            index = inf
            for i in range(n_local - 1, -1, -1):
                if s[i] == ord('?') or s[i] == 97 + j:
                    accu += 1
                else:
                    accu = 0
                if accu >= needed:
                    index = i + needed
                effect[j][i] = index
                if effect[j][i] > inf:
                    effect[j][i] = inf

        for state in range(1, 1 << k):
            minimum = minstate[state]
            for j in range(k):
                if (1 << j) & state == 0:
                    continue
                index = minstate[state ^ (1 << j)]
                if index < n_local:
                    if effect[j][index] < minimum:
                        minimum = effect[j][index]
            minstate[state] = minimum

        return minstate[-1] <= n_local

    front = 0
    rear = n_local // k + 1
    while front < rear:
        mid = (front + rear) // 2
        flag = judge(mid)
        if flag:
            front = mid + 1
        else:
            rear = mid

    result = front - 1
    print(result)
    return result


if __name__ == "__main__":
    # 示例调用：可以修改这里的 n 进行规模实验
    main(1000)