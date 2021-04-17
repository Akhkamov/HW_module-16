class Client:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __str__(self):
        return f"Клиент: {self.name} {self.surname}"

class Balance:
    def __init__(self, balance):
        self.balance = balance
    def __str__(self):
        return f"Бфлфнс: {self.balance} рублей"
