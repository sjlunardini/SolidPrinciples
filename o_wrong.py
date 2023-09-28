""" O - the incorrect way 

Your boss asks to add a method to save the invoice to a database
along with a file.
"""
from s_right import Book, Invoice


class InvoicePersistence:
    """Invoice Persistence Object"""

    def __init__(self, invoice: Invoice) -> None:
        self.invoice = invoice

    def save_invoice_to_file(self, filename: str) -> None:
        """Save invoice to file"""
        print(f"Saved to {filename}")

    def save_invoice_to_database(self) -> None:
        """Save invoice to database"""
        print("Saved to database")


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
    InvoicePersistence(fellowship_invoice).save_invoice_to_file("Inv12345.txt")
    InvoicePersistence(fellowship_invoice).save_invoice_to_database()
