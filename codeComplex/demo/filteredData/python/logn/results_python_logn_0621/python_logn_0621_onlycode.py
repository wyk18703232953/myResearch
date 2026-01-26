class Read:
    @staticmethod
    def int():
        return int(input())
 
    @staticmethod
    def list(sep=' '):
        return input().split(sep)
 
    @staticmethod
    def list_int(sep=' '):
        return list(map(int, input().split(sep)))
    @staticmethod
    def calc(sep = '', k = ''):
        count = 0
        for i in range(sep):
            j = sep - i
            sum = ((i + 1)* i) / 2
            if (sum - j == k):
                return j
        return count
 
 
def main():
    n, k = Read.list_int()
    print(Read.calc(n, k))
        
 
main()