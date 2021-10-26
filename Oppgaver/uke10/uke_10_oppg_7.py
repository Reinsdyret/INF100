"""Make your own version of get() called my_get(d,k,v).
Takes three arguments: dictonary, key, default value:
then if the key is in the dictonary my_get(d,k,v) returns it value
else: it returns the defaul value"""

def my_get(d:dict,k,v):
    """Own version of the get() function but with a default value v"""
    try:
        return d[k]
    except KeyError:
        return v
