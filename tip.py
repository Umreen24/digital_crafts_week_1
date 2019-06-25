def tip_calc(total_amount, tip_percent):
    return int(total_amount) * int(tip_percent)/100

total_amount = int(input("Enter total amount: "))
tip_percent = int(input("Enter tip percent: "))

result = tip_calc(total_amount, tip_percent)
print(result)