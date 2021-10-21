"""Do the same as in task 4 but if the stock does not have the book then it will be added with amount 10"""

def find_book(title:str,stock:dict):
    """Takes in a title and stock and returns how many of that book is in stock if there is or false if there are none"""
    if title not in stock:
        return False
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
    if find_book(book_title,in_storage):
        print(find_book(book_title,in_storage))
    else:
        print(f'Vi har 10 av "{book_title}"')
        in_storage.update({book_title : 10})

    book_title = input("\nTittel: ")

print("Ha det!")
