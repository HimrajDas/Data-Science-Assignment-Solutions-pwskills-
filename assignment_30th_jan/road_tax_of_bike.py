def main():
    bike_price = int(input("Enter bike cost: "))
    tax(bike_price)


def tax(cost_price):
    if cost_price > 100000:
        print("15%")
    elif cost_price > 50000:
        print("10%")
    else:
        print("5%")


main()