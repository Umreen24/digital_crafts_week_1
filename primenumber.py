# A prime number is a whole number greater than 1 whose only factors are 1 and itself


number = int(input("Enter number here: "))

for index in range(2, number):
    if number % index == 0:
        print("Not prime")
        break 
else: 
    print("Prime")
