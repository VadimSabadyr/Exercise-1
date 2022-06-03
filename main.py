class Name:

    def __init__(self, first_n, last_n):
        self.first_n = first_n
        self.last_n = last_n

    def first_name(self):
        return self.first_n.casefold() and self.first_n.capitalize()

    def last_name(self):
        return self.last_n.casefold() and self.last_n.capitalize()

    def full_name(self):
        return f'{self.first_name()} {self.last_name()}'

    def initials(self):
        return f"{self.first_name()[0]}.{self.last_name()[0]}"


