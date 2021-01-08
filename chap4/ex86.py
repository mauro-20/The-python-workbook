# Taxi Fare


def taxi_fare(km):
    # base fare 4$
    base_fare = 4
    # additional fare 0.25$ every 140m
    add_fare = 0.25
    # compute total fare
    total_fare = base_fare + km//0.140 * add_fare

    return total_fare


def main():
    km = float(input('enter how many km you use the taxi: '))
    return print(f"the total taxi fare for {km}km is ${taxi_fare(km):.2f}")


if __name__ == '__main__':
    main()
