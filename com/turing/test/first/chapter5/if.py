cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else: 
        print(car.title())

age = 19
if age >= 18:
    print("You are old enough to vote!")


print('---------------')
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                    'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else: 
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

