"""
>>> print(os.popen('echo 0 0| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
The largest isosceles triangle has a size of 0
>>> print(os.popen('echo 0 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 0
    0 1 0 0 1 0 1 0 0 1
    1 0 1 1 1 0 1 1 1 0
    0 0 1 0 1 1 0 1 0 0
    0 0 0 1 0 0 1 1 0 1
    1 0 1 0 1 1 0 1 1 0
    1 0 0 0 0 1 1 0 0 0
    0 0 0 1 1 0 0 1 1 1
    1 1 0 1 0 1 1 0 0 0
    1 0 0 1 0 1 1 0 0 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 0 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 0 1 0 1 0 0 1 1 1
    1 1 0 1 0 1 0 1 1 1
    1 0 1 1 1 1 1 0 1 1
    1 1 1 0 1 0 0 1 1 1
    1 1 0 1 1 1 0 1 1 1
    0 0 1 0 0 0 1 1 0 0
    1 1 1 0 1 1 1 1 0 1
    1 1 0 1 1 1 1 1 0 1
    1 1 1 0 1 0 0 0 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 0 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 0 0 1
    1 0 1 1 1 1 1 1 1 0
    0 0 1 0 1 1 1 1 0 1
    1 1 1 1 0 0 1 1 0 1
    1 0 1 1 1 1 0 1 1 1
    1 1 1 1 0 1 1 0 0 1
    1 0 0 1 1 1 1 1 1 1
    1 1 0 1 0 1 1 1 1 0
    1 0 1 1 1 1 1 0 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 0 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 0 0 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 0
    1 0 0 1 0 1 1 1 1 1
    0 1 1 1 1 1 1 1 0 0
    1 1 1 0 1 1 1 0 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 0 1 1
    1 0 0 1 1 0 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 0 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 0 1 0 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 0 1 0 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 0 0
    1 1 1 0 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 0 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 0 1 0 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 0 0 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 0 0 1 1
    1 0 1 1 1 1 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 350285 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 0 1
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 416452 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 1 0 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 0 0 0 1 0 0 1 1 1
    0 0 1 0 1 1 0 0 0 0
    0 1 0 0 1 0 0 0 1 1
    1 1 0 1 0 1 0 1 1 0
    1 1 1 0 0 1 0 1 0 0
    1 0 1 1 1 1 1 0 1 1
    0 1 1 1 0 1 1 1 1 1
    1 0 0 1 0 1 1 0 1 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 339771 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 0 1 0 1 0 1 1
    1 0 1 1 1 0 0 0 1 0
    1 0 0 0 0 0 0 1 1 1
    1 1 1 0 1 1 1 1 1 1
    0 1 0 0 0 1 0 1 1 1
    0 0 1 0 0 1 0 0 1 1
    1 1 0 0 0 1 1 1 1 0
    1 1 1 1 0 1 1 0 0 1
    1 0 0 1 1 0 1 1 1 1
    0 1 1 0 0 0 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 375688 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 0 1 1 1
    0 0 1 1 0 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 0 1 1 1 1 1
    0 1 1 1 1 0 1 0 1 0
    0 1 1 1 1 1 1 0 1 1
    1 0 0 1 1 0 1 1 1 0
    1 0 1 1 0 0 1 1 1 1
    1 1 0 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 407155 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 0 0 1 0 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 0 0 1 1 1 1 0 1
    1 1 1 0 1 1 0 1 1 0
    1 1 1 1 1 1 1 0 0 1
    1 0 0 1 1 1 1 0 1 1
    0 0 1 1 1 1 1 0 1 1
    0 1 1 1 1 1 0 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 390239 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 0 0
    1 1 1 1 1 1 1 0 1 0
    1 1 1 1 0 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 0 0 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 0 1 1 1 1
    1 1 1 0 1 0 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 335676 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 0 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 0 1 1 0 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 0
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 0 1 1 1 0 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 368460 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 0
    0 1 1 0 1 1 1 0 1 1
    1 1 0 0 1 1 0 1 1 1
    1 1 1 1 0 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 0 1 1 1 1 0 0 1 0
    0 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 377926 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 0 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 352209 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 0 1 1 0 1 1
    1 0 0 1 0 0 0 1 1 0
    1 0 1 1 1 1 0 0 0 1
    1 1 0 0 1 0 1 0 0 1
    1 0 0 0 0 1 1 0 1 0
    1 0 1 0 1 1 0 1 0 1
    1 0 0 0 1 0 0 0 1 1
    0 1 0 1 0 0 1 0 0 0
    0 0 1 1 0 0 1 1 0 1
    0 1 0 0 0 1 0 0 1 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 322833 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 0 1 0 1 0 1 1
    0 0 1 1 1 1 1 0 1 0
    1 0 1 1 1 0 1 1 0 1
    0 1 0 1 1 1 1 0 0 0
    1 1 1 1 1 0 1 1 1 1
    1 1 0 1 1 0 0 1 1 0
    1 1 0 1 0 1 1 0 0 1
    1 0 0 0 0 0 1 0 1 1
    1 0 0 1 0 1 1 0 1 1
    0 1 1 1 1 1 0 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 344626 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 1 1 1 0 1 1
    1 1 0 1 1 1 1 1 1 0
    1 0 1 0 1 0 0 1 1 1
    0 0 0 1 0 1 1 1 0 1
    1 1 1 1 0 1 1 0 1 1
    1 0 1 1 1 1 1 1 0 1
    1 1 1 0 1 1 1 1 0 1
    1 0 1 0 1 0 1 1 0 0
    1 1 0 1 0 0 1 0 0 1
    1 0 0 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 0 100| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
"""
if __name__ == '__main__':
    import doctest
    import os
    print('Test Start......')
    doctest.testmod()
    print('Test Done! If not show "Test Failed", you pass my test')
