def main():
    percentage = int(input("Enter your percentage: "))
    check_grade(percentage)


def check_grade(percentage):
    if percentage > 90:
        print("A")
    elif percentage > 80:
        print("B")
    elif percentage >= 60:
        print("C")
    else:
        print("D")


main()