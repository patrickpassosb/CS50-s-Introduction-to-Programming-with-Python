amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amount_due = amount_due - coin

change_owed = 0
if amount_due == 0:
    change_owed = 0
elif amount_due < 0:
    change_owed = amount_due * -1

print(f"Change Owed: {change_owed}")

