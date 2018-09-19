if __name__ == '__main__':
    phys_class = [[input(), float(input())] for _ in range(int(input()))]

    for student in sorted(filter(lambda x: x[1] == sorted({x[1] for x in phys_class})[1], phys_class)):
        print(student[0])
