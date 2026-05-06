def calculate_due_amount():
    bill = float(input("Enter the bill amount: "))
    paid = float(input("Enter the amount paid: "))
    balance = bill - paid
    if balance > 0:
        print("Amount due: ", balance)
    elif balance < 0:
        print("Change to be returned: ", -balance)
    else:
        print("No amount due. Thank you for the exact payment!")
calculate_due_amount()