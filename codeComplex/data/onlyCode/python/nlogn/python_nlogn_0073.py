#!/usr/bin/env python3

if __name__ == "__main__":
	n, k = map(int, input().split())
	ais = []
	for i in range(n):
		ais.append(list(map(int, input().split())))
	ais.sort(key = lambda x: (-x[0], x[1]))
	print(ais.count(ais[k-1]))
