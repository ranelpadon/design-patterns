"""
Decorator/Wrapper Design Pattern:

- augments an object without inheritance
- keeps new functionalities separate (Single Responsibility Principle)
- does not alter existing code (Open-Closed Principle)
- prevents subclasses explosion
- makes it possible to have composable changes which is messy w/ multiple inheritance
    - avoids classes like `TicketWithDiscountWithVoucher`
- needs to implement the dunder methods when the target object has lots of attributes/methods
    that you're not interested
"""


### Example 1 ###


class Text:
    def __init__(self, value):
        self.value = value

    def render(self):
        return self.value


class Bold:
    def __init__(self, text):
        self.text = text

    def render(self):
        return f'<b>{self.text.render()}</b>'


class Italic:
    def __init__(self, text):
        self.text = text

    def render(self):
        return f'<i>{self.text.render()}</i>'


print(Text('hello').render())  # 'hello'
print(Bold(Text('hello')).render())  # '<b>hello</b>'
print(Italic(Text('hello')).render())  # '<i>hello</i>'
print(Bold(Italic(Text('hello'))).render())  # '<b><i>hello</i></b>'



### Example 2 ###


from abc import ABC, abstractmethod


class TicketBase(ABC):
    @abstractmethod
    def get_price(self):
        pass


class Ticket(TicketBase):
    def get_price(self):
        return 100


class VIPDiscount(TicketBase):
    def __init__(self, ticket):
        self.ticket = ticket

    def get_price(self):
        return self.ticket.get_price() - 50


class BlackFridayDiscount(TicketBase):
    def __init__(self, ticket):
        self.ticket = ticket

    def get_price(self):
        return self.ticket.get_price() - 20


print(Ticket().get_price())  # 100
print(VIPDiscount(Ticket()).get_price())  # 50
print(BlackFridayDiscount(Ticket()).get_price())  # 80
print(VIPDiscount(BlackFridayDiscount(Ticket())).get_price())  # 30
