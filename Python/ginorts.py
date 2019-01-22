def main():
    print(''.join(sorted(input(), key=lambda s: (s.isdigit(), s.isdigit() and int(s) % 2 == 0, s.isupper(), s.islower(), s))))

if __name__ == '__main__':
    main()
