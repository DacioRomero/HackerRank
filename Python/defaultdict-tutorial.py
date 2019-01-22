from collections import defaultdict

def main():
    n, m = map(int, input().split())
    indices_dict = defaultdict(list)
    
    for i in range(n):
        indices_dict[input()].append(i + 1)
    
    for _ in range(m):
        indices = indices_dict[input()]
        
        if len(indices) == 0:
            print(-1)
        else:
            print(*indices)

if __name__ == '__main__':
    main()
