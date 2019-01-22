from collections import OrderedDict

def main():
    net_prices = OrderedDict()
    
    for _ in range(int(input())):
        item, price = input().rsplit(maxsplit=1)
        net_prices[item] = net_prices.get(item, 0) + int(price)
    
    for item in net_prices:
        print(item, net_prices[item])

if __name__ == '__main__':
    main()
