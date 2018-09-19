import string

def print_rangoli(size):
    top = ['-'.join(string.ascii_lowercase[size-1:i-1 if i-1 > -1 else None:-1]
                    + string.ascii_lowercase[i+1:size]).center(size * 4 - 3, '-')
           for i in range(size - 1, -1, -1)]
    print('\n'.join(top + top[-2::-1]))
