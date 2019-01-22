from collections import deque

def main():
    d = deque()

    for _ in range(int(input())):
        method, *arguments = input().split()
        getattr(d, method)(*arguments)
    
    print(*d)

if __name__ == '__main__':
    main()
