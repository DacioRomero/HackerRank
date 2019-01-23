def main():
    _, M = input(), set(map(int, input().split()))
    _, N = input(), set(map(int, input().split()))
    print(*sorted(M ^ N), sep='\n')

if __name__ == '__main__':
    main()
