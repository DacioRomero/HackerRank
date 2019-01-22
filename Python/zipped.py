def main():
    n, x = map(int, input().split())
    
    for student in zip(*(map(float, input().split()) for _ in range(x))):
        print(sum(student) / len(student))

if __name__ == '__main__':
    main()
