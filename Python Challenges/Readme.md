# New Knowledge I've learned

## Comma.py
I learned about **FORMATTING** while solve the problem about 'How to print number with commas as thousands separators?'

<group> allows you to include a grouping separator character in numeric output. For decimal and floating-point presentation types, <group> may be specified as either a comma character (,) or an underscore character (_). That character then separates each group of three digits in the output.

```Python
>>> '{0:,d}'.format(1234567)
'1,234,567'
>>> '{0:_d}'.format(1234567)
'1_234_567'

>>> '{0:,.2f}'.format(1234567.89)
'1,234,567.89'
>>> '{0:_.2f}'.format(1234567.89)
'1_234_567.89'
```

A <group> value using an underscore (_) may also be specified with the *binary, octal, and hexadecimal presentation types*. In that case, each group of four digits is separated by an underscore character in the output.

```Python
>>> '{0:_b}'.format(0b111010100001)
'1110_1010_0001'
>>> '{0:#_b}'.format(0b111010100001)
'0b1110_1010_0001'

>>> '{0:_x}'.format(0xae123fcc8ab2)
'ae12_3fcc_8ab2'
>>> '{0:#_x}'.format(0xae123fcc8ab2)
'0xae12_3fcc_8ab2'
```

* For more information: [Python Docs FORMATTING](https://realpython.com/python-formatted-output/#the-group-subcomponent, "link to formatting python docs")


*****

## DistanceofAlphabet.py
I learned **map()** while programming 'DistanceofAlphabet.py'.

Python’s map() is a built-in function that allows you to __process and transform all the items in an iterable without using an explicit for loop__, a technique commonly known as _mapping_. map() is useful when you need to apply a transformation function to each item in an iterable and transform them into a new iterable. map() is one of the tools that support a functional programming style in Python.

### Understanding map()
map() loops over the items of an input iterable (or iterables) and returns an iterator that results from applying a transformation function to every item in the original input iterable.

map() takes a function object and an iterable (or multiple iterables) as arguments and returns an iterator that yields transformed items on demand.

```Python
map(function, iterable[, iterable1, iterable2,..., iterableN])
```

- Function can be any Python function that takes a number of arguments equal to the number of iterables you pass to map().

This **first argument** to map() is a **transformation** function. In other words, it’s the function that transforms each original item into a new (transformed) item.


Suppose you need to take a list of numeric values and transform it into a list containing the square value of every number in the original list.

```Python
>>> def square(number):
...     return number ** 2
...

>>> numbers = [1, 2, 3, 4, 5]

>>> squared = map(square, numbers)

>>> list(squared)
[1, 4, 9, 16, 25]
```

- c.f. Lambda functions are quite useful when it comes to using map(). 

Examples Using map()
```Python
>>> string_it = ["processing", "strings", "with", "map"]
>>> list(map(str.capitalize, string_it))
['Processing', 'Strings', 'With', 'Map']

>>> list(map(str.upper, string_it))
['PROCESSING', 'STRINGS', 'WITH', 'MAP']

>>> list(map(str.lower, string_it))
['processing', 'strings', 'with', 'map']
```

```Python
>>> def powers(x):
...     return x ** 2, x ** 3
...

>>> numbers = [1, 2, 3, 4]

>>> list(map(powers, numbers))
[(1, 1), (4, 8), (9, 27), (16, 64)]

>>> # Convert to integer
>>> list(map(int, ["12", "3", "-15"]))
[12, 3, -15]
```

