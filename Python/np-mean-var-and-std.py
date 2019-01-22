import numpy

def main():
    my_array = numpy.array([list(map(int, input().split())) for _ in range(int(input().split()[0]))])
    numpy.set_printoptions(legacy='1.13')
    print(numpy.mean(my_array, axis=1))
    print(numpy.var(my_array, axis=0))
    print(numpy.std(my_array))

if __name__ == '__main__':
    main()
