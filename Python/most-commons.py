if __name__ == '__main__':
    s = input()
    letters = sorted(set(s))
    occurences = []

    for letter in letters:
        occurences.append((letter, s.count(letter)))

    occurences.sort(key=lambda x: x[1], reverse=True)

    for occurence in occurences[:3]:
        print(*occurence)
