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
>>> print(os.popen('echo 93 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 0 1 1 1
    1 0 1 1 1 0 1 1 0 1
    1 1 1 1 0 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 0 0 1 1 1 0
    0 0 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 0 1 0 1
    1 0 1 1 0 0 1 1 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 93 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 0 1 0 0 1 0 0 1 1
    1 1 1 1 0 1 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 0 1 0 1 0 1 1 1 0
    1 1 0 0 1 1 1 0 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 93 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 0 1 1 0
    0 1 0 0 1 1 1 1 1 1
    1 1 1 0 1 0 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 0 1 0 1 1 0 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 93 9| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 0 1 1 0
    0 1 1 0 0 1 1 1 1 1
    1 1 1 1 0 1 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 93 10| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 0 1 1 0 0 1 1 1
    0 0 1 1 1 1 1 1 1 1
    1 1 0 1 0 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 93 11| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 0 1
    1 0 0 1 1 1 0 0 1 1
    1 1 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 31 12| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    0 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 31 13| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    0 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 31 14| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 0 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 31 15| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 31 16| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 31 17| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 98 18| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 98 19| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 98 20| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 98 21| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 98 22| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 0
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 98 23| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 47 24| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 0 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 47 25| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 0 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 47 26| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 0 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 47 27| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 0 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 47 28| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 0 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 47 29| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 0 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 28 30| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 28 31| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 28 32| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 28 33| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 28 34| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 0 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 28 35| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 68 36| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 68 37| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 68 38| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 68 39| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 68 40| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 68 41| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 81 42| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 81 43| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 81 44| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 81 45| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 81 46| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 81 47| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 54 48| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 54 49| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 54 50| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 54 51| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 54 52| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 54 53| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 96 54| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 96 55| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 96 56| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 96 57| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 96 58| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 96 59| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 7 60| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 7 61| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 7 62| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 7 63| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 7 64| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 7 65| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 31 66| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 31 67| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 31 68| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 31 69| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 31 70| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 31 71| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 22 72| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 22 73| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 22 74| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 22 75| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 22 76| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 22 77| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 33 78| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
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
