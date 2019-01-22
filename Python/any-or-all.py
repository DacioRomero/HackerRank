_, integers = input(), input().split()
print(all(map(lambda i: int(i) > 0, integers)) and any(map(lambda i: i == i[::-1], integers)))
