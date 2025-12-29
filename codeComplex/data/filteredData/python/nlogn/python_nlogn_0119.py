import random

def main(n):
    # 3. 根据 n 生成测试数据：生成一个长度为 n 的随机整数数组
    # 数值范围可按需调整，这里设为 1~n
    arr = [random.randint(1, n) for _ in range(n)]

    # 原逻辑开始
    if arr == [1, 2, 3, 4, 5, 3]:
        print("NO")
    else:
        orig = sorted(arr)
        ans = 0
        for i in range(n):
            if arr[i] != orig[i]:
                ans += 1
        ans = ans / 2
        if ans <= 1:
            print("YES")
        else:
            print("NO")


# 示例：直接运行本文件时执行 main(6)
if __name__ == "__main__":
    main(6)