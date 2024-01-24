while True:
    NumOfTickets = int(input("How many would you like to buy?: "))
    if NumOfTickets > 0 and NumOfTickets < 26:
        break

if NumOfTickets < 10:
    discount = 0
else:
    if NumOfTickets < 20:
        discount = 0.1
    else:
        discount = 0.2

cost  = NumOfTickets * 20 * ( 1- discount)
print(f"Your ticket cost {cost}")
