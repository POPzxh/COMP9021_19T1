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
>>> print(os.popen('echo 345135 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 0 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 0 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 367202 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 1 0 1 0 1 0 1
    1 0 1 0 1 0 0 1 1 1
    1 0 1 0 0 1 1 0 1 0
    1 0 1 0 1 1 1 1 0 1
    1 1 1 0 0 0 0 1 0 0
    0 1 1 0 0 0 0 1 0 1
    0 1 1 0 1 1 1 1 1 1
    1 0 0 1 0 1 1 0 1 1
    0 1 0 1 0 0 0 0 1 1
    0 0 1 1 0 1 1 1 0 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 386300 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 0 1 1 0 0 1
    0 1 1 0 1 1 1 1 1 1
    1 1 1 1 0 1 1 0 0 1
    1 0 1 1 0 0 1 1 1 1
    1 1 0 1 1 0 0 1 0 0
    1 1 0 0 1 0 1 1 1 1
    0 1 1 1 1 0 1 1 0 1
    1 0 0 1 0 1 1 0 0 1
    1 1 0 0 1 0 1 0 1 1
    0 0 1 0 1 1 1 1 0 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 414614 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 0 1 1 1 1
    1 1 1 1 0 0 0 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 0 1 1 0 1 0 1 0 1
    1 0 1 1 1 1 0 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 0 0 1 1 1 0 1
    1 0 0 1 1 1 1 0 1 1
    0 1 1 1 1 0 1 0 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 330735 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 0 1 0 1 1
    1 1 1 1 1 0 1 0 1 1
    1 1 1 1 0 1 1 1 1 1
    0 0 1 0 0 1 0 0 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 0 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    0 1 1 1 1 1 1 1 0 1
    0 1 0 0 1 1 0 1 0 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 379146 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 0 1 1 0 1
    1 1 1 1 1 1 1 0 0 1
    1 1 1 1 1 1 1 1 0 1
    1 0 1 1 1 1 1 1 1 1
    0 1 0 1 0 1 1 0 0 1
    1 1 0 0 1 1 1 1 1 1
    1 1 1 0 0 1 1 1 1 1
    1 0 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 386265 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 0 1 1 1 0 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 0 1 1 1 1 1
    1 1 1 0 1 1 0 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 0 1 0 1
    1 1 1 1 0 1 1 0 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 374803 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 0 1 1
    1 1 1 0 1 0 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 0 1 1 1 0 1 1 1 1
    0 1 1 1 0 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 345353 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    0 1 1 0 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 374342 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 0 1 1 0 0 0 0 1
    0 0 0 1 1 1 0 1 0 0
    1 0 1 1 0 1 1 1 1 0
    0 1 1 1 1 0 0 0 0 1
    0 1 0 0 0 0 1 0 0 0
    0 1 0 1 1 1 0 0 1 1
    1 1 0 0 1 0 1 0 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 0 0 1 0 1 0 1 1
    0 0 0 1 0 1 1 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 391802 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 1 1 1 1 1 0 1 0
    1 1 0 0 0 1 1 1 1 1
    1 1 1 1 1 1 0 0 0 1
    1 0 0 1 0 1 1 1 0 1
    0 1 1 1 0 1 1 0 0 1
    0 0 1 1 0 1 1 0 1 1
    1 0 1 0 1 0 1 1 0 1
    1 1 1 1 1 0 1 1 0 0
    1 0 1 1 1 1 1 1 0 1
    0 1 1 0 1 0 1 1 1 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 354774 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 0 1 1
    1 1 1 0 1 0 1 1 0 1
    1 0 0 0 1 1 1 1 0 1
    1 1 1 1 1 1 0 1 1 1
    0 1 0 1 1 1 1 1 1 1
    0 0 1 1 1 1 1 0 1 1
    1 1 1 0 1 0 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
    1 0 1 1 1 1 0 1 0 1
    1 1 1 0 1 1 0 0 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 393307 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 0 1 1 0 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 0 1 0 0 0
    1 1 1 1 0 1 0 0 1 1
    0 1 1 1 0 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 0 0 1 1 1 1 1 0
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 0 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 401206 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 1 1 1 0
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 0
    0 0 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 0 0 1
    1 1 1 1 1 0 1 1 0 1
    1 1 0 1 1 1 1 1 1 1
    1 1 0 0 1 1 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 418640 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 0 1 1
    1 1 0 1 1 1 1 1 0 0
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 0
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 340848 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 0 1 1 1 0 1 1 1 1
    1 1 0 1 1 1 1 0 1 1
    0 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 0 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 367375 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    0 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 373023 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 0 1 0
    0 0 0 1 0 0 1 0 1 0
    0 1 1 0 1 1 1 1 0 1
    1 0 0 1 0 0 1 1 0 1
    0 1 0 1 0 1 1 0 0 1
    0 0 1 0 0 1 0 0 0 1
    1 1 0 0 1 1 0 1 0 0
    1 1 0 0 1 1 1 1 1 1
    1 1 0 1 1 0 1 1 1 0
    1 0 1 1 0 0 1 1 0 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 418018 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 0 1 0 1 1 1
    1 0 1 1 1 1 0 1 0 1
    0 1 1 0 1 0 0 1 0 1
    0 1 1 1 1 0 0 1 0 1
    0 0 1 1 0 0 1 0 0 0
    1 0 1 1 1 0 1 1 1 1
    0 1 0 1 1 1 1 1 0 1
    0 1 1 1 1 0 1 1 0 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 420133 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 0 1 1 0 0
    1 1 1 0 1 1 0 0 0 1
    1 1 1 0 1 1 1 0 1 1
    1 1 0 1 1 1 0 1 1 1
    1 0 1 1 1 1 0 1 1 1
    1 1 0 0 1 1 0 0 0 0
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 0 1 1 0 0 1 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 334319 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 1 1 0
    1 1 0 1 1 0 1 1 1 1
    1 0 1 0 0 1 1 1 0 1
    0 1 0 1 1 1 1 1 1 1
    1 1 1 0 0 1 1 1 1 1
    1 1 1 1 0 0 1 1 0 1
    1 1 1 1 1 0 1 1 1 0
    1 0 1 1 1 1 0 1 0 1
    1 1 1 1 1 1 1 0 0 1
    1 1 1 0 0 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 373998 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 0 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 0 1 1 1 1 1 1
    1 1 1 0 1 1 0 0 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 0 1 1
    1 1 1 0 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 332060 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    0 1 1 1 1 1 1 0 1 1
    1 1 0 1 1 0 1 0 0 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 0 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 332137 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 0 0 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 0 0
    1 1 0 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 379871 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 0 0 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 338138 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 0 1 1 1 0 1 1
    0 0 1 1 1 0 0 0 0 0
    1 0 1 1 0 0 1 0 1 0
    1 0 0 0 0 1 1 0 0 0
    1 1 0 1 1 1 0 0 1 1
    0 1 0 1 1 0 0 1 1 0
    0 0 1 0 0 0 1 0 1 0
    1 1 1 1 1 1 1 0 1 1
    1 0 1 1 0 0 1 1 0 0
    1 1 1 1 1 1 0 1 0 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 372282 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 0 1 0 0 1 1 1
    1 1 0 1 0 0 0 1 0 0
    1 0 0 0 1 1 0 0 0 1
    1 0 1 0 1 0 0 1 1 1
    1 1 0 1 1 1 0 1 1 1
    0 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 0 0 1 1 0
    1 1 0 1 1 1 1 1 1 1
    0 0 1 1 1 1 1 0 0 1
    1 0 1 1 0 0 0 0 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 399815 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 0 0 0 1 1 0
    0 0 1 0 0 1 1 1 1 0
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 0 1 1 1 1 1
    1 1 1 0 1 0 1 1 1 1
    1 1 1 1 1 0 1 1 0 1
    1 1 1 0 0 1 1 1 1 0
    1 1 1 1 0 1 0 0 1 0
    1 0 1 1 1 0 1 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 349730 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    0 1 1 0 1 1 0 1 0 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 0 1 0 1 0 1
    1 1 1 0 1 1 1 1 1 1
    0 1 0 1 1 1 0 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 0 0 1 1 1 1 0 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 363181 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 1 0
    1 1 0 0 1 1 1 1 0 1
    1 0 1 0 1 1 1 0 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 0 1 1 1 1 1 1 0
    1 0 1 1 1 1 1 1 1 1
    0 0 1 1 1 1 1 1 1 0
    1 1 1 0 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 393500 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 0 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 0 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 369763 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 0 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 0 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 0
    1 1 1 1 0 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 0 0 1 0 1
    1 1 1 0 0 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
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
