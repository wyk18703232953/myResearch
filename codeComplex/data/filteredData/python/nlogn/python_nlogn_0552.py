import random

def main(n: int):
    # 生成测试数据：board[1..n]，每个位置放置 1..n 范围内的正整数
    # 为保证可走动，避免生成 0
    board = [0] + [random.randint(1, n) for _ in range(n)]

    hashed = [0] * (n + 1)
    for i in range(n + 1):
        hashed[board[i]] = i

    answer = ['C'] * (n + 1)
    for i in range(n, 0, -1):
        flag = 0
        pos = hashed[i]
        step = board[pos]

        k = pos - step
        while k > 0:
            if answer[k] == 'B':
                flag = 1
                break
            k -= step

        if flag == 0:
            k = pos + step
            while k <= n and k != 0:
                if answer[k] == 'B':
                    flag = 1
                    break
                k += step

        if flag == 1:
            answer[pos] = 'A'
        else:
            answer[pos] = 'B'

    answer.pop(0)
    print(''.join(answer))


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)