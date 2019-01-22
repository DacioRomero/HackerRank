count, index = int(input()), input().split().index('MARKS')
print('%.2f' % (sum([float(input().split()[index]) for _ in range(count)]) / count))
# from collections import namedtuple
# count, Student = int(input()), namedtuple('Student', input())
# students = (Student(*input().split()) for _ in range(count))
# print('%.2f' % (sum(map(lambda s: float(s.MARKS), students)) / count))
