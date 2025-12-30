from random import randint

def main(n: int):
    # 生成长度为 n 的测试数据，这里用 1~10 的随机整数
    arr = [randint(1, 10) for _ in range(n)]

    okk = 0
    s = 0
    for i in range(n - 1):
        s += arr[i]
        cnt = 0
        ok = 1
        sss = 0
        for j in range(i + 1, n):
            cnt += arr[j]
            if cnt == s:
                cnt = 0
                sss += 1
            if cnt > s:
                ok = 0
        if cnt == 0 and sss:
            okk = 1
            break

    print("YES" if okk else "NO")


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n
    main(10)