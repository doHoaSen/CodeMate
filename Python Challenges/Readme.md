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