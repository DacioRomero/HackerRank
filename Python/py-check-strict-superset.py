def main():
    A = set(map(int, input().split()))

    for _ in range(int(input())):
        subset =  set(map(int, input().split()))
        if A.intersection(subset) != subset:
            print('False')
            break
    else:
        print('True')

if __name__ == '__main__':
    main()
