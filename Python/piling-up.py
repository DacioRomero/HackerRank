from collections import deque

def main():
    for _ in range(int(input())):
        _, cubes = input(), deque(map(int, input().split()))
        
        for cube in sorted(cubes, reverse=True):
            if cube == cubes[-1]:
                cubes.pop()
            elif cube == cubes[0]:
                cubes.popleft()
            else:
                print('No')
                break
        else:
            print('Yes')
                
if __name__ == '__main__':
    main()
