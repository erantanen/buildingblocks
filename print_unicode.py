"""
examples of unicode printing

listed are corners/horizontals/verticals and white space.

intermixed with ascii


"""

# describes?

u_corner_lu = '\u250c'
u_horizontal = '\u2500'

u_string = u_corner_lu + u_horizontal

print(u'\u250c\u2500\u2500\u2500\u2510')
print('12345')
print(u'\u2502\u205f\u205f\u205f\u2502')
print(u'\u2514\u2500\u2500\u2500\u2518')

print(u'\u250c\u2500\u2500\u2500\u2500\u2510')
print('123456')

print(u_string)
