import itertools

def main():
    list_a = list(map(int, input().split(' ')))
    list_b = list(map(int, input().split(' ')))
    return list(itertools.product(list_a, list_b))

if __name__ == '__main__':
    print(*main())
