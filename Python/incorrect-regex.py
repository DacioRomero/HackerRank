import re

if __name__ == '__main__':
    for i in range(int(input())):
        try:
            re.compile(input())
            print(True)
        except re.error:
            print(False)
