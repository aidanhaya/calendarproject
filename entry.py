class Entry:
    def __init__(self, name, amount, category, type):
        self.name = name
        self.amount = float(amount)
        self.category = category
        self.type = type

    def get_type(self):
        return self.type

    def get_amount(self):
        return self.amount

    def get_category(self):
        return self.category