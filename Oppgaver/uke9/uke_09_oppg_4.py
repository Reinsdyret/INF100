"""Write a program that takes in constant input for a book name
and returns the current amount of that book in the stock, using the get function.
The stock is a dictonary and if the book cannot be found:
'Vi har :math:`0` av [book_tittel]' should be printed
If the book is in stock:
'Vi har amount av "title"' should be printed
The program will exit if the input is empty"""

def find_book(title:str,stock:dict) -> str:
    """Takes in a title and stock and returns how many of that title is in stock"""
    if title not in stock:
        return f'Vi har 0 av "{title}"'
    return f'Vi har {stock.get(title)} av "{title}"'

book_title = input("Tittel: ")
in_storage = {
    "Ancillary Justice": 1_046, # vi kan bruke _ i tall, den blir ignorert
    "The Use of Weapons": 372,
    "1984": 5_332,
    "The Three-Body Problem": 523,
    "A Fisherman of the Inland Sea": 728,
}

while book_title != "":
    print(find_book(book_title,in_storage))
    book_title = input("\nTittel: ")

print("Ha det!")
