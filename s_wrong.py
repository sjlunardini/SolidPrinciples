""" S the incorrect way """


class Book:
    """Book Data Class"""

    def __init__(
        self,
        name: str,
        author_name: str,
        year: int,
        price: int,
        isbn: str,
    ) -> None:
        self.name = name
        self.author_name = author_name
        self.year = year
        self.price = price
        self.isbn = isbn


class Invoice:
    """Invoice Object"""

    def __init__(
        self,
        book: Book,
        quantity: int,
        discount_rate: float,
        tax_rate: float,
    ) -> None:
        self.book = book
        self.quantity = quantity
        self.discount_rate = discount_rate
        self.tax_rate = tax_rate

    @property
    def price(self) -> float:
        """Return Price"""
        return (self.book.price - self.book.price * self.discount_rate) * self.quantity

    @property
    def price_with_taxes(self) -> float:
        """Return Price with Taxes"""
        return self.price * (1 + self.tax_rate)

    def print_invoice(self) -> None:
        """Print Invoice to terminal"""
        print(f"{self.quantity} x {self.book.name}\t${self.book.price}")
        print(f"Discount Rate: {self.discount_rate}")
        print(f"Tax Rate: {self.tax_rate}")
        print(f"Total: ${self.price_with_taxes}")

    def save_invoice(self, filename: str) -> None:
        """Save invoice to file"""


if __name__ == "__main__":
    the_fellowship = Book(
        name="The Fellowship of the Ring",
        author_name="Tolkien",
        year=1954,
        price=100,
        isbn="abcde",
    )
    fellowship_invoice = Invoice(
        book=the_fellowship, quantity=2, discount_rate=0.1, tax_rate=0.065
    )
    fellowship_invoice.print_invoice()
