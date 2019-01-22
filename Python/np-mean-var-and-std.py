import numpy

def main():
    _, my_array = input(), numpy.array([list(map(int, input().split())) for _ in range(2)])
    numpy.set_printoptions(legacy='1.13')
    print(numpy.mean(my_array, axis=1))
    print(numpy.var(my_array, axis=0))
    print(numpy.std(my_array))

if __name__ == '__main__':
    main()
