# this file calculate total sum of all products

def calculate_total():
    prices = []
    print("Enter price: (end for stop)")

    while True:
        user_input = input("Price: ")
        if user_input.lower() == 'end':
            break
        try:
            price = float(user_input)
            prices.append(price)
        except ValueError:
            print("Enter number or END for stop")

    if prices:
        total_price = sum(prices)
        print(f"Total sum is: {total_price:.2f}")
    else:
        print("You not enter any price.")

calculate_total()

