addison-tech's Solution to Build a Budget App Project
Close
×
PY
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry['description'][:23]
            amt = "{0:.2f}".format(entry['amount'])
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    spendings = []
    total_spent = 0

    # Calculate spend per category
    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spendings.append({'name': category.name, 'spent': spent})
        total_spent += spent

    # Compute percentage spent rounded down to nearest 10
    for item in spendings:
        item['percent'] = int((item['spent'] / total_spent) * 100 // 10) * 10

    # Chart header
    chart = "Percentage spent by category\n"

    # Chart bars from 100 down to 0
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for item in spendings:
            if item['percent'] >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    # Separator line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical category names
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += category.name[i] + "  "
            else:
                line += "   "
        if i != max_length - 1:
            line += "\n"
        chart += line

    return chart

Add Budget App solution
