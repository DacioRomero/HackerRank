def main():
    _, array = input(), map(int, input().split())
    A, B = (set(map(int, input().split())) for _ in range(2))
    print(sum((x in A) - (x in B) for x in array))

if __name__ == '__main__':
    main()
