n = int(input())
a = list(map(int, input().split()))
w = sum(a[i] == i + 1 for i in range(n))
print("Petr") if w >= n // 1000 else print("Um_nik")
