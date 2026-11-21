transactions = [
    {"amount": 500, "category": "food", "kind": "expense", "comment": "l"},
    {"amount": 3000, "category": "salary", "kind": "income", "comment": "advance"},
]

by_amount = sorted(transactions, key=lambda t: t["amount"])


print(by_amount)
