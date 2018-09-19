from itertools import groupby

if __name__ == '__main__':
    n = int(input())
    arr = list(groupby(sorted(map(int, input().split()))))
    print(arr[n - 2][0])
