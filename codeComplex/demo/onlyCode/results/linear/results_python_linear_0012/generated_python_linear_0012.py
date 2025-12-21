def prime(n):
    j = 3
    while j * j <= n:
        if n % j == 0:
            return False
        j += 2
    return True

ref = [2]
for j in range(3, 1000, 2):
    if prime(j) == True:
        ref.append(j)

def check(n):
    for j in range(1, len(ref) - 1):
        v = n - ref[j] - 1
        if ref[j - 1] == v or ref[j + 1] == v:
            return True
        if j > n:
            break
    return False

arr = []
for j in range(3, 1001, 2):
    if prime(j) == True and check(j) == True:
        arr.append(j)

def main(n):
    k = n // 2
    count = 0
    for j in range(2, n + 1):
        if j in arr:
            count += 1
    if count >= k:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    print(main(1000))