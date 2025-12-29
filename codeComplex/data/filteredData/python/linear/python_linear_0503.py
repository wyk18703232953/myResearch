import random

def main(n):
    # 生成测试数据：A 是 1..n 的随机排列
    A = list(range(1, n + 1))
    random.shuffle(A)

    PLACE = [None] * (n + 1)
    for i in range(n):
        PLACE[A[i]] = i

    al = n
    WINLIST = [None] * (n + 1)  # 0:必败("B"),1:必胜("A")

    def move(x, al):
        place = PLACE[x]
        # 向左跳
        for i in range(place, -1, -x):
            if A[i] > x and WINLIST[A[i]] == "B":
                WINLIST[x] = "A"
                return
        # 向右跳
        for i in range(place, al, x):
            if A[i] > x and WINLIST[A[i]] == "B":
                WINLIST[x] = "A"
                return
        WINLIST[x] = "B"

    for j in range(n, 0, -1):
        move(j, al)

    ANS = "".join(WINLIST[i] for i in A)
    print(ANS)


if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)