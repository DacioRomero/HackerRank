def main():
    n, m = map(int, input().split())
    spreadsheet = [list(map(int, input().split())) for _ in range(n)]
    
    key = int(input())
    spreadsheet.sort(key=lambda x: x[key])
    
    for line in spreadsheet:
        print(*line)

if __name__ == '__main__':
    main()
