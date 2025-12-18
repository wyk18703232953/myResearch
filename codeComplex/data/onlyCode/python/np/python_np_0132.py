def main():
    input()
    acc = {0: 0}
    for p, c in zip(list(map(int, input().split())),
                    list(map(int, input().split()))):
        adds = []
        for b, u in acc.items():
            a = p
            while b:
                a, b = b, a % b
            adds.append((a, u + c))
        for a, u in adds:
            acc[a] = min(u, acc.get(a, 1000000000))
    print(acc.get(1, -1))


if __name__ == '__main__':
    main()



# Made By Mostafa_Khaled