""" O - the correct way 

Your boss asks to add a method to save the invoice to a database
along with a file.
"""
import typing as t
from abc import ABC, abstractmethod
from s_right import Book, Invoice


class InvoicePersistence(ABC):
    """Invoice Persistence Object"""

    @abstractmethod
    def save(self, invoice: Invoice, filename: t.Optional[str] = None) -> None:
        """Save the invoice"""


class FilePersistence(InvoicePersistence):
    """Save invoice to file"""

    def save(self, invoice: Invoice, filename: str = None) -> None:
        """Save invoice to file"""
        if filename is None:
            raise ValueError("Please insert value for filename")
        print(f"Saved invoice for '{invoice.book.name}' to {filename}")


class DatabasePersistence(InvoicePersistence):
    """Save invoice to database"""

    def save(self, invoice: Invoice, filename: str = None) -> None:
        """Save invoice to database"""
        print(f"Saved invoice for '{invoice.book.name}' to database")


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
    FilePersistence().save(fellowship_invoice, "Inv12345.txt")
    DatabasePersistence().save(fellowship_invoice)
