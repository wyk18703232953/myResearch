def main(n):
    # 将 n 映射为问题规模：这里使用
    #   n -> (N, pos, l, r)
    # 其中 N 为总长度，pos 为当前位置，l、r 为左右边界
    # 为了保证可扩展性和确定性，使用简单算术构造
    N = max(2, n)
    pos = (n % N) + 1          # 保证在 [1, N]
    l = max(1, (n // 3) % N + 1)
    r = max(l, (2 * n // 3) % N + 1)
    if r > N:
        r = N
    if l > r:
        l, r = r, l

    time = 0
    if l != 1 and r != N:
        if abs(pos - l) < abs(pos - r):
            time += abs(pos - l) + abs(l - r) + 2

        else:
            time += abs(pos - r) + abs(l - r) + 2
    elif l == 1 and r != N:
        time += abs(pos - r) + 1
    elif r == N and l != 1:
        time += abs(pos - l) + 1

    else:
        time += 0
    # print(time)
    pass
if __name__ == "__main__":
    main(10)