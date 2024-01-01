transactions = [10.1, 22.0, 32.2, 17.8, 55.0]

max_transaction = transactions[0]

for transaction in transactions[1:]:
    if transaction > max_transaction:
        max_transaction = transaction

print(f"Maximum {max_transaction}")
