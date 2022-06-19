import sys
import os


def prime(s):
    s = int(sys.argv[1])
    if (s == 1):
        print(s, "is not really a prime number since prime numbers are greater than 1")
    elif (s == 2) or (s == 3):
        print(s, "is a prime number")
    elif (s % 3 == 0):
        print(s, "is not a prime number")

    else:
        for num in range(2, s):
            if (s % num == 0):
                print(s, "is not a prime number")
                break
            else:
                print(s, "is a prime number")
                break
def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
