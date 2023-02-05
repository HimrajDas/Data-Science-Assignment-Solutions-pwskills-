def main():
    # pattern2(5)
    pattern3(5)


def pattern1(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print("*", end=" ")
            j += 1
        print()
        i += 1


def pattern2(n):
    i = 0
    while i <= n:
        j = 0
        while j <= n:
            print("*", end=" ")
            j += 1
        print()
        i += 1



def pattern3(n):
    i = 0
    while i <= n:
        j = 0
        while j < n - i:
            print("*", end=" ")
            j += 1
        print()
        i += 1



main()