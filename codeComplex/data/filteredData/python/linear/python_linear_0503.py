import sys

# 原程序中的全局变量
PLACE = []
WINLIST = []
A = []


def move(n, al):
    place = PLACE[n]
    for i in range(place, -1, -n):
        if A[i] > n and WINLIST[A[i]] == "B":
            WINLIST[n] = "A"
            return

    for i in range(place, al, n):
        if A[i] > n and WINLIST[A[i]] == "B":
            WINLIST[n] = "A"
            return

    WINLIST[n] = "B"
    return


def main(n):
    # n 作为输入规模：原代码中就是数组长度
    # 构造一个 1..n 的排列，保持确定性
    # 这里使用简单的“旋转”构造：A[i] = (i+1)%n + 1
    global PLACE, WINLIST, A

    if n <= 0:
        return ""

    A = [((i + 1) % n) + 1 for i in range(n)]

    PLACE = [None] * (n + 1)
    for i in range(n):
        PLACE[A[i]] = i

    al = n
    WINLIST = [None] * (n + 1)

    for j in range(n, 0, -1):
        move(j, al)

    ans = ""
    for x in A:
        ans += WINLIST[x]

    # 为了便于实验，返回结果而不是直接打印
    return ans


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的规模做实验
    n = 10
    result = main(n)
    print(result)