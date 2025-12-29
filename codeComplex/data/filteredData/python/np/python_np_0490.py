from collections import defaultdict

# 全局变量（沿用原程序结构）
s = ""
k = 0
outs = set()

def gen(temp, i):
    """递归生成所有符合规则的模式集合 outs。"""
    global s, k, outs
    if i == k:
        j = ''
        for o in range(k):
            if temp[o] == 1:
                j += s[o]
            else:
                j += '_'
        outs.add(j)
        return
    temp[i] = 1
    gen(temp, i + 1)
    temp[i] = -1
    gen(temp, i + 1)


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour]:
                return True
        recStack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True
        return False

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        stack.append(v)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        stack = stack[::-1]
        # 保持原输出格式
        print("yes")
        print(" ".join(str(i + 1) for i in stack))


def generate_test_data(n):
    """
    根据规模 n 生成测试数据：
    - k 固定为 3。
    - 生成 n 条模式，每条模式为长度 k 的字符串，由小写字母和 '_' 组成。
    - 构造一个有向无环图的依赖关系，用 m 条边描述。
    返回：
        n, m, k, all_patterns(list[str]), queries(list[tuple[str,int]])
    """
    # 为了确定性与简洁性，构造固定模式：
    # 第 i 个模式：用 'a'+(i%26) 填充非 '_' 的位置，位置模式固定。
    k = 3
    all_patterns = []
    for i in range(n):
        ch = chr(ord('a') + (i % 26))
        # 简单构造：第一位为字符，后两位为 '_'
        pattern = ch + "__"
        all_patterns.append(pattern)

    # 为构造 m 和查询：
    # 让每个模式都被作为一次目标模式，形成 m=n 条查询
    m = n
    queries = []
    for i in range(n):
        # 查询字符串 s 取 all_patterns[i] 本身，目标索引为 i+1（1-based）
        queries.append((all_patterns[i], i + 1))

    return n, m, k, all_patterns, queries


def main(n):
    """
    无 input() 版主函数。
    n: 规模，用于生成测试数据。
    """
    import sys

    # 生成测试数据
    n, m, k_local, all_patterns, queries = generate_test_data(n)

    # 将生成的测试数据映射到原程序变量名
    global k
    k = k_local
    patterns = {}
    all_list = []

    for i in range(n):
        s_local = all_patterns[i]
        patterns[s_local] = i
        all_list.append(s_local)

    dg = Graph(n)

    for q_s, mt in queries:
        mt = mt - 1  # 转换为 0-based
        global s, outs
        s = q_s
        outs = set()
        temp = [0 for _ in range(k)]
        gen(temp, 0)

        if all_list[mt] not in outs:
            print("no")
            sys.exit(0)

        for pat in outs:
            if pat != all_list[mt] and pat in patterns:
                dg.addEdge(mt, patterns[pat])

    if dg.isCyclic():
        print("no")
    else:
        dg.topologicalSort()


if __name__ == "__main__":
    # 示例：调用 main(5) 运行规模为 5 的测试
    main(5)