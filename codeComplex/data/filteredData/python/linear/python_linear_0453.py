import random

def main(n):
    # 生成测试数据：
    # 1. 随机生成一个由 '(' 和 ')' 组成的长度为 n 的字符串
    # 2. 令 k 为不大于 n 的最大偶数（与原题“取出长度为 k 的合法括号子序列”场景一致）
    arr = [random.choice(['(', ')']) for _ in range(n)]
    k = n if n % 2 == 0 else n - 1

    st = []
    ans = []
    for i in range(n):
        if k <= 0:
            break
        if arr[i] == '(':
            st.append((arr[i], i))
        else:
            if st and st[-1][0] == '(':
                k -= 2
                ans.append(st.pop())
                ans.append((arr[i], i))
            else:
                st.append((arr[i], i))

    ans.sort(key=lambda x: x[1])
    res = [ch for ch, _ in ans]
    print(''.join(res))


if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(10)