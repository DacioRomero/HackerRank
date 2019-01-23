def main():
    _, english = input(), set(input().split())
    _, french = input(), set(input().split())
    print(len(english ^ french))

if __name__ == '__main__':
    main()
