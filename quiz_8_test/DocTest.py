"""
>>> from quiz_8 import *
>>> a = Polynomial()
>>> print(a)
0
>>> a = Polynomial('2')
>>> print(a)
2
>>> a = Polynomial('0')
>>> print(a)
0
>>> a = Polynomial('x')
>>> print(a)
x
>>> a = Polynomial('2x')
>>> print(a)
2x
>>> a = Polynomial('x^2')
>>> print(a)
x^2
>>> a = Polynomial('2x^2')
>>> print(a)
2x^2
>>> a = Polynomial('x + 1')
>>> print(a)
x + 1
>>> a = Polynomial('2x + 1')
>>> print(a)
2x + 1
>>> a = Polynomial('x^2 + 1')
>>> print(a)
x^2 + 1
>>> a = Polynomial('2x^2 + 1')
>>> print(a)
2x^2 + 1
>>> a = Polynomial('x^3 + x + 1')
>>> print(a)
x^3 + x + 1
>>> a = Polynomial('x^3 + 2x + 1')
>>> print(a)
x^3 + 2x + 1
>>> a = Polynomial('x^3 + x^2 + 1')
>>> print(a)
x^3 + x^2 + 1
>>> a = Polynomial('x^3 + 2x^2 + 1')
>>> print(a)
x^3 + 2x^2 + 1
>>> a = Polynomial('2x^3 + x + 1')
>>> print(a)
2x^3 + x + 1
>>> a = Polynomial('2x^3 + 2x + 1')
>>> print(a)
2x^3 + 2x + 1
>>> a = Polynomial('2x^3 + x^2 + 1')
>>> print(a)
2x^3 + x^2 + 1
>>> a = Polynomial('2x^3 + 2x^2 + 1')
>>> print(a)
2x^3 + 2x^2 + 1
>>> a = Polynomial('x^3 - x + 1')
>>> print(a)
x^3 - x + 1
>>> a = Polynomial('x^3 - 2x + 1')
>>> print(a)
x^3 - 2x + 1
>>> a = Polynomial('x^3 - x^2 + 1')
>>> print(a)
x^3 - x^2 + 1
>>> a = Polynomial('x^3 - 2x^2 + 1')
>>> print(a)
x^3 - 2x^2 + 1
>>> a = Polynomial('2x^3 - x + 1')
>>> print(a)
2x^3 - x + 1
>>> a = Polynomial('2x^3 - 2x + 1')
>>> print(a)
2x^3 - 2x + 1
>>> a = Polynomial('2x^3 - x^2 + 1')
>>> print(a)
2x^3 - x^2 + 1
>>> a = Polynomial('2x^3 - 2x^2 + 1')
>>> print(a)
2x^3 - 2x^2 + 1
>>> a = Polynomial('x^3 + x')
>>> print(a)
x^3 + x
>>> a = Polynomial('x^3 + 2x')
>>> print(a)
x^3 + 2x
>>> a = Polynomial('x^3 + x^2')
>>> print(a)
x^3 + x^2
>>> a = Polynomial('x^3 + 2x^2')
>>> print(a)
x^3 + 2x^2
>>> a = Polynomial('2x^3 + x')
>>> print(a)
2x^3 + x
>>> a = Polynomial('2x^3 + 2x')
>>> print(a)
2x^3 + 2x
>>> a = Polynomial('2x^3 + x^2')
>>> print(a)
2x^3 + x^2
>>> a = Polynomial('2x^3 + 2x^2')
>>> print(a)
2x^3 + 2x^2
>>> a = Polynomial('-x')
>>> print(a)
-x
>>> a = Polynomial('-2x')
>>> print(a)
-2x
>>> a = Polynomial('-x^2')
>>> print(a)
-x^2
>>> a = Polynomial('-2x^2')
>>> print(a)
-2x^2
>>> a = Polynomial('-x - 1')
>>> print(a)
-x - 1
>>> a = Polynomial('-2x - 1')
>>> print(a)
-2x - 1
>>> a = Polynomial('-x^2 - 1')
>>> print(a)
-x^2 - 1
>>> a = Polynomial('-2x^2 - 1')
>>> print(a)
-2x^2 - 1
>>> a = Polynomial('-x^3 - x - 1')
>>> print(a)
-x^3 - x - 1
>>> a = Polynomial('-x^3 - 2x - 1')
>>> print(a)
-x^3 - 2x - 1
>>> a = Polynomial('-x^3 - x^2 - 1')
>>> print(a)
-x^3 - x^2 - 1
>>> a = Polynomial('-x^3 - 2x^2 - 1')
>>> print(a)
-x^3 - 2x^2 - 1
>>> a = Polynomial('-2x^3 - x - 1')
>>> print(a)
-2x^3 - x - 1
>>> a = Polynomial('-2x^3 - 2x - 1')
>>> print(a)
-2x^3 - 2x - 1
>>> a = Polynomial('-2x^3 - x^2 - 1')
>>> print(a)
-2x^3 - x^2 - 1
>>> a = Polynomial('-2x^3 - 2x^2 - 1')
>>> print(a)
-2x^3 - 2x^2 - 1
>>> a = Polynomial('-x^3 + x - 1')
>>> print(a)
-x^3 + x - 1
>>> a = Polynomial('-x^3 + 2x - 1')
>>> print(a)
-x^3 + 2x - 1
>>> a = Polynomial('-x^3 + x^2 - 1')
>>> print(a)
-x^3 + x^2 - 1
>>> a = Polynomial('-x^3 + 2x^2 - 1')
>>> print(a)
-x^3 + 2x^2 - 1
>>> a = Polynomial('-2x^3 + x - 1')
>>> print(a)
-2x^3 + x - 1
>>> a = Polynomial('-2x^3 + 2x - 1')
>>> print(a)
-2x^3 + 2x - 1
>>> a = Polynomial('-2x^3 + x^2 - 1')
>>> print(a)
-2x^3 + x^2 - 1
>>> a = Polynomial('-2x^3 + 2x^2 - 1')
>>> print(a)
-2x^3 + 2x^2 - 1
>>> a = Polynomial('-x^3 - x')
>>> print(a)
-x^3 - x
>>> a = Polynomial('-x^3 - 2x')
>>> print(a)
-x^3 - 2x
>>> a = Polynomial('-x^3 - x^2')
>>> print(a)
-x^3 - x^2
>>> a = Polynomial('-x^3 - 2x^2')
>>> print(a)
-x^3 - 2x^2
>>> a = Polynomial('-2x^3 - x')
>>> print(a)
-2x^3 - x
>>> a = Polynomial('-2x^3 - 2x')
>>> print(a)
-2x^3 - 2x
>>> a = Polynomial('-2x^3 - x^2')
>>> print(a)
-2x^3 - x^2
>>> a = Polynomial('-2x^3 - 2x^2')
>>> print(a)
-2x^3 - 2x^2
>>> p = Polynomial()
>>> print(p + Polynomial('2'))
2
>>> print(p)
0
>>> p += Polynomial('2')
>>> print(p)
2
>>> p = Polynomial('3')
>>> print(p + Polynomial('-3'))
0
>>> print(p)
3
>>> p += Polynomial('-3')
>>> print(p)
0
>>> p = Polynomial('x')
>>> print(p + Polynomial('2x^3 + x - 4'))
2x^3 + 2x - 4
>>> print(p)
x
>>> p += Polynomial('2x^3 + x - 4')
>>> print(p)
2x^3 + 2x - 4
>>> p = Polynomial('4x^5 - x^2 + 6')
>>> print(p)
4x^5 - x^2 + 6
>>> print(p * Polynomial('x^3 - x + 4'))
4x^8 - 4x^6 + 15x^5 + 7x^3 - 4x^2 - 6x + 24
>>> print(p)
4x^5 - x^2 + 6
>>> p *= Polynomial('x^3 - x + 4')
>>> print(p)
4x^8 - 4x^6 + 15x^5 + 7x^3 - 4x^2 - 6x + 24
>>> p = Polynomial('x^4 - x^3 + x^2 - x')
>>> print(p * Polynomial('-2x^3 + 3x^2 - 4x + 5'))
-2x^7 + 5x^6 - 9x^5 + 14x^4 - 12x^3 + 9x^2 - 5x
>>> p *= Polynomial('-2x^3 + 3x^2 - 4x + 5')
>>> print(p)
-2x^7 + 5x^6 - 9x^5 + 14x^4 - 12x^3 + 9x^2 - 5x
>>> print(Polynomial('x + 5')+Polynomial('-5'))
x
>>> print(Polynomial('x^2 + 5')+Polynomial('-x^2'))
5
>>> print(Polynomial('x^2 + 5')+Polynomial('-x^2 - 5'))
0
>>> print(Polynomial('x^2 + x + 5')+Polynomial('x^2 - x + 5'))
2x^2 + 10
>>> print(Polynomial('x^2 + x + 5')+Polynomial('-x^2 + x - 5'))
2x
>>> print(Polynomial('-x^2 + x - 5')+Polynomial('x^2 - x + 5'))
0
>>> print(Polynomial('-x^2 + x + 5')+Polynomial('x^2 + x + 5'))
2x + 10
"""
if __name__ == '__main__':
    import doctest
    print('Test Start......')
    doctest.testmod()
    print('Test Done! If not show "Test Failed", you pass my test')
