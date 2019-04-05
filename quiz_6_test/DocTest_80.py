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
>>> print(os.popen('echo 373111 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 0 1 1 1 1 0
    1 1 1 1 1 1 1 1 0 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 0 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 411315 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 0 0 1 0 0 0 0 1
    1 0 0 1 0 0 0 0 1 1
    1 1 1 0 1 1 1 1 0 0
    0 0 0 1 0 0 1 1 0 1
    1 1 1 0 1 0 0 1 0 1
    0 0 0 1 0 1 1 0 0 1
    1 1 0 0 1 1 1 1 1 0
    1 0 1 0 1 0 1 1 1 0
    0 0 0 1 0 1 1 0 1 1
    1 0 0 0 1 1 1 0 1 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 322846 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 0 1 0 1 0 1 1
    1 0 1 0 1 0 0 1 0 0
    0 0 0 0 0 1 0 1 1 1
    1 1 1 0 1 1 1 0 1 1
    0 1 0 0 0 1 0 1 0 0
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 0 0
    1 1 0 1 1 0 1 0 1 1
    0 0 0 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 394127 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 0
    0 1 1 0 1 0 1 1 1 0
    1 1 1 1 1 0 0 1 1 1
    1 0 1 0 1 1 1 0 1 1
    1 1 1 1 0 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 1
    0 0 0 0 1 1 1 0 0 1
    1 0 1 1 0 1 1 1 0 0
    0 1 0 1 0 1 1 0 1 1
    1 1 1 0 1 1 1 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 420654 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 1 0 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 0 1 1 1 1 0 1 1
    1 1 0 1 1 1 1 1 0 0
    1 1 1 0 1 1 1 1 1 1
    1 0 1 1 1 1 1 0 1 1
    1 1 0 0 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 0 1 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 388703 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 1 1 0 1
    0 1 1 0 1 0 1 1 0 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 1 1 1 1 1
    1 0 1 1 1 0 0 1 1 0
    1 1 1 1 1 1 1 1 1 1
    0 1 0 1 1 1 1 1 0 0
    0 1 1 1 1 1 1 1 1 0
    1 1 0 1 1 1 0 1 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 334614 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 0 1 0 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    0 1 1 0 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 0
    0 1 1 1 1 1 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 418823 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 1 1 1 0 1 1 1
    1 1 0 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 0
    0 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 361308 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 0 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 356752 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 0 1 1 1 1 0 0 0
    1 0 0 0 0 1 0 0 0 0
    0 1 0 0 0 0 1 1 1 0
    1 1 0 1 0 1 0 1 1 0
    1 0 0 1 0 1 0 0 0 1
    1 1 1 0 1 0 1 1 1 0
    1 1 1 1 1 1 1 1 0 0
    1 1 0 1 1 0 0 0 1 0
    0 1 0 1 0 0 0 1 1 1
    1 1 0 1 0 1 1 1 1 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 339515 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 1 1 1
    0 0 1 1 1 0 1 0 0 1
    0 0 1 1 0 1 1 1 1 1
    1 1 0 0 1 0 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    0 0 1 1 1 1 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 0 0 0 1 1 1 1 1 1
    0 1 0 0 1 0 1 1 1 1
    1 1 1 0 0 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 384838 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 0 0 1 1 0 0
    0 0 1 0 1 1 0 1 0 1
    0 1 1 0 1 1 1 1 1 1
    1 1 0 0 0 1 0 0 1 1
    0 0 1 0 0 1 1 0 1 1
    0 1 1 0 1 0 1 1 1 1
    1 1 0 0 1 1 1 1 1 1
    1 1 1 0 1 1 0 1 1 1
    0 1 1 1 0 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 350340 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 0 1 1 1 0 1 1 1 1
    1 0 1 1 1 1 1 1 0 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 0 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 0 1 0 0 1 1 1 1 1
    0 1 1 1 0 1 1 1 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 392253 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 0 1 1 1 0 1 1 1
    1 1 1 0 1 1 0 1 1 1
    1 1 1 0 0 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    0 0 0 1 1 1 1 1 1 0
    1 1 1 1 1 1 0 1 0 0
    1 1 1 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 391410 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 1 1 1
    0 1 1 1 1 1 1 1 1 0
    1 0 0 1 0 1 1 1 1 1
    1 1 1 0 0 1 0 1 1 0
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 0
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 0 1 1
    1 0 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 0 1 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 378075 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 1 0 0 1 0
    1 0 1 1 0 1 1 1 1 1
    0 1 1 1 1 0 0 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 0 1 0 0 1
    1 1 1 0 1 1 0 1 1 0
    1 1 1 1 1 0 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 0 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 359530 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 0 1 1 1 1
    0 1 1 1 1 1 0 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    0 1 1 1 1 0 1 1 1 0
    1 1 1 1 1 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 356630 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 1 0 1 1 1 1 1 1
    0 0 1 0 1 1 1 1 0 0
    0 1 0 0 0 1 1 0 0 1
    0 1 1 1 1 1 1 0 1 0
    1 1 1 1 1 0 1 0 1 1
    1 0 0 1 1 0 0 0 0 1
    0 1 0 0 0 0 0 1 0 1
    1 1 0 1 0 1 0 1 1 0
    1 0 1 1 0 0 0 0 1 0
    1 1 1 0 0 0 0 0 0 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 372579 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 0 0 1 0 1 1 1 1
    1 0 1 1 1 1 1 1 0 0
    0 1 1 1 1 1 1 1 1 1
    0 0 1 0 1 0 1 1 1 1
    0 1 0 1 0 1 1 1 1 0
    0 0 1 0 1 1 0 1 1 1
    0 1 1 1 1 0 1 0 0 1
    1 1 1 0 1 1 1 1 1 1
    0 1 1 1 0 1 0 1 1 1
    0 1 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 323714 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 1 1 1 0
    1 1 1 0 0 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    0 1 1 1 1 1 0 1 0 0
    1 0 1 1 1 1 0 1 1 1
    0 0 0 1 1 1 0 0 0 1
    1 1 1 1 0 1 1 1 0 1
    1 1 0 1 0 0 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 365136 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 0 0 0 1
    1 1 1 1 1 1 1 0 1 1
    0 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 0 1 0 0 1
    1 0 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 0 0 0 1
    1 1 1 1 1 1 1 1 1 0
    1 1 0 1 0 1 1 1 1 1
    1 1 0 1 1 1 1 1 0 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 402597 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 0 0 1
    1 0 1 1 1 1 1 1 1 1
    1 0 0 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 0 1
    1 1 1 1 1 1 0 0 1 1
    1 0 1 1 1 1 1 1 0 1
    0 1 1 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 375380 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 0 0 1 1 1 1
    0 1 1 1 1 1 1 1 1 0
    1 1 1 1 0 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 0 0 1 1
    1 1 1 1 0 1 1 1 1 1
    0 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 321521 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 0 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 372553 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    0 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 370010 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 0 1 1 1
    1 0 0 1 0 1 0 1 1 0
    0 0 1 1 0 1 1 0 0 0
    0 1 0 0 1 1 1 1 0 1
    0 1 1 1 1 1 0 0 0 1
    1 0 1 1 0 0 1 0 1 0
    0 0 1 0 0 0 0 0 0 1
    1 1 1 0 0 0 0 0 0 0
    1 1 1 1 0 1 0 0 0 0
    1 1 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 341830 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 0 1 1 0 1 1 1
    1 1 1 0 0 1 1 1 1 1
    1 1 0 0 0 1 1 1 1 1
    1 0 0 0 1 0 0 0 1 0
    0 1 1 1 1 1 1 0 1 1
    0 0 1 1 0 0 0 0 1 0
    1 1 0 1 1 0 1 0 1 0
    1 1 1 0 0 1 1 1 0 1
    0 1 0 1 0 1 1 0 0 1
    0 0 1 1 0 1 0 0 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 325237 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 0 1 1
    1 1 1 0 1 1 0 1 1 1
    1 1 0 1 0 1 1 1 0 1
    1 1 1 1 0 1 0 1 1 1
    1 1 0 0 0 1 1 0 1 1
    0 0 1 1 1 1 0 1 1 1
    1 1 1 1 0 0 0 1 1 1
    0 1 0 0 1 1 0 1 1 1
    1 1 0 1 1 1 1 0 1 1
    1 1 1 1 0 1 1 1 0 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 376595 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 0 0
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    0 1 0 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 0 0 1 1 1
    1 0 0 1 1 1 1 1 1 0
    1 1 0 1 1 1 1 0 1 1
    1 1 0 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 403363 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 0 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 0 0
    1 1 1 1 1 1 0 1 1 0
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 398783 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 0 1 1 1 0 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 0 1 1 0 1
    1 0 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 0 1
    1 1 1 0 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 0 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 389895 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 0 1 1 1 1
    1 0 0 1 1 0 1 1 1 1
    1 0 0 1 0 0 1 1 1 1
    1 1 0 1 1 0 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 0 1 0 0 1 1 1
    1 1 1 1 1 1 1 1 0 0
    1 1 1 1 1 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 367814 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 1 1 1 1
    1 1 0 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 0 1 1 1 0 0 0 1 0
    1 1 1 1 1 0 1 1 0 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 345325 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 1 0 1 0 1 0 1
    1 1 0 0 0 1 1 1 0 0
    1 0 1 1 0 0 0 1 0 1
    1 0 1 1 1 0 1 1 0 1
    1 1 1 0 1 0 1 1 0 0
    1 0 0 1 0 1 0 0 0 0
    1 1 0 1 1 0 0 1 0 0
    1 0 0 1 1 0 0 1 1 0
    1 0 1 1 0 1 1 0 1 0
    1 0 0 1 0 0 0 0 1 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 405778 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 0 0 1 1 1 1 0
    1 0 1 1 0 1 0 0 0 1
    0 1 1 1 1 0 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 0 1 1 1 0 1 1 1 1
    0 1 1 0 0 1 1 1 1 1
    1 0 1 1 1 1 1 0 0 1
    1 0 1 1 0 0 1 0 1 1
    0 1 0 1 1 1 1 0 0 1
    1 0 0 1 0 0 0 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 387971 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 0 0 0 1 1 1
    1 0 1 1 1 1 0 1 1 0
    1 1 0 1 1 1 0 1 0 1
    1 1 1 0 0 1 0 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 0
    0 1 0 1 1 1 1 1 1 1
    1 0 1 0 1 1 1 0 1 0
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 346622 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    0 0 0 1 1 0 1 0 1 0
    1 0 1 1 1 1 0 1 1 1
    1 0 1 1 1 1 1 1 0 0
    1 0 1 1 1 1 1 1 0 0
    1 1 1 1 0 1 1 0 0 1
    1 0 0 1 0 1 1 1 1 1
    1 0 0 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 335779 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 1 0 1 1
    1 1 1 0 1 1 1 1 1 0
    0 0 1 1 0 1 0 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 0 0 1 0 1 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 322997 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 0 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 0 0 1
    1 1 1 1 1 1 0 0 1 1
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 351909 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 0 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 375782 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 0
    1 1 0 1 0 1 1 1 0 1
    1 1 1 1 0 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 397356 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 1 1 1 1 0 1 0
    0 0 0 1 0 0 0 1 1 1
    1 0 1 1 0 0 0 0 0 1
    0 1 0 0 0 0 0 1 1 0
    0 0 0 0 0 1 0 0 1 1
    0 1 0 0 1 0 1 0 0 1
    0 1 1 1 0 0 0 0 0 0
    0 1 0 0 1 1 1 1 1 0
    1 0 0 1 0 1 1 1 0 1
    1 1 1 1 1 0 1 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 391512 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 0 1 1
    1 1 0 0 0 0 1 1 1 1
    0 1 0 0 0 0 1 1 1 0
    1 1 1 1 0 1 0 1 1 1
    1 0 0 0 1 1 1 1 0 0
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 0 1 0 1 1 1 0 1 1
    0 0 0 1 1 1 1 0 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 392175 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 0 0 1 1
    1 1 1 0 1 0 1 1 1 0
    1 1 0 1 1 0 0 1 0 1
    0 1 1 1 0 0 1 1 0 0
    1 1 1 1 1 1 0 1 1 1
    1 1 1 0 0 1 1 0 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 0 1 1 1 1 1
    0 1 1 1 0 0 1 0 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 345701 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 0 1 0 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 0 1 1 1 0 0 1 1
    1 1 1 1 1 0 1 0 1 1
    1 1 1 1 1 0 1 1 1 1
    0 1 1 1 1 1 1 0 1 0
    0 1 1 1 0 0 1 1 1 1
    1 1 0 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 375972 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 1 1 1 0 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 0
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 0 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 417787 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 0
    1 0 1 1 1 0 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 0 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 0 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 0 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 394682 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 0 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 0 1 0 0 1
    1 1 1 0 1 0 1 1 1 1
    1 1 1 1 0 0 1 1 1 1
    1 1 1 0 1 1 0 0 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 351148 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 0 0 1
    1 1 1 1 1 1 0 1 1 1
    1 1 0 0 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 375713 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 0 0 0 1 1 0 1
    1 0 0 0 1 1 1 1 1 0
    1 0 0 1 0 1 0 1 0 0
    1 1 1 1 1 1 0 0 0 0
    1 0 1 0 1 1 0 1 0 0
    0 1 0 0 1 1 0 0 1 1
    1 0 0 1 0 0 0 0 1 1
    1 0 0 0 1 1 0 0 0 0
    0 1 1 0 0 1 0 1 1 1
    0 0 0 0 1 0 1 0 1 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 406539 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 0 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 0 1 0 1 1 0 1 0
    1 1 1 1 1 0 1 0 1 1
    1 0 1 1 1 1 1 1 0 1
    1 0 1 1 1 1 1 1 0 1
    1 0 1 0 1 1 1 0 0 1
    1 0 1 1 1 0 1 1 1 1
    1 0 1 0 1 1 1 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 361255 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 0 1 1 1 1 1
    1 1 0 1 1 1 0 1 1 1
    0 1 1 0 1 0 1 0 0 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 0 1 0 1 0 0
    1 1 0 1 0 1 1 1 1 0
    1 1 1 0 1 0 0 1 1 1
    0 1 0 1 1 1 1 0 1 1
    0 1 1 1 1 1 1 0 1 1
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 406768 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 0 1 0 1 1 1
    1 0 0 1 0 1 1 1 0 1
    1 0 1 1 0 1 0 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 0 0 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 387496 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 1 0 1 0
    1 1 1 1 1 0 1 1 1 1
    1 1 1 0 1 0 1 1 1 0
    1 1 1 1 1 1 0 1 1 0
    1 1 1 1 1 1 0 1 1 0
    1 1 1 1 1 1 0 1 1 1
    1 1 0 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 0 0 1 0
    1 1 1 0 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 410260 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 0 1 1 0
    1 1 1 0 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 0 1 1
    1 0 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 0 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 347943 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 1 0 1 1 1
    1 1 1 0 1 1 1 0 1 1
    0 1 1 1 1 1 1 1 1 1
    0 1 1 1 0 1 0 1 1 1
    0 1 1 1 1 0 1 0 1 1
    1 1 1 1 0 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 395158 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 0 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 0 1 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 392145 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 0 0 0 0 0 0 0
    0 1 0 1 0 0 0 0 0 1
    0 0 0 1 0 0 0 1 1 1
    1 1 1 0 1 1 0 0 0 1
    0 1 1 0 0 1 0 1 1 0
    0 1 0 0 1 1 0 1 0 0
    1 1 1 0 1 1 1 1 0 1
    1 1 1 1 0 0 0 1 0 0
    1 1 1 0 1 0 1 1 1 0
    0 1 0 0 0 0 1 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 322230 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 0 1 1 1 1
    1 1 1 0 1 0 1 1 1 1
    1 1 1 1 1 1 0 1 0 1
    1 1 0 1 1 1 0 0 0 1
    1 1 1 0 1 1 0 0 1 0
    1 1 1 1 1 1 1 1 1 1
    0 0 1 1 1 1 0 1 0 1
    1 1 1 0 1 1 1 1 1 1
    1 1 0 1 0 1 0 0 1 1
    1 1 0 1 1 1 0 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 381414 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 0 1 1 0 1 1
    0 0 1 1 1 0 1 1 0 0
    0 1 1 1 0 1 0 1 1 1
    1 0 0 0 0 1 1 1 1 1
    0 1 0 1 1 0 1 1 1 1
    0 1 1 1 0 1 1 1 1 1
    1 1 1 0 1 0 1 0 1 1
    1 1 1 1 1 1 0 1 1 1
    0 1 1 1 1 1 1 0 0 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 381821 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 0 0
    1 1 1 1 1 0 1 1 1 1
    1 1 0 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 0 1 1 1 1 0 0
    1 1 1 1 1 1 1 1 0 1
    1 1 1 0 1 0 0 1 0 1
    1 1 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 416619 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 0 0 1 1
    1 1 1 1 0 1 1 1 1 1
    1 0 1 1 1 1 1 0 1 0
    1 1 1 0 1 1 0 1 1 1
    1 1 1 1 1 1 0 1 0 1
    1 1 0 1 0 1 1 1 1 1
    0 1 0 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 332352 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 0 1 1
    1 0 1 1 1 1 0 1 1 0
    1 1 1 1 1 0 1 1 1 1
    0 1 1 1 1 1 1 1 1 0
    1 0 1 0 0 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 0 0 1 1
    1 0 1 1 0 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 415553 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    0 1 0 1 1 1 0 1 1 1
    1 1 1 1 0 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 352528 8| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 0 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 0 1 1 0 1
    1 1 1 1 1 1 0 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 0 0
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 345039 1| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 1 0 0 0 1 0 1 0
    1 1 1 0 1 0 1 0 0 0
    1 0 1 0 0 1 0 0 0 0
    1 0 0 0 0 0 0 0 0 1
    0 1 1 1 0 1 0 1 1 0
    0 1 0 0 0 1 1 0 1 0
    0 1 1 1 0 0 0 1 0 1
    0 1 1 0 0 1 1 0 0 1
    0 1 0 1 0 0 1 1 0 0
    1 1 1 0 0 1 0 1 0 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 345554 2| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 1 0 0 0 1 1 0
    0 1 1 1 0 0 0 1 0 1
    1 0 1 1 1 0 0 1 1 0
    1 1 1 1 1 0 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 0 0 1 1 1 1
    1 0 0 1 0 0 0 0 1 1
    1 1 0 0 1 1 1 1 1 0
    0 1 1 0 1 1 0 1 1 1
    1 0 0 0 0 0 1 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 387515 3| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 0 1 0 1 1
    0 1 1 1 1 0 1 0 1 1
    1 1 1 0 0 1 1 1 0 1
    0 1 1 1 1 0 1 1 0 1
    1 0 1 0 1 1 1 1 1 0
    1 1 1 1 1 0 1 0 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 0 0 1 0 0 1
    0 1 1 0 1 1 1 0 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 368333 4| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 0 1 1 1
    1 1 1 0 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 0 1 1 1
    1 1 0 1 1 1 1 1 0 1
    0 1 1 1 1 1 0 1 1 1
    1 1 1 0 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 0 1 1 1 1
    1 0 1 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 375727 5| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 1 1 1 1
    1 1 1 0 0 1 0 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 0 0 1
    1 1 1 0 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 0 1 1 0 0
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 0 1 1
    1 1 1 1 1 1 0 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 334093 6| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    0 1 1 0 0 0 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 0 1
    0 1 0 1 1 1 0 1 1 0
    1 0 1 1 1 1 1 0 1 0
    1 1 0 1 1 1 1 1 1 1
    1 0 1 1 0 0 0 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 347885 7| python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 0
    1 1 1 1 0 1 1 1 0 0
    1 0 1 1 0 1 0 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 0 0 1 0 1 1 1 1
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
