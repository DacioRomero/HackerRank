from itertools import combinations

if __name__ == '__main__':
    S, k = input().split(' ')
    S = sorted(S)
    k = int(k)

    for i in range(1, k + 1):
        for j in list(combinations(S, i)):
            print(''.join(j))
