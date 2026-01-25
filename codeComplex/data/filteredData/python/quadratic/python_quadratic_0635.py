class APaintTheNumbers:
    def solve(self, n, a):
        a.sort()
        ans = 0
        done = [0] * n
        for i in range(n):
            if done[i]:
                continue
            ans += 1
            for j in range(i, n):
                if done[j]:
                    continue
                if a[j] % a[i] == 0:
                    done[j] = 1
        return ans

def main(n):
    # 生成确定性测试数据：
    # 对于给定的 n，生成 n 个正整数，构造方式为 i*2+1，保证全为奇数且递增
    a = [2 * i + 1 for i in range(n)]
    solver = APaintTheNumbers()
    result = solver.solve(n, a)
    print(result)

if __name__ == "__main__":
    # 示例调用，使用一个固定的 n 值
    main(10)