def main():
    n = int(input("Enter any number: "))
    print(divisible_by_3(n))


def divisible_by_3(n):
    ans = 0
    while n >= 10:
        if (n % 3 == 0):
            ans += 1
        n /= 3

    return ans


main()