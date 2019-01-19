import itertools

def main():
    s, k = input().split(' ')
    k = int(k)
    s = sorted(s)

    perms = itertools.permutations(s, k)

    for i in perms:
        print(''.join(i))

if __name__ == '__main__':
    main()
