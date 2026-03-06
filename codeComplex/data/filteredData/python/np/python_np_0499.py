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
            if "end" in trie[u]:
                res.append(trie[u]["end"])
            continue
        if s[i] in trie[u]:
            stack.append((trie[u][s[i]], i+1))
        if "_" in trie[u]:
            stack.append((trie[u]["_"], i+1))
    return res

def main(n):
    global trie
    trie = [{}]

    if n <= 0:
        print("YES")
        print()
        return

    k = 5
    num_chars = 3
    n_words = n
    m_queries = n

    words = []
    for i in range(n_words):
        s = []
        x = i
        for j in range(k):
            s.append(chr(ord('a') + (x % num_chars)))
            x //= num_chars
        words.append(''.join(s))

    for i in range(n_words):
        push(words[i], i, k)

    to = [[] for _ in range(n_words)]

    # generate queries
    for i in range(m_queries):
        u = i % n_words
        w = words[u]
        s = list(w)
        pos = i % k
        s[pos] = '_'
        s = ''.join(s)

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

if __name__ == "__main__":
    main(10)