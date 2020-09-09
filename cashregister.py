def cash_register():
    print("Welcome to Austin's cash register! Please see instructions below")
    print('***********************************************************************************')
    print("if done 'shopping' please type 'y' after entering last product price")
    print('If still calculating press the "enter" key after typing in the product price')
    print('the program can take any floating integer, but will round to the 10th place')
    print('***********************************************************************************')
    total_price = 0
    ready = 'n'
    product_price = float(input( 'Product Price: \n'))
    ready = str(input('Are you done shopping? y/n: '))
    if ready == 'y':
        print("Please pay",'$',product_price,'now')
        total_price = product_price
    elif(product_price < 0):
        print(' Must be a positive number!')
    else:
        while (ready != 'y'):            
            if product_price < 0:
                print('please enter valid price')
            elif ready != 'y':
                total_price += product_price
                print('current total is','$',round(float(total_price), 2))
                product_price = float(input( 'Product Price: \n'))
                ready = str(input())
        total_price += product_price        
        print("Please pay",'$',round(float(total_price),2),'now')
    cash_used = float(input( 'Cash Used: \n'))
    if (cash_used < 0):
        print(' Must be a positive number!')
    elif cash_used < total_price:
        print('You too broke! come back with more money.')
    else:
        change_needed1 = (cash_used - total_price)
        change_needed = change_needed1
        num_hundreds = (change_needed // 100)
        change_needed -= num_hundreds * 100 # subtract 100 dollar bills amount from total change 
        num_fifties = change_needed  // 50
        change_needed -= num_fifties * 50 # subtract 50 dollar bills amount from change
        num_twenty =  change_needed  // 20
        change_needed -= num_twenty * 20# subtract 20 dollar bills amount from change 
        num_ten =  change_needed  // 10
        change_needed -= num_ten * 10 # subtract 10 dollar bills amount from change
        num_fives = change_needed // 5
        change_needed -= num_fives * 5
        num_ones = change_needed // 1
        change_needed -= num_ones * 1
        num_cents = round(change_needed  * 100)
        change = num_cents
        quarters = change // 25
        change -= quarters * 25
        dimes = change // 10
        change -= dimes * 10
        nickels = change // 5
        change -= nickels * 5
        pennies = change // 1
        print("your change is:", '$',round(change_needed1, 2))
        print('*******************************************')
        print (int(num_hundreds), ('hundred dollar bills'))
        print (int(num_fifties),('Fifty dollar bills'))
        print (int(num_twenty), ('tewnty dollar bills'))
        print (int(num_ten), ('ten dollar bills'))
        print (int(num_fives), ('five dollar bills'))
        print (int(num_ones), ('one dollar bills '))
        print ('*******************************************')
        print (int(quarters), ('quarters'))
        print (int(dimes), ('dimes'))
        print (int(nickels), ('nickels'))
        print (int(pennies), ('pennies \n'))
while True:
    cash_register()
