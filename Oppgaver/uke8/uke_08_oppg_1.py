"""Make a function that takes in two integers, payment and price, and returns the change. 
The change consists of coins valued at 1,5,10 and 20 
and of course you would like the higher coins rather than alot of small valued coins"""

def return_change(payment, price :int) -> list:
    """Takes in two integers, payment and price, and returns the change."""
    changeSum = payment - price
    changeList = []
    coins = [20,10,5,1]
    for coin in coins:
        for  i in range(0,changeSum//coin):
            changeList.append(coin)
            changeSum -= coin

    return changeList
