x, k = map(int, input().split())

twoPow = pow(2, k, 1000000007)

minQ = max(0, (x * twoPow - twoPow + 1))
minQ *= 2

maxQ = (x * twoPow * 2)

print(((maxQ*(maxQ+1)//2 - minQ*(minQ+1)//2 + minQ) // (maxQ-minQ+1)) % 1000000007)