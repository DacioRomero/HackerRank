from itertools import groupby

if __name__ == '__main__':
    for k, g in groupby(input()):
        print('(%d, %d)' % (len(list(g)), int(k)), end=' ')
