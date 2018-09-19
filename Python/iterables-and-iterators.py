from itertools import combinations

if __name__ == '__main__':
    N, L, K = int(input()), input().split(), int(input())

    # Get all combinations of the string L up to K
    C = list(combinations(L, K))
    # Filter every tuple with 'a'
    F = filter(lambda c: 'a' in c, C)

    print(len(list(F)) / len(C))
