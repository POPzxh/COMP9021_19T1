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
>>> print(os.popen('echo 357159 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 0 1 1
    1 1 1 1 1 0 1 0 1 1
    1 1 1 1 1 1 0 1 1 0
    1 0 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 344460 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 0 0 0 1 1 1 0 1
    1 0 1 1 0 1 1 1 1 1
    0 0 0 1 1 1 0 1 1 0
    0 1 0 0 0 0 1 1 1 1
    1 1 0 0 0 0 1 0 1 1
    0 0 0 0 0 1 1 1 0 0
    0 0 1 1 1 0 1 1 0 0
    1 0 1 1 0 1 0 1 0 0
    0 0 0 1 0 1 0 0 1 1
    1 1 0 1 1 0 0 1 1 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 327495 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 0 1 1 0 1 1
    1 0 1 1 1 1 1 0 0 1
    0 1 1 1 1 1 0 1 1 1
    0 1 1 1 0 1 0 1 1 1
    0 0 1 0 0 1 0 1 0 1
    1 1 1 0 1 1 1 1 0 0
    1 1 1 0 0 0 1 0 0 0
    0 1 0 1 0 1 0 1 0 1
    1 1 1 0 1 1 1 0 1 0
    0 1 1 1 1 1 0 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 364046 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 0 1 1 1 1 1
    1 0 1 0 1 1 0 1 1 1
    0 1 1 0 0 1 1 1 1 1
    1 0 0 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    0 1 1 0 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 0 0 0 1 1 1 1 1
    1 0 1 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 404252 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 0 1 1
    0 1 1 0 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 0 1 1
    1 1 0 1 1 1 0 1 1 1
    1 1 0 0 1 1 1 1 1 1
    1 1 1 0 1 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 0 1 0 1 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 332130 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 0 1 1 1 1
    1 1 1 1 1 0 0 1 1 1
    0 1 0 0 1 0 1 1 1 0
    0 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 0 0 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 0 1
    1 1 0 1 1 1 1 1 0 1
    0 1 1 0 1 1 1 0 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 354351 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 0 0 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 0 1
    0 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 0 1
    1 0 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 347549 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 0 0 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 0
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 325236 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 1 1 1
    0 0 1 1 1 1 1 1 1 1
    1 0 1 1 0 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 0 1 1 1
    0 0 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 0
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 419075 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 1 0 0 0 0 0 0
    1 0 0 0 1 1 1 1 0 1
    0 1 0 1 0 1 1 1 1 0
    0 1 1 1 0 1 0 0 1 0
    0 0 0 0 1 1 1 1 1 0
    0 1 0 1 0 0 0 1 0 0
    1 0 0 1 0 1 1 1 1 1
    1 0 0 1 0 0 0 1 0 0
    1 1 0 1 0 0 1 1 0 0
    0 1 1 1 1 0 1 0 1 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 405760 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 0 1 0 0 1 0 1
    0 1 1 0 1 0 0 1 1 1
    0 1 0 0 1 1 0 0 1 1
    0 1 1 0 0 1 1 1 0 1
    0 1 0 1 1 1 0 1 1 1
    1 1 0 1 0 1 0 0 1 0
    0 1 1 0 1 1 1 0 1 1
    1 0 1 0 1 1 1 0 0 1
    1 1 0 0 1 1 1 1 0 0
    1 0 0 0 1 1 1 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 360798 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 1 1 1
    0 1 1 0 1 0 1 1 0 1
    1 1 1 0 1 1 1 1 1 1
    1 1 0 0 0 0 1 1 1 1
    0 0 1 0 0 1 1 1 0 1
    1 1 1 0 1 0 1 1 1 1
    1 0 1 1 1 1 1 0 1 0
    1 1 1 0 0 0 1 1 0 1
    1 1 1 1 0 1 1 0 1 1
    1 1 0 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 388331 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 0 1 1 1
    1 1 1 1 1 1 0 1 0 1
    1 1 1 1 1 1 1 0 1 1
    0 0 0 1 1 1 1 0 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 0 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 0 0 1 0 1 0 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 352703 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 1 1 1 1 0 1 1
    1 0 1 0 1 1 1 1 0 1
    1 1 1 1 0 1 1 1 1 1
    0 1 1 1 1 0 1 0 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 0 0
    0 1 1 1 1 1 1 0 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    0 1 1 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 328423 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 0 1
    0 1 1 1 1 1 1 1 0 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 359848 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 1 1
    1 0 1 1 0 1 1 1 1 1
    1 0 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 0 0 1
    1 1 1 0 0 1 1 1 1 1
    1 0 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 0 0 1 1
    0 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 375250 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 0 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 325193 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 0 0 1 1
    1 0 1 0 1 0 1 0 0 1
    0 1 0 0 1 1 1 1 0 0
    1 0 0 0 1 1 1 1 1 1
    1 1 0 0 1 0 1 1 0 0
    0 1 1 1 1 0 1 0 0 0
    1 0 0 0 0 1 0 1 1 0
    0 0 1 0 0 1 0 0 1 1
    1 0 1 0 0 1 0 1 1 1
    0 0 0 1 0 1 0 0 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 403329 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 1 1 0 0 1 0 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 0 1 1 0 1
    0 1 1 1 0 0 0 0 1 1
    0 0 1 0 1 1 1 0 1 0
    0 1 0 1 1 1 1 0 1 1
    1 1 1 0 0 0 1 0 1 0
    0 0 1 1 0 0 1 0 1 0
    1 0 1 0 1 0 1 0 1 0
    1 1 1 0 0 1 0 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 376605 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 0 1 0 1 1
    1 1 0 0 1 1 1 1 0 1
    0 1 1 1 0 0 1 0 1 0
    0 1 1 1 1 1 0 0 1 1
    0 1 1 1 1 0 1 1 1 1
    0 1 1 1 1 1 0 1 0 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 0 0 1 1 1 1
    0 1 1 1 1 1 1 0 0 1
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 367813 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 0 0 1 0 1 1
    1 1 0 0 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 0 1 1 1 1 1 1
    0 0 1 1 1 0 1 1 1 0
    1 1 0 1 1 1 1 1 0 0
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 0 1 1 1 0 1
    1 1 1 0 1 0 1 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 391931 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 0
    1 1 1 0 1 1 1 0 1 1
    1 1 0 1 1 0 1 1 1 1
    0 1 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 338082 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 0 1 0 1 1 1 1 1
    1 1 1 0 1 1 1 0 1 1
    1 0 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    0 1 1 1 0 1 0 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 332942 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 0 1 1 1 1 1
    1 0 1 1 1 0 1 1 0 1
    1 1 1 1 0 1 1 1 1 1
    0 1 1 1 1 1 1 1 0 0
    1 1 1 1 1 1 0 1 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 332827 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 0 1
    1 0 1 1 1 1 0 1 1 1
    1 0 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 356954 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 0 1 0
    0 0 1 0 0 1 0 0 1 1
    1 1 0 1 1 1 1 0 1 0
    1 0 0 1 0 0 0 1 0 1
    1 0 1 0 0 1 1 1 1 0
    1 1 0 0 1 0 1 0 1 0
    0 1 0 1 1 1 0 0 0 1
    0 0 0 1 1 0 1 0 0 1
    1 0 0 1 0 1 1 1 1 1
    1 1 0 0 0 0 1 1 1 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 397192 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 0 1
    1 0 0 1 1 1 0 0 1 0
    1 1 0 0 1 0 1 1 1 1
    1 1 0 1 0 1 0 1 1 0
    1 1 0 1 0 1 0 1 1 0
    1 0 0 1 1 0 0 1 1 1
    1 1 1 1 1 1 1 1 0 1
    0 1 1 0 0 0 1 0 1 1
    1 1 1 1 1 0 0 0 1 1
    1 0 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 419240 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 0 1 1 1 1 1 1
    1 1 0 1 1 0 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 0 1
    1 1 0 1 1 1 0 1 1 1
    1 0 1 0 0 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 0 1 1 0 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 347368 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 0 1 0 1 1
    0 1 0 1 1 1 0 0 1 1
    1 1 1 0 0 0 1 1 1 1
    1 1 0 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 0 1 0 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 0 1 0 1
    1 1 1 1 0 1 0 1 1 1
    1 1 1 1 1 1 1 1 0 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 380594 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 0 0 1 1 0 1
    1 1 1 0 1 1 1 0 1 1
    1 1 1 0 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 371077 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 0 1
    1 1 1 0 1 1 1 0 1 1
    1 1 1 1 0 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 0 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 0 1 0 1 1 1 0
    0 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 362937 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    0 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 393297 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 0 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 403999 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 1 1 0 1 1 0 1 1
    1 0 1 0 0 1 1 0 0 0
    1 0 1 0 0 0 0 1 1 1
    1 1 0 1 1 0 1 0 1 0
    1 1 0 1 0 1 1 1 1 0
    1 1 1 1 0 0 1 0 0 1
    1 1 0 1 1 1 0 1 0 1
    0 0 0 0 1 0 1 1 0 1
    0 0 0 1 1 1 0 0 1 0
    1 1 0 0 1 0 1 0 0 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 384871 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 0 1 0 1 0
    1 0 1 1 0 1 1 1 1 1
    1 0 1 1 0 1 1 0 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 0 0 1 0 0 1 0 1
    0 1 0 1 1 0 1 1 0 0
    0 1 1 1 1 1 1 0 0 1
    1 1 1 0 0 1 0 0 0 0
    0 1 0 1 0 0 1 0 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 379165 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 0
    1 0 1 1 0 1 0 0 0 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 0 1 1 1 0 1
    1 1 0 1 0 1 1 1 1 1
    1 1 1 1 0 1 0 1 1 0
    0 1 1 1 0 1 1 0 0 1
    1 0 1 1 0 1 1 1 1 0
    1 1 1 0 0 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 395380 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 1 1
    1 0 0 0 1 1 1 0 1 1
    1 1 1 0 0 1 1 1 1 1
    0 0 1 1 1 0 1 0 1 1
    1 1 1 1 1 1 1 0 0 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 0 1 1 0 1 1 1
    1 1 0 0 1 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 321559 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 1 0 0 0
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 0 1 1 1 0
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 0 1 1 0 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 0 1 1 1 1 0 1 1
    1 1 1 1 0 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 354256 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 1 1 1
    0 1 1 1 1 0 0 1 1 0
    1 0 1 1 0 1 1 0 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 0 1 0 1
    0 1 1 0 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 407584 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 0 0 0
    0 0 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 0 1 1
    1 1 0 1 1 1 0 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 392038 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 0
    1 1 1 1 1 0 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    0 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 355917 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 0 1 0 1 0 1 0
    1 0 0 1 0 0 1 0 0 0
    0 1 0 0 0 0 0 1 1 1
    1 0 1 1 0 0 0 0 0 0
    1 0 1 1 0 1 0 0 1 1
    0 1 0 1 0 1 1 0 1 1
    1 1 1 0 1 0 1 1 0 0
    1 1 1 1 1 0 1 0 1 1
    0 0 0 0 0 1 1 0 1 1
    1 0 1 0 1 1 0 1 1 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 332341 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 1 1 1 0 0
    1 0 1 0 1 1 0 1 1 0
    0 0 0 1 1 1 1 1 0 0
    1 0 1 0 1 0 0 1 0 1
    1 1 1 1 0 1 0 1 1 0
    1 0 0 0 1 1 0 1 1 1
    1 1 1 0 0 0 0 1 0 1
    1 1 1 0 1 1 1 1 0 1
    0 0 1 1 1 1 0 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 359215 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 0 1
    0 1 1 1 1 1 1 1 0 1
    0 1 0 1 1 1 1 1 0 0
    1 1 1 1 1 0 1 1 1 1
    1 0 1 1 1 1 0 1 1 0
    1 1 1 1 0 0 1 1 1 1
    1 1 1 0 1 1 1 0 0 1
    1 1 1 1 1 1 0 1 1 1
    1 0 1 0 1 1 1 1 1 1
    1 1 1 1 0 1 1 0 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 327430 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 0 0 1 1 1
    1 1 0 1 1 0 0 1 0 1
    1 1 1 0 1 0 1 0 1 0
    0 1 0 0 1 1 1 1 1 1
    0 1 0 1 1 0 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 342109 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 0
    1 1 1 1 1 1 0 0 0 1
    1 1 1 1 1 0 0 1 0 1
    1 1 1 0 1 0 1 1 1 1
    1 1 1 1 1 0 0 0 0 1
    1 1 1 1 0 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 335509 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 0 1 1
    1 1 1 0 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 0
    1 1 0 1 1 0 1 0 1 1
    1 1 1 0 1 1 1 1 0 0
    1 1 1 0 0 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 0 0 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 397909 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 1 1 1 1 1 1 1
    0 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 398777 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 1 1
    0 1 1 0 1 1 1 1 0 0
    1 1 0 1 0 1 0 1 0 1
    0 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 0 1 0
    1 1 0 1 0 0 1 1 1 1
    1 0 1 1 1 1 1 0 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 407316 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 0 0 0 1 1
    0 0 0 0 1 0 0 1 1 0
    0 0 1 0 0 0 1 1 1 0
    1 1 1 1 0 1 0 1 0 1
    1 1 0 0 0 1 0 1 0 1
    0 0 0 0 0 0 1 0 1 0
    1 0 0 1 1 0 1 1 0 1
    0 1 1 0 0 1 0 1 0 0
    0 1 0 1 1 0 1 1 1 0
    0 1 0 1 1 0 0 0 0 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 386879 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 0 0 0 1 0 1 1 1
    0 1 1 1 1 0 1 1 1 1
    1 1 0 1 1 1 1 0 0 0
    0 1 1 0 0 0 1 0 0 1
    1 1 0 1 0 0 0 1 1 1
    1 1 1 1 1 1 0 1 0 1
    1 1 1 1 1 1 1 1 0 0
    0 1 1 0 1 0 1 0 1 0
    1 0 1 0 1 1 1 1 1 1
    0 0 0 1 1 1 1 0 0 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 327074 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 0
    1 1 1 1 0 1 0 1 1 1
    1 1 1 1 0 1 0 1 1 1
    1 1 1 1 0 1 1 0 0 1
    1 1 0 1 1 0 1 1 1 1
    1 0 1 0 0 1 1 0 0 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 381267 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    0 0 1 1 1 1 0 1 1 0
    1 1 1 1 1 1 1 1 1 0
    0 0 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 0 1 1 1 1 1 1
    0 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 0 1 0
    1 0 0 0 1 0 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 357317 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 0 1 0 0 1 1 1
    1 0 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 0 0 1
    1 1 1 1 1 1 1 0 1 1
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 0 1 1 0
    1 1 1 1 0 0 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    0 1 0 0 0 1 1 1 0 1
    1 0 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 397767 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 0 1 1 1 1
    0 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 0
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 376095 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 0 1
    0 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 0 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 387166 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 0 1 0
    1 1 1 1 0 1 1 1 1 0
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    0 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 0 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 367735 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 1 0 0 1 1 1
    1 0 0 0 1 1 0 1 1 0
    0 0 0 1 0 1 1 0 0 1
    1 1 1 0 0 1 0 1 1 0
    1 1 0 1 0 1 0 0 1 0
    1 1 0 1 0 0 0 0 0 0
    0 1 0 1 1 0 0 0 1 0
    1 0 1 1 1 0 0 0 1 1
    0 0 1 1 1 1 1 1 0 0
    0 0 1 0 0 0 1 1 1 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 390089 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 0 1 0 1 0 1
    0 1 1 0 0 1 0 1 1 1
    1 1 1 1 0 0 0 1 1 1
    1 0 0 0 1 0 1 1 1 0
    0 0 1 1 1 1 1 0 1 0
    1 1 0 1 1 0 1 1 0 1
    1 0 0 1 1 0 1 0 1 0
    0 1 1 0 1 1 0 1 1 1
    1 1 1 1 0 1 0 1 1 1
    1 1 0 1 0 1 1 1 0 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 386418 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 0 1 1 0 0 1
    1 0 1 1 1 1 0 0 1 1
    1 0 1 1 1 1 0 1 1 0
    1 1 1 1 1 1 0 1 1 1
    1 1 1 0 1 1 1 1 0 1
    1 1 0 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 0
    0 0 1 1 1 1 1 0 1 1
    1 1 1 1 1 0 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 383560 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 0 0 1
    1 1 1 0 1 1 0 0 0 1
    0 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 0
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 0 1 0
    0 1 1 1 1 0 0 0 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 349926 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 0 1 1 0
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    0 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 345456 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 0
    1 1 1 0 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 0 1 1
    1 1 1 1 1 1 0 0 0 0
    1 1 1 0 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 371340 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 1 1 1
    0 1 1 1 1 0 1 1 1 1
    1 0 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 0 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 414555 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 0 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 0 0 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 363292 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 1 0 0 0 1 0 1 0
    1 0 0 0 1 1 1 0 1 0
    0 1 1 1 0 0 1 1 1 0
    0 1 1 0 1 0 0 0 1 0
    1 1 1 0 1 0 1 1 1 1
    0 1 0 1 1 1 0 0 1 0
    1 1 1 1 1 0 0 0 0 0
    0 1 1 0 1 1 1 0 1 1
    0 1 1 0 1 0 1 1 0 0
    0 1 0 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 398102 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 0 1 1 1 1 0
    1 0 1 1 0 1 1 1 0 1
    1 1 1 1 0 1 1 0 1 1
    0 1 1 1 0 1 1 1 1 1
    0 0 1 1 1 1 1 1 0 1
    1 1 1 0 1 1 1 1 1 1
    1 1 0 1 1 0 0 1 1 0
    1 1 1 1 1 1 0 1 0 0
    1 1 0 0 1 1 1 0 1 1
    0 0 1 1 1 1 0 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 413389 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 0 1 0 1
    1 1 1 1 0 1 0 1 0 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 0 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 0 1 0 1 1 1 0 1
    0 0 1 1 0 1 1 1 1 1
    0 0 1 1 1 1 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 358174 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 1 1
    1 1 0 1 1 0 1 1 1 1
    1 1 1 1 1 0 1 1 0 1
    1 1 1 0 1 1 1 1 0 1
    0 0 1 1 0 0 1 1 1 0
    1 1 0 1 1 1 0 1 1 0
    1 1 0 0 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    0 1 1 0 0 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 332082 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 0 1 0 1 1
    1 0 1 1 1 0 1 0 1 1
    1 1 0 1 1 1 0 1 1 1
    1 1 1 1 0 1 1 0 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 0 1
    1 0 0 1 1 1 1 1 1 1
    1 0 1 1 1 0 1 1 1 1
    1 1 1 0 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 395254 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 0 1 1 1 1
    0 1 1 0 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 0 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 353055 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 336897 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 0 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 0 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 0 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 0 1 1
    0 1 1 1 0 1 1 1 1 0
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 361530 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 0 0 0 1 0 1 1
    1 1 1 0 0 0 1 1 0 0
    0 1 0 1 0 0 0 1 1 0
    0 1 0 1 1 1 0 1 0 0
    1 0 0 0 0 1 1 0 0 0
    1 0 0 1 1 1 0 0 1 1
    1 1 1 1 1 0 0 1 0 1
    1 1 0 1 1 1 0 0 0 0
    1 1 0 1 1 0 0 0 0 1
    1 0 0 0 1 1 1 0 0 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 402144 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 0 1 1 1
    1 1 1 0 0 0 1 1 1 0
    0 0 0 0 1 1 1 0 0 1
    1 1 0 1 0 1 1 1 0 1
    0 1 0 1 1 1 1 0 0 1
    1 0 1 1 1 0 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 0 1 0 0 0 1
    0 1 1 1 0 0 1 1 1 0
    0 1 0 1 0 1 0 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 396859 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 0 1 1 1 0 1
    0 0 1 0 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 0 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 0 1 1 0 1 0 1 1 1
    1 1 0 0 1 1 1 0 0 1
    1 1 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 325099 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 0 1 1
    1 1 1 1 1 0 0 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 0 1 0 1 1 1 1 1
    0 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 0 1 0 1 1
    1 1 1 1 1 1 0 1 0 1
    1 1 0 1 1 1 1 1 1 1
    1 0 1 1 0 1 1 1 1 1
    0 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 407332 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 0 1 1 1
    1 1 1 1 1 1 0 1 1 1
    0 1 1 1 1 0 1 1 0 1
    1 1 1 1 1 1 1 0 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 331836 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 0 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 0 0 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 0 1 1 0 1 0
    1 0 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 0 0
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 358538 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    0 1 1 1 1 1 0 1 1 1
    0 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 0 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 352550 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 0 1 1
    1 1 1 0 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 0 0 1 1
    1 1 1 0 0 1 1 0 1 1
    1 0 1 1 0 1 1 1 1 1
    1 1 1 0 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 397398 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 1 1 1 0 1 1 0 1
    0 0 1 1 0 1 0 1 0 0
    0 0 0 1 1 1 1 1 1 0
    1 1 1 1 0 0 1 1 0 0
    1 1 1 1 0 0 1 1 0 1
    1 0 1 1 0 1 0 1 0 0
    0 0 0 0 1 0 0 1 0 1
    0 1 1 1 0 0 1 0 1 1
    1 1 0 0 1 1 0 0 0 1
    0 1 1 0 1 1 0 1 1 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 419033 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 0 1 0 0 1 1 1
    1 0 0 1 1 1 0 1 1 1
    0 1 1 1 1 1 1 0 0 1
    0 0 0 1 1 1 0 1 1 0
    1 1 0 1 0 1 0 0 0 0
    1 1 1 1 1 1 1 1 0 0
    0 1 0 1 1 1 1 0 1 0
    1 0 1 1 0 1 0 1 0 1
    1 0 1 1 1 0 0 1 1 1
    1 0 0 0 1 1 0 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 390471 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 0 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 0 0 1 1 1 0 1 1
    0 1 0 1 1 0 1 1 0 0
    0 1 1 0 1 1 1 0 0 0
    1 1 1 1 1 1 1 0 1 1
    0 1 1 0 1 1 1 1 1 0
    1 0 1 1 1 0 1 1 1 0
    0 1 1 1 1 0 1 1 1 0
    1 0 1 1 1 1 0 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 392099 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 0
    1 1 1 0 0 1 0 1 1 1
    1 0 0 1 1 0 1 1 1 1
    1 1 1 1 1 0 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 0 1 0 0 1 0
    1 1 1 0 1 1 1 0 1 0
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 0 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 367900 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 0 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 0 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 404255 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 0 0 1 1
    1 1 0 1 1 1 1 0 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 0 1 0 1 1 1 0 0 0
    1 1 1 1 0 1 1 1 1 0
    1 1 1 1 0 1 1 1 0 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 412397 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 0 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 0 1 1 0 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 0 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 376528 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 0 1 1 1 0 1
    1 0 1 1 1 1 0 1 1 1
    0 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 0 1 1 1 1
    1 1 0 1 1 1 1 1 1 0
    1 1 1 1 1 0 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 361981 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 0 0
    0 0 0 0 1 1 1 1 0 0
    1 0 0 1 0 1 1 1 1 1
    1 0 1 1 1 0 1 0 0 0
    0 0 0 1 1 1 1 0 0 0
    1 0 0 0 0 0 0 0 1 1
    0 1 1 0 0 1 0 0 1 0
    1 0 1 1 1 0 0 0 1 0
    0 0 1 0 1 0 0 1 1 1
    1 0 0 0 0 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 408066 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 1 1 1 1 1 0 1
    1 1 1 0 1 1 1 0 0 1
    0 1 0 1 1 0 0 1 1 0
    0 1 0 0 1 1 0 0 1 1
    0 1 0 1 0 0 1 0 1 1
    1 0 0 0 1 1 1 0 0 1
    1 0 1 1 0 1 0 0 1 1
    1 1 1 0 1 0 1 1 1 1
    1 1 0 1 1 0 0 1 1 0
    0 1 1 0 0 1 1 0 1 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 413328 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 1 1 1
    1 1 1 0 0 1 1 0 0 1
    0 1 1 1 1 0 1 0 1 0
    1 0 1 1 1 1 1 1 1 1
    0 1 1 1 1 0 1 1 0 1
    1 1 1 1 1 1 1 0 1 0
    1 1 0 1 1 0 0 1 1 1
    1 1 1 1 0 0 1 1 1 1
    1 1 0 0 1 0 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 408419 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 1 1 0 1 1 1 1
    1 1 1 1 1 1 0 0 1 1
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 0 0 1 1 1
    1 1 1 1 1 1 1 1 1 0
    0 1 1 0 1 1 1 0 1 1
    1 1 1 1 1 0 0 0 0 1
    0 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 0 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 333812 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 0 0 1
    1 0 0 0 0 1 0 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    0 1 0 1 1 0 1 1 0 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 356728 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 0 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 0
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 355412 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    0 1 0 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 0 1
    0 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 367577 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 0 0 1
    1 0 0 0 1 1 1 1 1 1
    0 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 0 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 341290 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 0
    1 0 1 1 1 1 1 1 0 1
    1 0 0 0 0 0 1 1 1 1
    0 1 0 0 0 0 1 1 1 0
    0 0 0 1 0 1 0 1 1 1
    1 0 0 1 1 1 1 1 1 0
    0 0 1 1 0 0 1 1 1 0
    1 0 1 1 1 1 1 0 0 0
    0 1 1 1 1 1 1 0 1 0
    0 0 1 0 1 0 1 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 371535 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 0 1 1 1 0
    0 0 1 0 0 1 0 0 1 0
    1 1 1 1 1 1 0 1 1 1
    1 0 1 0 1 1 1 0 0 1
    1 0 1 1 1 0 0 0 0 1
    1 1 1 1 1 0 1 1 0 1
    0 1 1 1 1 1 0 1 1 1
    0 1 0 1 1 1 1 1 1 0
    1 0 0 1 1 1 1 0 0 1
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 370384 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 0 1 1 1 0 0 1
    1 0 1 1 1 0 1 1 1 0
    1 1 1 1 1 1 1 1 1 0
    0 1 0 1 0 1 1 1 1 0
    1 0 1 0 0 1 0 0 1 1
    1 1 1 1 0 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 0 1 1 0
    1 1 0 1 1 1 1 1 1 1
    0 1 0 1 0 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 373957 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 0 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 0 0 1 1 1 0 1
    1 1 0 1 0 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 0 1 1 1 1 1 1 0 1
    0 1 1 1 0 0 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 349418 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 0 1 1 0 1 1
    1 0 1 1 1 1 1 1 1 0
    1 0 1 0 1 1 0 0 1 1
    1 1 1 1 1 0 1 0 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 0 1 1 0 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 389454 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 0 1 0 1 1
    1 0 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 0 0 1
    1 1 1 1 1 0 1 0 1 1
    0 0 1 1 1 1 1 0 1 0
    0 1 0 0 1 0 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 330591 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 0 1 0 0 1 1
    1 0 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 325259 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 1 1 1 0
    1 0 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 0 1
    1 1 1 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 324431 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 0 0 1 1 1 1 1 0
    0 1 0 0 0 1 1 1 1 0
    0 0 0 0 1 0 1 0 1 1
    1 0 0 0 0 1 1 1 1 0
    0 1 0 0 0 1 0 0 0 1
    0 1 0 0 0 1 0 0 0 0
    0 1 0 0 0 1 0 0 0 1
    0 0 1 0 1 0 1 1 0 1
    1 0 0 1 0 1 1 1 1 1
    1 1 1 1 0 0 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 351623 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 1 0 0 1 0 0 1
    1 0 1 0 1 0 1 1 0 0
    0 1 1 1 0 0 0 1 1 0
    0 1 1 1 1 1 1 0 1 1
    0 1 0 0 1 1 1 0 1 0
    1 1 0 0 1 1 0 1 0 1
    0 1 1 1 1 1 1 0 0 1
    0 1 0 0 1 0 0 1 0 1
    0 1 1 1 1 1 0 1 1 1
    1 1 0 0 0 0 1 0 1 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 393617 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 0 1 1 1 1 1
    0 1 0 1 1 1 1 1 0 1
    1 0 1 0 1 1 0 1 1 1
    1 1 1 0 0 0 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 0 0 0 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 381455 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 0 1
    1 1 0 1 1 1 1 1 1 1
    0 1 0 0 1 1 1 1 1 1
    1 0 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 416134 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 1 1 1 1 1 1 1
    1 0 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 0 1 1 1 1 0 1 0 1
    1 1 1 1 1 0 1 1 1 0
    1 1 1 1 1 1 0 0 0 1
    1 0 0 0 1 1 1 0 1 1
    1 0 0 1 1 1 1 0 1 1
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 411053 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 0 0 1 1 1 1
    1 1 1 1 1 1 1 0 0 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 0 1 1 1 1 0 1
    1 1 0 1 1 1 1 1 0 1
    1 1 1 1 0 1 1 0 1 1
    1 1 0 1 1 1 1 1 1 0
    1 1 1 1 0 1 1 0 1 1
    0 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 387673 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 1 1 0 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 0 0 1 1
    1 1 1 0 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 0 1 0 1 1 1 1
The largest isosceles triangle has a size of 4
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
