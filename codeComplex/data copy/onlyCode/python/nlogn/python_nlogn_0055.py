n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
target = (sum(coins)+2)//2

count = 1
total = coins[count-1]
while total < target:
    count += 1
    total += coins[count-1]

print(count)

