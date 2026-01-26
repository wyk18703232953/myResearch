import itertools

mmm = 998244353

def count_k(ka, k, t):
    if t == 0:
        return ka[k][0] + ka[k][1] + ka[k][2] + ka[k-1][3]
    if t == 1:
        return ka[k-1][0] + ka[k][1] + ka[k-2][2] + ka[k-1][3]
    if t == 2:
        return ka[k-1][0] + ka[k-2][1] + ka[k][2] + ka[k-1][3]
    if t == 3:
        return ka[k-1][0] + ka[k][1] + ka[k][2] + ka[k][3]

def run_algorithm(n, k):
    kas = [[0,0,0,0],[1,0,0,1],[0,1,1,0]]
    for i in range(1, n):
        if len(kas) < k + 1:
            kas.append([0,0,0,0])
            kas.append([0,0,0,0])
        for kk in range(min(len(kas)-1, k), 1, -1):
            kas[kk] = [count_k(kas, kk, t) % mmm for t in range(4)]
    return sum(kas[k]) % mmm if k < len(kas) else 0

def main(n):
    if n < 1:
        n = 1
    k = n // 2
    if k < 2:
        k = 2
    return run_algorithm(n, k)

if __name__ == "__main__":
    result = main(10)
    print(result)