xs = {

'a' : 5,

'5' : 'hello',

7 : 3.1415,

5 : 7

}

print(xs['5'] == 'hello')
print('5' in xs.keys())
print(xs[5] + xs['a'] == 12)
print(len(xs['5']) == xs['a'])
