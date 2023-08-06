#Using nested loops, draw the following shape through print statements:
# XXXXX
# XX
# XXXXX
# XX
# XX

def printLetter():
    numbers = [5, 2, 5, 2, 2]
    for num in numbers:
        for i in range(num):
            print('X', end='', flush=True)
        print("\n", end='')


if __name__ == '__main__':
    printLetter()