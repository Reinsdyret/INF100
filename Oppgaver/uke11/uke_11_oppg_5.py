"""Sheesh"""
from decimal import *

class NoPrice(Exception):
    """Exception for when there is no price for the product"""
    pass

class NotEnoughPaid(Exception):
    """Exception for when customer has not paid enough"""
    pass


def get_price(product,prices_filename:str) -> float:
    """Get price of product from price file, if there is no price an exception is raised"""
    price = False
    with open(prices_filename, "r") as prices:
        for line in prices:
            name, price_in_file = line.strip().split(";")
            if name == product:
                price = price_in_file
    if price == False:
        raise NoPrice
    return Decimal(str(price))


def get_amount(toDo,product,cash_register_filename:str) -> int:
    """Get amount of product in cash register history"""
    amount = 0
    with open(cash_register_filename, "r") as cash_register:
        for line in cash_register:
            action, name = line.strip().split(";")
            if name == product and toDo == action:
                amount += 1
    return amount


def receipt_content(prices_filename, cash_register_filename):
    """Construct contents of a receipt of the cash register events,
    given the store prices."""

    # list_of_tuples.sort(key=lambda x:x[1]) for å sortere en liste med tupler etter andre verdi
    list_of_purchase_and_return = []
    products = []
    list_of_returned = []
    returned_products = []
    total_price = Decimal('0')
    paid = Decimal('0')
    with open(cash_register_filename, "r") as cash_registrer:
        with open(prices_filename, "r") as prices:
            for line in cash_registrer:
                action, value = line.strip().split(";")
                if action == "pay":
                    paid += Decimal(str(value))
                elif action == "buy":
                    if value in products:
                        continue
                    products.append(value)
                    # Find how many products are being bought
                    amount = get_amount(action,value,cash_register_filename)
                    # Find the cost of the product if exists
                    cost = get_price(value,prices_filename) * Decimal(str(amount))
                    # Add the total cost to the total price
                    total_price += cost

                    list_of_purchase_and_return.append(tuple((amount,value,cost)))
                elif action == "return":
                    if value in returned_products:
                        continue
                    returned_products.append(value)
                    # Find how many products are being returned
                    amount = get_amount(action,value,cash_register_filename)
                    #Define cost
                    cost = get_price(value,prices_filename) * Decimal(str(amount)) * -1
                    # Add the total cost to the total price
                    total_price += cost

                    list_of_returned.append(tuple((amount * -1,value,cost)))
    list_of_purchase_and_return.sort(key=lambda x:x[1])
    list_of_returned.sort(key=lambda x:x[1])
    for tuple_returned in list_of_returned:
        list_of_purchase_and_return.append(tuple_returned)
    
    total_mva = total_price * Decimal('0.2')
    paid_back = total_price - paid
    
    # Raise error if not enough is paid
    if paid_back > 0:
        raise NotEnoughPaid
    return tuple((list_of_purchase_and_return,total_price,total_mva,paid,paid_back))
    

def receipt(prices_filename, cash_register_filename):
    """Construct a receipt of the cash register events,
    given the store prices."""

    # get receipt content from receipt_content()
    purcases_returns, total, vat, payment, change = receipt_content(
        prices_filename, cash_register_filename
    )

    # the formatted lines of the receipt
    receipt_lines = [f"{'Nr.':>4}  {'Item':18}  {'Price':>10}"]

    for nr, item, price in purcases_returns:
        receipt_lines.append(f"{nr:4d}  {item:18}  {price:10.2f}")

    receipt_lines.append(f"Total: {total}")
    receipt_lines.append(f"Of which VAT: {vat:.2f}")
    receipt_lines.append(f"Payment: {payment}")
    receipt_lines.append(f"Change {change}")

    # add some dividers
    max_len = max(len(line) for line in receipt_lines)
    divider = "-" * max_len
    receipt_lines.insert(1, divider)
    receipt_lines.insert(-4, divider)
    receipt_lines.insert(-2, divider)

    return "\n".join(receipt_lines)

#print(receipt("prices.txt","cash_register.txt"))