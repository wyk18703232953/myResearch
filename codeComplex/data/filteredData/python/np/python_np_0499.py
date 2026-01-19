import sys

sys.setrecursionlimit(10**5)
int1 = lambda x: int(x)-1
p2D = lambda x: print(*x, sep="\n")
inf = 10**16
md = 10**9+7

trie = [{}]

def push(s, val, k):
    now = 0
    for c in s:
        if c not in trie[now]:
            trie[now][c] = len(trie)
            trie.append({})
        now = trie[now][c]
    trie[now]["end"] = val

def match(s, k):
    res = []
    stack = [(0, 0)]
    while stack:
        u, i = stack.pop()
        if i == k:
            res.append(trie[u]["end"])
            continue
        if s[i] in trie[u]:
            stack.append((trie[u][s[i]], i+1))
        if "_" in trie[u]:
            stack.append((trie[u]["_"], i+1))
    return res

def build_deterministic_input(n):
    if n <= 0:
        n = 1
    k = 3
    if n == 1:
        n_words = 1
        m_edges = 1
    else:
        n_words = n
        m_edges = n
    words = []
    for i in range(n_words):
        s = []
        for j in range(k):
            c = chr(ord('a') + (i + j) % 3)
            s.append(c)
        words.append("".join(s))
    patterns = []
    for i in range(m_edges):
        s = list(words[i % n_words])
        if i % 4 == 0:
            pos = i % k
            s[pos] = '_'
        patterns.append("".join(s))
    us = [(i + 1) % n_words for i in range(m_edges)]
    return n_words, m_edges, k, words, patterns, us

def core(n_words, m_edges, k, words, patterns, us):
    global trie
    trie = [{}]
    for i in range(n_words):
        push(words[i], i, k)
    to = [[] for _ in range(n_words)]
    for i in range(m_edges):
        s = patterns[i]
        u = us[i]
        vv = match(s, k)
        notmatch = True
        for v in vv:
            if u == v:
                notmatch = False
            else:
                to[u].append(v)
        if notmatch:
            print("NO")
            return
    vis = [-1] * n_words
    topo = []
    for u in range(n_words):
        if vis[u] == 1:
            continue
        stack = [u]
        while stack:
            u = stack.pop()
            if vis[u] == -1:
                vis[u] = 0
                stack.append(u)
                for v in to[u]:
                    if vis[v] == 0:
                        print("NO")
                        return
                    if vis[v] == -1:
                        stack.append(v)
            elif vis[u] == 0:
                topo.append(u + 1)
                vis[u] = 1
    print("YES")
    print(*topo[::-1])

def main(n):
    n_words, m_edges, k, words, patterns, us = build_deterministic_input(n)
    core(n_words, m_edges, k, words, patterns, us)

if __name__ == "__main__":
    main(5)