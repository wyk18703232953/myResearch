import random

def main(n):
    # 生成规模为 n 的测试数据（这里生成 1~100 之间的随机整数）
    a = [random.randint(1, 100) for _ in range(n)]

    a.sort()
    ans = 0
    ok = False

    for i in range(len(a)):
        if a[i] > min(a):
            ans = a[i]
            ok = True
            break

    if ok:
        print(ans)
    else:
        print("NO")


# 示例调用
if __name__ == "__main__":
    main(10)