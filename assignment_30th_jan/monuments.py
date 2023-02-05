def main():
    city_name = input("Enter city name: ").title()
    show_monuments(city_name)


def show_monuments(city):
    if city == "Delhi":
        print("Red Fort")
    elif city == "Agra":
        print("Taj Mahal")
    elif city == "Jaipur":
        print("Jal Mahal")
    else:
        print("Only Delhi, Agra, Jaipur supported.")


main()