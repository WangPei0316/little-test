while True:
    try:
        count = int(input('Enter count:'))
        price = int(input('Enter price for each one:'))
        price_all = 'Pay:' + str(count*price)
        print(price_all)
        break
    except ValueError:
        print("Error,please enter numeric one.")
