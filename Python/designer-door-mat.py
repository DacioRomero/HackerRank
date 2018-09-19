if __name__ == '__main__':
    N, M = map(int, input().split())

    half = [('.|.' * (1 + i * 2)).center(M, '-') for i in range(N // 2)]
    
    print('\n'.join(half))
    print('WELCOME'.center(M, '-'))
    print('\n'.join(half[::-1]))
