from collections import deque
import random

def removeUsed(adj, used):
    to_remove = []
    for s in adj:
        if used[s]:
            to_remove.append(s)
    for s in to_remove:
        adj.remove(s)

def solve(a, s):  # a - adjacency list as list of sets, s - sequence
    if s[0] != 0:
        return False
    q = deque()
    q.append(0)
    i, n, cur = 1, len(a), -1
    used = [False] * n
    used[0] = True
    while i < n:
        if cur == -1:
            if not q:
                return False
            cur = q.popleft()
            removeUsed(a[cur], used)
        if not a[cur]:
            cur = -1
            continue
        cur_s = s[i]
        i += 1
        if cur_s not in a[cur]:
            return False
        a[cur].remove(cur_s)
        q.append(cur_s)
        used[cur_s] = True
    return True

def generate_tree(n):
    """Random tree on vertices 0..n-1."""
    a = [set() for _ in range(n)]
    for v in range(1, n):
        u = random.randint(0, v - 1)
        a[u].add(v)
        a[v].add(u)
    return a

def generate_sequence(n):
    """Random permutation of 0..n-1."""
    s = list(range(0, n))
    random.shuffle(s)
    return s

def main(n):
    random.seed(0)  # fixed seed for reproducibility; remove or change as needed
    a = generate_tree(n)
    s = generate_sequence(n)
    # Make a deep copy of adjacency sets because solve modifies them
    a_copy = [set(neigh) for neigh in a]
    result = solve(a_copy, s)
    print("Yes" if result else "No")

# 示例调用（测试时可取消注释）
# if __name__ == "__main__":
#     main(5)