def pay_bill(expenses, percent_commission = 9.8, special_offer_amount = None):
    total_expense = sum(expenses)
    comission = percent_commission
    if special_offer_amount is not None and total_expense > special_offer_amount:
        comission += 1.2
    return total_expense + ((comission / 100) * 100)

expense = [1200,12300,13000,1100,10]
print(pay_bill(expense, 3.2, 1000))