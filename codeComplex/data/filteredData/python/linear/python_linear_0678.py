import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里生成范围在 -10^9 到 10^9 的随机整数
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    
    st = [a[0]]
    for i in range(1, n):
        if len(st) > 0 and st[-1] % 2 == a[i] % 2:
            st.pop()
        else:
            st.append(a[i])
    if len(st) <= 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：将 n 设置为 10，可根据需要修改
    main(10)