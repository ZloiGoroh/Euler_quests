# Searching for special triples of Pythagoras

limit = 1000

def main():
    for a in range(1, limit):
        for b in range(1, limit):
            c = limit - a - b
            if a*a + b*b == c*c:
                print(a*b*c)
                return


if __name__ == '__main__':
    main()