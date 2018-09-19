from itertools import combinations_with_replacement

if __name__ == '__main__':
    S, k = input().split(' ')
    S = sorted(S)
    k = int(k)

    for j in list(combinations_with_replacement(S, k)):
        print(''.join(j))
