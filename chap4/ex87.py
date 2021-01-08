# Shipping Calculator

def shipping_calculator(n):
    first_item = 10.95
    add_item = 2.95
    shipping_charge = round(first_item + (n-1)*add_item, 2)
    return shipping_charge


def main() -> object:
    num_items = int(input('enter the number of items you purchased: '))
    charge = shipping_calculator(num_items)
    print(f"the shipping charge for {num_items} items is ${charge:.2f}")


if __name__ == '__main__':
    main()
