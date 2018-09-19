if __name__ == '__main__':
    for i in range(int(input())):
        a, b = input().split(' ')
        try:
            print(int(a) // int(b))
        except (ZeroDivisionError, ValueError) as e:
            print('Error Code:', e)
