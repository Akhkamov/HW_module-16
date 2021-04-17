class Client:
    def __init__(self, name, surname, city, status):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status
    def __str__(self):
        return f"Guest: {self.name} {self.surname}, {self.city},статус {self.status}"