from re import A


def mygenerator():
 yield 1
 yield 2
 yield 3

g = mygenerator()

# for i in g:
#  print(i)
value = next(g)
print(value)
value = next(g)
print(value)


# fibanocci

def fibanocci(limit):
 a, b = 0, 1

 while a < limit:
  yield a
  a, b = b, a + b

fib = fibanocci(40)
for i in fib:
 print(i)

 mygen = (i for i in range(10) if i % 2 ==0)
 print(list(mygen))