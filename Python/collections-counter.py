from collections import Counter

def main():
    input()
    shoes = Counter(input().split())
    sales = 0

    for _ in range(int(input())):
        cur_shoe, price = input().split()
        price = int(price)

        if shoes[cur_shoe] != 0:
            sales += price
            shoes[cur_shoe] -= 1
    
    print(sales)

if __name__ == '__main__':
    main()
