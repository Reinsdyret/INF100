"""Sheesh"""
import decimal

class NoPrice(Exception):
    """Exception for when there is no price for the product"""
    pass

class NotEnoughPaid(Exception):
    """Exception for when customer has not paid enough"""
    pass


def receipt_content(prices_filename, cash_register_filename):
    """Construct contents of a receipt of the cash register events,
    given the store prices."""

    list_of_purchase_and_return = []
    products = []
    list_of_returned = []
    returned_products = []
    total_price = 0
    paid = 0
    with open(cash_register_filename, "r") as cash_registrer:
        with open(prices_filename, "r") as prices:
            for line in cash_registrer:
                action, value = line.strip().split(";")
                if action == "pay":
                    paid += float(value)
                elif action == "buy":
                    if value in products:
                        continue
                    products.append(value)
                    # Find how many products are being bought
                    count_product = 0
                    for new_line in cash_registrer:
                        el1,el2 = new_line.strip().split(";")
                        if el1 == "buy" and el2 == value:
                            count_product += 1
                    # Find the cost of the product if exists
                    cost = False
                    for prices_line in prices:
                        product, price = prices_line.split(";")
                        if product == value:
                            print(float(price) * count_product)
                            cost = float(price) * count_product
                    
                    # Raise error if the product is not in prices file
                    if cost == False:
                        raise NoPrice

                    # Add the total cost to the total price
                    total_price += cost

                    list_of_purchase_and_return.append(tuple((count_product,value,cost)))
                elif action == "return":
                    if value in returned_products:
                        continue
                    returned_products.append(value)
                    # Find how many products are being returned
                    count_product = 0
                    for new_line in cash_registrer:
                        el1,el2 = new_line.split(";")
                        if el1 == "return" and el2 == value:
                            count_product -= 1
                    # Find the cost of the product if exists
                    cost = False
                    for prices_line in prices:
                        product, price = prices_line.split(";")
                        if product == value:
                            cost = float(price) * count_product
                    
                    # Raise error if the product is not in prices file
                    if not cost:
                        raise NoPrice
                    
                    # Add the total cost to the total price
                    total_price += cost

                    list_of_returned.append(tuple((count_product,value,cost)))
                    returned += count_product
    for tuple_returned in list_of_returned:
        list_of_purchase_and_return.append(tuple_returned)
    
    total_mva = total_price * 0.2
    paid_back = total_price - paid
    
    # Raise error if not enough is paid
    if paid_back < 0:
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

print(receipt("prices.txt","cash_register.txt"))
