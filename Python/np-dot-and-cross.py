import numpy

def main():
    N = int(input())
    A, B = [numpy.array([list(map(int, input().split())) for _ in range(N)]) for _ in range(2)]
    print(numpy.matmul(A, B))

if __name__ == '__main__':
    main()
