import math

def main():
    AB, BC = int(input()), int(input())
    print(f'{round(math.degrees(math.atan2(AB, BC)))}°')

if __name__ == '__main__':
    main()
