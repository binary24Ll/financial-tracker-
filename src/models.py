class Transaction:
    def __init__(self, amount, category, kind, comment):
        self.amount = amount 
        self.category = category
        self.comment = comment
        self.kind = kind 
    
    def summary(self):
       return f"{self.kind}: {self.amount}  ({self.category})"
    


