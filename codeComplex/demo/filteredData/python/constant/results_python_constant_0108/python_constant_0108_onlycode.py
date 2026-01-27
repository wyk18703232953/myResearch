import sys

def num_ops(low, high):
    if high % low == 0:
        return high // low
    else:
        return (high // low) + num_ops(high % low, low)

def main():
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        low, high = [int(i) for i in sys.stdin.readline().strip().split()]
        print(num_ops(low, high))




if __name__ == '__main__':
    main()