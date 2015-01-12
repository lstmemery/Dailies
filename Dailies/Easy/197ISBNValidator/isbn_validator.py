import random


def isbn_generator():
    isbn10 = [random.randint(0, 9) for _ in range(0, 9)]
    checksum = sum([isbn10[n] * (10-n) for n in range(0, 9)]) % 11
    if checksum == 10:
        checksum = 'X'
    isbn10.append(checksum)
    return ''.join(map(str, isbn10))

if __name__ == '__main__':
    print isbn_generator()