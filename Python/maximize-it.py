import itertools

def main():
    list_count, divisor = list(map(int, input().split(' ')))

    lists = (list(map(int, input().split()))[1:] for _ in range(list_count))

    results = (sum(map(lambda x: x * x, l)) % divisor for l in itertools.product(*lists))
    
    print(max(results))

if __name__ == '__main__':
    main()
