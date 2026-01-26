n , k = map(int, input().split())
#K-ОСТАЛОСЬ, N-КОЛ-ВО ХОДОВ
# x - сколько конфет съели, n - x ходов на которых конфеты добавляли
# x = n, то останется -n конфет, это < k
# x = 0, останется (1 + n) * n / 2 >= k
l = 0
r = n
while r - l > 1:
    mid = (r + l) // 2
    a = n - mid
    if ((1 + a) * a) // 2 >= k + mid:
        l = mid
    else:
        r = mid
print(l)