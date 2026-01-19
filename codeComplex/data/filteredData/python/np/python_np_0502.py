import collections
import functools
import heapq
import bisect
import math

def binary(s):
    ans = set()
    for i in range(2 ** len(s)):
        x = []
        for j in range(len(s)):
            if (i >> j) & 1:
                x.append(s[j])
            else:
                x.append('_')
        ans.add(''.join(x))
    return ans

seen = set()
visited = set()
ans = []
graph = {}
n = 0

def dfs(i):
    visited.add(i)
    seen.add(i)
    for j in graph[i]:
        if j in visited:
            return True
        if j in seen:
            continue
        if dfs(j):
            return True
    ans.append(str(i))
    visited.remove(i)
    return False

def topo():
    seen.clear()
    for i in range(1, n + 1):
        if i in seen:
            continue
        if dfs(i):
            return False
    return True

def generate_input(n):
    # n controls number of variables; we scale m and k deterministically
    if n <= 0:
        n = 1
    m = n * 2
    k = max(1, n // 2)

    # generate n distinct strings of length L over 'a'..'z' deterministically
    # encode i in base-26, fixed length L
    L = max(1, (n.bit_length() + 4) // 5)
    vars_list = []
    for i in range(n):
        x = i
        chars = []
        for _ in range(L):
            chars.append(chr(ord('a') + (x % 26)))
            x //= 26
        vars_list.append(''.join(chars))

    # generate m clauses:
    # each clause is (pattern_string, index)
    # pattern is based on two variables; index cycles over 1..n
    clauses = []
    for i in range(m):
        idx = (i % n) + 1
        a = vars_list[i % n]
        b = vars_list[(i * 7 + 3) % n]
        pattern_chars = []
        for j in range(L):
            if j % 2 == 0:
                pattern_chars.append(a[j])
            else:
                pattern_chars.append(b[j])
        pattern = ''.join(pattern_chars)
        clauses.append((pattern, idx))

    return n, m, k, vars_list, clauses

def main(input_n):
    global graph, ans, n
    n, m, k, vars_list, clauses = generate_input(input_n)

    d = {}
    dop = {}
    for i in range(1, n + 1):
        d[i] = vars_list[i - 1]
        dop[d[i]] = i

    res_outputs = []
    graph = collections.defaultdict(list)
    ans.clear()

    for s0, ind in clauses:
        ind_int = ind
        sset = binary(s0)
        if d[ind_int] not in sset:
            res_outputs.append('NO')
            break
        for pat in sset:
            if pat in dop and dop[pat] != ind_int:
                graph[dop[pat]].append(ind_int)
    else:
        if topo():
            res_outputs.append('YES')
            res_outputs.append(' '.join(ans))
        else:
            res_outputs.append('NO')

    out = '\n'.join(res_outputs)
    print(out)
    return out

if __name__ == "__main__":
    main(5)